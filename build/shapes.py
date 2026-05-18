"""Генерация диаграмм через нативные шейпы Word (DrawingML).

Используем wp:inline + wpg:wgp (group shape) для размещения нескольких шейпов.
Каждая диаграмма — это группа shapes (rect, ellipse, line, arrow, text inside).

Координаты внутри группы — в EMU. 1 cm = 360000 EMU.
Размер диаграммы по умолчанию: 16x10 см = 5760000 x 3600000 EMU.

Особенности:
- Используем wpg:wgp для группы, чтобы все шейпы были на одной странице.
- Для каждого шейпа: wps:wsp с wps:spPr (геометрия + позиция + размер),
  wps:txbx (текст внутри) и wps:bodyPr.
- Текст внутри шейпа: a:p, a:r, a:t.
"""

# id-генератор
_uid = [1000]


def _next_id():
    _uid[0] += 1
    return _uid[0]


def _emu_cm(cm):
    return int(cm * 360000)


# ============================================================
# Базовые элементы
# ============================================================

def _txbx_content(text, font_size=10, bold=False, align="ctr", color="000000"):
    """text — может быть многострочным."""
    bold_attr = ' b="1"' if bold else ''
    sz = font_size * 100  # a:rPr sz в сотых долях pt
    paragraphs = []
    for line in str(text).split('\n'):
        line_xml = (
            f'<a:p>'
            f'<a:pPr algn="{align}"><a:defRPr sz="{sz}"{bold_attr}/></a:pPr>'
            f'<a:r>'
            f'<a:rPr lang="ru-RU" sz="{sz}"{bold_attr}>'
            f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
            f'<a:latin typeface="Times New Roman"/>'
            f'<a:cs typeface="Times New Roman"/>'
            f'</a:rPr>'
            f'<a:t>{_esc(line)}</a:t>'
            f'</a:r>'
            f'</a:p>'
        )
        paragraphs.append(line_xml)
    if not paragraphs:
        paragraphs.append('<a:p/>')
    return ''.join(paragraphs)


def _esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


def _shape(prst, x, y, w, h, text="", fill="FFFFFF", line_color="000000",
           line_width=12700, font_size=10, bold=False, font_color="000000",
           text_align="ctr"):
    """Создаёт wps:wsp шейп определённой пресет-формы.

    prst: rect, roundRect, ellipse, parallelogram, hexagon, diamond, etc.
    x, y, w, h: в EMU.
    """
    sid = _next_id()
    fill_xml = (f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>'
                if fill else '<a:noFill/>')
    line_xml = (f'<a:ln w="{line_width}"><a:solidFill><a:srgbClr val="{line_color}"/></a:solidFill></a:ln>'
                if line_color else '<a:ln><a:noFill/></a:ln>')
    txbx_xml = _txbx_content(text, font_size=font_size, bold=bold,
                             align=text_align, color=font_color)
    return (
        f'<wps:wsp>'
        f'<wps:cNvSpPr/>'
        f'<wps:spPr>'
        f'<a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm>'
        f'<a:prstGeom prst="{prst}"><a:avLst/></a:prstGeom>'
        f'{fill_xml}'
        f'{line_xml}'
        f'</wps:spPr>'
        f'<wps:txbx><w:txbxContent>{txbx_xml}</w:txbxContent></wps:txbx>'
        f'<wps:bodyPr wrap="square" lIns="36000" tIns="18000" rIns="36000" bIns="18000" anchor="ctr" anchorCtr="0"/>'
        f'</wps:wsp>'
    )


def rect(x, y, w, h, text="", **kw):
    return _shape("rect", x, y, w, h, text, **kw)


def roundrect(x, y, w, h, text="", **kw):
    return _shape("roundRect", x, y, w, h, text, **kw)


def ellipse(x, y, w, h, text="", **kw):
    return _shape("ellipse", x, y, w, h, text, **kw)


def diamond(x, y, w, h, text="", **kw):
    return _shape("diamond", x, y, w, h, text, **kw)


def parallelogram(x, y, w, h, text="", **kw):
    return _shape("parallelogram", x, y, w, h, text, **kw)


def hexagon(x, y, w, h, text="", **kw):
    return _shape("hexagon", x, y, w, h, text, **kw)


