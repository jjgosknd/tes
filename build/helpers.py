"""Хелперы для генерации DOCX вручную через zipfile + XML.

Соглашения:
- 1 EMU = 1/914400 inch. 1 cm = 360000 EMU.
- Размер шрифта в half-points: 14pt = 28.
- Отступы w:ind w:firstLine="709" — это абзацный отступ ~1.25 см.
- Межстрочный интервал 1.5 — w:line="360" w:lineRule="auto".
"""
from xml.sax.saxutils import escape as _xml_escape


def esc(text):
    if text is None:
        return ""
    return _xml_escape(str(text), {'"': '&quot;'})


# ============================================================
# Основные блоки
# ============================================================

def p(text="", style=None, align=None, first_line=True,
      bold=False, italic=False, size=28, font="Times New Roman",
      line=360, before=0, after=0, page_break_before=False,
      keep_next=False, keep_lines=False):
    """Параграф обычного текста."""
    ppr_parts = []
    if style:
        ppr_parts.append(f'<w:pStyle w:val="{style}"/>')
    if keep_next:
        ppr_parts.append('<w:keepNext/>')
    if keep_lines:
        ppr_parts.append('<w:keepLines/>')
    if page_break_before:
        ppr_parts.append('<w:pageBreakBefore/>')
    spacing_attrs = []
    if line is not None:
        spacing_attrs.append(f'w:line="{line}" w:lineRule="auto"')
    spacing_attrs.append(f'w:after="{after}"')
    spacing_attrs.append(f'w:before="{before}"')
    ppr_parts.append(f'<w:spacing {" ".join(spacing_attrs)}/>')
    if first_line:
        ppr_parts.append('<w:ind w:firstLine="709"/>')
    else:
        ppr_parts.append('<w:ind w:firstLine="0" w:left="0"/>')
    if align:
        ppr_parts.append(f'<w:jc w:val="{align}"/>')
    else:
        ppr_parts.append('<w:jc w:val="both"/>')

    rpr_parts = [f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}" w:eastAsia="{font}"/>',
                 f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>']
    if bold:
        rpr_parts.append('<w:b/><w:bCs/>')
    if italic:
        rpr_parts.append('<w:i/><w:iCs/>')

    ppr = '<w:pPr>' + ''.join(ppr_parts) + '<w:rPr>' + ''.join(rpr_parts) + '</w:rPr></w:pPr>'

    if text == "":
        return f'<w:p>{ppr}</w:p>'

    runs = []
    parts = text.split('\n')
    for i, part in enumerate(parts):
        runs.append(_run(part, font=font, size=size, bold=bold, italic=italic))
        if i < len(parts) - 1:
            runs.append(f'<w:r><w:rPr>{"".join(rpr_parts)}</w:rPr><w:br/></w:r>')

    return f'<w:p>{ppr}{"".join(runs)}</w:p>'


def _run(text, font="Times New Roman", size=28, bold=False, italic=False, color=None):
    rpr_parts = [f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}" w:eastAsia="{font}"/>',
                 f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>']
    if bold:
        rpr_parts.append('<w:b/><w:bCs/>')
    if italic:
        rpr_parts.append('<w:i/><w:iCs/>')
    if color:
        rpr_parts.append(f'<w:color w:val="{color}"/>')
    rpr = '<w:rPr>' + ''.join(rpr_parts) + '</w:rPr>'
    return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def h1(text, page_break_before=True):
    return p(text.upper(), style="Heading1", align="center", first_line=False,
             bold=True, size=28, line=360, before=0, after=0,
             page_break_before=page_break_before, keep_next=True)


def h2(text):
    return p(text, style="Heading2", align="both", first_line=True,
             bold=True, size=28, line=360, before=240, after=120, keep_next=True)


def empty_line(size=28):
    return p("", first_line=False, size=size)


def page_break():
    return ('<w:p><w:pPr><w:spacing w:after="0"/></w:pPr>'
            '<w:r><w:br w:type="page"/></w:r></w:p>')


# ============================================================
# Подписи
# ============================================================

def fig_caption(num, text):
    full = f"Рис. {num}. {text}"
    return p(full, align="center", first_line=False, before=60, after=240)