def actor(x, y, w=560000, h=900000, text=""):
    """Стилизованный «актор» UML (палочный человечек) — упрощённо как ellipse + label."""
    head = ellipse(x + w // 4, y, w // 2, h // 4, fill="FFFFFF", line_color="000000")
    # тело — line
    body = _line(x + w // 2, y + h // 4, x + w // 2, y + 3 * h // 4)
    # ноги
    leg1 = _line(x + w // 2, y + 3 * h // 4, x + w // 4, y + h)
    leg2 = _line(x + w // 2, y + 3 * h // 4, x + 3 * w // 4, y + h)
    # руки
    arm = _line(x, y + h // 2, x + w, y + h // 2)
    label = textbox(x - 200000, y + h, w + 400000, 360000, text,
                    fill="", line_color="", font_size=9, text_align="ctr")
    return head + body + leg1 + leg2 + arm + label


def _line(x1, y1, x2, y2, color="000000", width=9525):
    """Прямая линия."""
    sid = _next_id()
    # bbox of line
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1) or 1
    h = abs(y2 - y1) or 1
    flipH = 1 if x2 < x1 else 0
    flipV = 1 if y2 < y1 else 0
    flip_attrs = ''
    if flipH:
        flip_attrs += ' flipH="1"'
    if flipV:
        flip_attrs += ' flipV="1"'
    return (
        f'<wps:wsp>'
        f'<wps:cNvSpPr/>'
        f'<wps:spPr>'
        f'<a:xfrm{flip_attrs}><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm>'
        f'<a:prstGeom prst="line"><a:avLst/></a:prstGeom>'
        f'<a:ln w="{width}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:ln>'
        f'</wps:spPr>'
        f'<wps:bodyPr/>'
        f'</wps:wsp>'
    )


def line(x1, y1, x2, y2, color="000000", width=9525):
    return _line(x1, y1, x2, y2, color, width)


def arrow(x1, y1, x2, y2, color="000000", width=9525, dashed=False):
    """Линия со стрелкой на конце."""
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1) or 1
    h = abs(y2 - y1) or 1
    flipH = 1 if x2 < x1 else 0
    flipV = 1 if y2 < y1 else 0
    flip_attrs = ''
    if flipH:
        flip_attrs += ' flipH="1"'
    if flipV:
        flip_attrs += ' flipV="1"'
    dash_xml = '<a:prstDash val="dash"/>' if dashed else ''
    return (
        f'<wps:wsp>'
        f'<wps:cNvSpPr/>'
        f'<wps:spPr>'
        f'<a:xfrm{flip_attrs}><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm>'
        f'<a:prstGeom prst="straightConnector1"><a:avLst/></a:prstGeom>'
        f'<a:ln w="{width}">'
        f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
        f'{dash_xml}'
        f'<a:tailEnd type="triangle" w="med" len="med"/>'
        f'</a:ln>'
        f'</wps:spPr>'
        f'<wps:bodyPr/>'
        f'</wps:wsp>'
    )


def textbox(x, y, w, h, text, fill="", line_color="", font_size=10,
            bold=False, font_color="000000", text_align="ctr"):
    """Текстовый блок без границы."""
    fill_xml = (f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>'
                if fill else '<a:noFill/>')
    if line_color:
        line_xml = f'<a:ln><a:solidFill><a:srgbClr val="{line_color}"/></a:solidFill></a:ln>'
    else:
        line_xml = '<a:ln><a:noFill/></a:ln>'
    txbx_xml = _txbx_content(text, font_size=font_size, bold=bold,
                             align=text_align, color=font_color)
    return (
        f'<wps:wsp>'
        f'<wps:cNvSpPr/>'
        f'<wps:spPr>'
        f'<a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
        f'{fill_xml}'
        f'{line_xml}'
        f'</wps:spPr>'
        f'<wps:txbx><w:txbxContent>{txbx_xml}</w:txbxContent></wps:txbx>'
        f'<wps:bodyPr wrap="square" lIns="36000" tIns="18000" rIns="36000" bIns="18000" anchor="ctr" anchorCtr="0"/>'
        f'</wps:wsp>'
    )


# ============================================================
# Группа шейпов как inline-картинка
# ============================================================

def diagram(width_cm, height_cm, shapes_xml, name="Diagram"):
    """Возвращает w:p, содержащий <w:drawing><wp:inline> с группой шейпов.

    width_cm, height_cm — внешний размер диаграммы.
    shapes_xml — XML всех вложенных wps:wsp элементов.
    """
    cx = _emu_cm(width_cm)
    cy = _emu_cm(height_cm)
    sid = _next_id()
    drawing = (
        f'<w:p><w:pPr>'
        f'<w:spacing w:line="240" w:lineRule="auto" w:after="0" w:before="120"/>'
        f'<w:ind w:firstLine="0" w:left="0"/>'
        f'<w:jc w:val="center"/>'
        f'</w:pPr>'
        f'<w:r><w:rPr><w:noProof/></w:rPr>'
        f'<mc:AlternateContent>'
        f'<mc:Choice Requires="wpg">'
        f'<w:drawing>'
        f'<wp:inline distT="0" distB="0" distL="0" distR="0">'
        f'<wp:extent cx="{cx}" cy="{cy}"/>'
        f'<wp:effectExtent l="0" t="0" r="0" b="0"/>'
        f'<wp:docPr id="{sid}" name="{name}"/>'
        f'<wp:cNvGraphicFramePr/>'
        f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        f'<a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup">'
        f'<wpg:wgp>'
        f'<wpg:cNvGrpSpPr/>'
        f'<wpg:grpSpPr>'
        f'<a:xfrm>'
        f'<a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/>'
        f'<a:chOff x="0" y="0"/><a:chExt cx="{cx}" cy="{cy}"/>'
        f'</a:xfrm>'
        f'</wpg:grpSpPr>'
        f'{shapes_xml}'
        f'</wpg:wgp>'
        f'</a:graphicData>'
        f'</a:graphic>'
        f'</wp:inline>'
        f'</w:drawing>'
        f'</mc:Choice>'
        f'<mc:Fallback>'
        f'<w:pict><v:rect style="width:1pt;height:1pt"/></w:pict>'
        f'</mc:Fallback>'
        f'</mc:AlternateContent>'
        f'</w:r></w:p>'
    )
    return drawing