def table_caption(num, text):
    out = []
    out.append(p(f"Таблица {num}", align="right", first_line=False,
                 before=120, after=0, keep_next=True))
    out.append(p(text, align="center", first_line=False,
                 before=0, after=60, keep_next=True))
    return ''.join(out)


def listing_caption(num, text):
    full = f"Листинг {num}. {text}"
    return p(full, align="center", first_line=False, before=60, after=120)


# ============================================================
# Таблицы
# ============================================================

def _tbl_props(width=9638):
    return (
        f'<w:tblPr>'
        f'<w:tblW w:w="{width}" w:type="dxa"/>'
        f'<w:jc w:val="center"/>'
        f'<w:tblBorders>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'</w:tblBorders>'
        f'<w:tblLayout w:type="fixed"/>'
        f'<w:tblLook w:val="04A0"/>'
        f'</w:tblPr>'
    )


def _tbl_grid(col_widths):
    grid = '<w:tblGrid>'
    for w in col_widths:
        grid += f'<w:gridCol w:w="{w}"/>'
    grid += '</w:tblGrid>'
    return grid


def _tc(text, w, bold=False, align="center", size=24, line=240, vmerge=None):
    rpr_parts = [
        f'<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>',
        f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    ]
    if bold:
        rpr_parts.append('<w:b/><w:bCs/>')
    rpr = '<w:rPr>' + ''.join(rpr_parts) + '</w:rPr>'

    ppr_parts = [
        f'<w:spacing w:line="{line}" w:lineRule="auto" w:after="0" w:before="0"/>',
        f'<w:jc w:val="{align}"/>',
        '<w:ind w:firstLine="0" w:left="0"/>',
        rpr
    ]
    ppr = '<w:pPr>' + ''.join(ppr_parts) + '</w:pPr>'

    paragraphs = []
    for line_text in str(text).split('\n'):
        paragraphs.append(f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{esc(line_text)}</w:t></w:r></w:p>')

    tcpr_parts = [f'<w:tcW w:w="{w}" w:type="dxa"/>']
    if vmerge == "restart":
        tcpr_parts.append('<w:vMerge w:val="restart"/>')
    elif vmerge == "continue":
        tcpr_parts.append('<w:vMerge/>')
    tcpr_parts.append('<w:vAlign w:val="center"/>')
    tcpr = '<w:tcPr>' + ''.join(tcpr_parts) + '</w:tcPr>'

    return f'<w:tc>{tcpr}{"".join(paragraphs)}</w:tc>'


def table(headers, rows, col_widths=None, header_size=24, row_size=24, line=240,
          header_align="center", row_aligns=None):
    n = len(headers)
    if col_widths is None:
        col_widths = [9638 // n] * n
    total_width = sum(col_widths)

    out = ['<w:tbl>']
    out.append(_tbl_props(width=total_width))
    out.append(_tbl_grid(col_widths))

    out.append('<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>')
    for h, w in zip(headers, col_widths):
        out.append(_tc(h, w, bold=True, align=header_align, size=header_size, line=line))
    out.append('</w:tr>')

    if row_aligns is None:
        row_aligns = ["left"] + ["left"] * (n - 1)

    for row in rows:
        out.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>')
        for cell, w, align in zip(row, col_widths, row_aligns):
            out.append(_tc(cell, w, bold=False, align=align, size=row_size, line=line))
        out.append('</w:tr>')

    out.append('</w:tbl>')
    out.append(p("", first_line=False, size=2))
    return ''.join(out)


# ============================================================
# Листинг (Courier New, 12pt, одинарный)
# ============================================================

def listing(code, font="Courier New"):
    out = []
    for line in code.split('\n'):
        rpr = (f'<w:rPr><w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
               f'<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>')
        ppr = ('<w:pPr><w:spacing w:line="240" w:lineRule="auto" w:after="0" w:before="0"/>'
               '<w:ind w:firstLine="0" w:left="0"/><w:jc w:val="left"/>'
               + rpr + '</w:pPr>')
        out.append(f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{esc(line)}</w:t></w:r></w:p>')
    return ''.join(out)
