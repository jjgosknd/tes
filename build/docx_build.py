"""Сборка финального .docx через zipfile + XML."""
import os
import zipfile
import shutil


# ---------- Вспомогательные XML-документы -------------

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Default Extension="png" ContentType="image/png"/>
<Default Extension="jpeg" ContentType="image/jpeg"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
<Override PartName="/word/fontTable.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"/>
<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
<Override PartName="/word/footer2.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''


ROOT_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''


DOCUMENT_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable" Target="fontTable.xml"/>
<Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
<Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer2.xml"/>
</Relationships>'''


CORE_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:dcterms="http://purl.org/dc/terms/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:creator>Соловьёв Г.А.</dc:creator>
<dc:title>Дипломная работа: Разработка мобильного приложения для прохождения онлайн курсов</dc:title>
<dcterms:created xsi:type="dcterms:W3CDTF">2026-05-01T00:00:00Z</dcterms:created>
<dcterms:modified xsi:type="dcterms:W3CDTF">2026-05-18T00:00:00Z</dcterms:modified>
</cp:coreProperties>'''


APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>Kiro</Application>
</Properties>'''


SETTINGS_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:defaultTabStop w:val="720"/>
<w:characterSpacingControl w:val="doNotCompress"/>
<w:compat>
<w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/>
</w:compat>
</w:settings>'''


FONT_TABLE = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:fonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:font w:name="Times New Roman"><w:panose1 w:val="02020603050405020304"/><w:charset w:val="CC"/><w:family w:val="roman"/><w:pitch w:val="variable"/></w:font>
<w:font w:name="Courier New"><w:panose1 w:val="02070309020205020404"/><w:charset w:val="CC"/><w:family w:val="modern"/><w:pitch w:val="fixed"/></w:font>
<w:font w:name="Symbol"><w:panose1 w:val="05050102010706020507"/><w:charset w:val="02"/><w:family w:val="roman"/><w:pitch w:val="variable"/></w:font>
</w:fonts>'''


# Стили: задаём Heading1 (TNR 14, заглавные, центр, чёрный, bold)
# и Heading2 (TNR 14, по ширине, чёрный, bold).
STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults>
<w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman"/>
<w:sz w:val="28"/><w:szCs w:val="28"/>
<w:lang w:val="ru-RU" w:eastAsia="ru-RU" w:bidi="ar-SA"/>
</w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr>
<w:spacing w:line="360" w:lineRule="auto" w:after="0" w:before="0"/>
<w:jc w:val="both"/>
</w:pPr></w:pPrDefault>
</w:docDefaults>

<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
<w:name w:val="Normal"/>
<w:qFormat/>
<w:pPr>
<w:spacing w:line="360" w:lineRule="auto" w:after="0" w:before="0"/>
<w:ind w:firstLine="709"/>
<w:jc w:val="both"/>
</w:pPr>
<w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
<w:sz w:val="28"/><w:szCs w:val="28"/>
</w:rPr>
</w:style>

<w:style w:type="paragraph" w:styleId="Heading1">
<w:name w:val="heading 1"/>
<w:basedOn w:val="Normal"/>
<w:next w:val="Normal"/>
<w:link w:val="Heading1Char"/>
<w:uiPriority w:val="9"/>
<w:qFormat/>
<w:pPr>
<w:keepNext/><w:keepLines/>
<w:pageBreakBefore/>
<w:spacing w:line="360" w:lineRule="auto" w:after="240" w:before="0"/>
<w:ind w:firstLine="0"/>
<w:jc w:val="center"/>
<w:outlineLvl w:val="0"/>
</w:pPr>
<w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
<w:b/><w:bCs/>
<w:caps/>
<w:sz w:val="28"/><w:szCs w:val="28"/>
</w:rPr>
</w:style>

<w:style w:type="paragraph" w:styleId="Heading2">
<w:name w:val="heading 2"/>
<w:basedOn w:val="Normal"/>
<w:next w:val="Normal"/>
<w:link w:val="Heading2Char"/>
<w:uiPriority w:val="9"/>
<w:qFormat/>
<w:pPr>
<w:keepNext/><w:keepLines/>
<w:spacing w:line="360" w:lineRule="auto" w:after="120" w:before="240"/>
<w:ind w:firstLine="709"/>
<w:jc w:val="both"/>
<w:outlineLvl w:val="1"/>
</w:pPr>
<w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
<w:b/><w:bCs/>
<w:sz w:val="28"/><w:szCs w:val="28"/>
</w:rPr>
</w:style>

<w:style w:type="character" w:customStyle="1" w:styleId="Heading1Char">
<w:name w:val="Heading 1 Char"/>
<w:basedOn w:val="DefaultParagraphFont"/>
<w:link w:val="Heading1"/>
<w:uiPriority w:val="9"/>
<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:b/><w:bCs/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
</w:style>

<w:style w:type="character" w:customStyle="1" w:styleId="Heading2Char">
<w:name w:val="Heading 2 Char"/>
<w:basedOn w:val="DefaultParagraphFont"/>
<w:link w:val="Heading2"/>
<w:uiPriority w:val="9"/>
<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:b/><w:bCs/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
</w:style>

<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont">
<w:name w:val="Default Paragraph Font"/>
<w:uiPriority w:val="1"/>
<w:semiHidden/><w:unhideWhenUsed/>
</w:style>

<w:style w:type="table" w:default="1" w:styleId="TableNormal">
<w:name w:val="Normal Table"/>
<w:uiPriority w:val="99"/>
<w:semiHidden/><w:unhideWhenUsed/>
<w:tblPr>
<w:tblInd w:w="0" w:type="dxa"/>
<w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar>
</w:tblPr>
</w:style>

<w:style w:type="numbering" w:default="1" w:styleId="NoList">
<w:name w:val="No List"/>
<w:uiPriority w:val="99"/>
<w:semiHidden/><w:unhideWhenUsed/>
</w:style>

<w:style w:type="paragraph" w:styleId="TOC1">
<w:name w:val="toc 1"/>
<w:basedOn w:val="Normal"/>
<w:next w:val="Normal"/>
<w:autoRedefine/>
<w:uiPriority w:val="39"/>
<w:unhideWhenUsed/>
<w:pPr>
<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9628"/></w:tabs>
<w:spacing w:line="360" w:lineRule="auto"/>
<w:ind w:firstLine="0"/>
</w:pPr>
</w:style>

<w:style w:type="paragraph" w:styleId="TOC2">
<w:name w:val="toc 2"/>
<w:basedOn w:val="Normal"/>
<w:next w:val="Normal"/>
<w:autoRedefine/>
<w:uiPriority w:val="39"/>
<w:unhideWhenUsed/>
<w:pPr>
<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9628"/></w:tabs>
<w:spacing w:line="360" w:lineRule="auto"/>
<w:ind w:left="240" w:firstLine="0"/>
</w:pPr>
</w:style>
</w:styles>'''


# Минимальная нумерация (на всякий случай для списков)
NUMBERING = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:abstractNum w:abstractNumId="0">
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="-"/>
<w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr></w:lvl>
</w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>'''


# Footer1 - пустой (для титульного листа и содержания)
FOOTER1 = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:p>
<w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/></w:rPr></w:pPr>
</w:p>
</w:ftr>'''

# Footer2 - с автоматической нумерацией страниц (с введения и далее)
FOOTER2 = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:p>
<w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/></w:rPr></w:pPr>
<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>
<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/></w:rPr><w:instrText xml:space="preserve">PAGE</w:instrText></w:r>
<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>
</w:p>
</w:ftr>'''


# Документ — оборачиваем body. sectPr задаёт поля A4 + footer.
def document_xml(body_xml):
    """Поля по ГОСТ: верх 20мм, низ 20мм, левое 30мм, правое 15мм
    1 cm = 567 dxa.
    Финальная секция документа (последняя в body): footer с PAGE.
    Нумерация страниц начинается с 3 (титул и содержание не нумеруются).
    """
    section = (
        '<w:sectPr>'
        '<w:footerReference w:type="default" r:id="rId6"/>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" '
        '         w:header="708" w:footer="708" w:gutter="0"/>'
        '<w:pgNumType w:start="3"/>'
        '<w:cols w:space="708"/>'
        '<w:docGrid w:linePitch="360"/>'
        '</w:sectPr>'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:document '
        'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" '
        'xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" '
        'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
        'xmlns:v="urn:schemas-microsoft-com:vml" '
        'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
        'mc:Ignorable="w14 wp14">'
        '<w:body>'
        + body_xml +
        section +
        '</w:body>'
        '</w:document>'
    )


# Section break, который меняет секцию (для размещения после содержания):
# вставляется как параграф с pPr включающим sectPr (предыдущей секции).
SECT_PR_FIRST = (
    '<w:p><w:pPr><w:sectPr>'
    '<w:footerReference w:type="default" r:id="rId5"/>'
    '<w:pgSz w:w="11906" w:h="16838"/>'
    '<w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" '
    '         w:header="708" w:footer="708" w:gutter="0"/>'
    '<w:cols w:space="708"/>'
    '<w:docGrid w:linePitch="360"/>'
    '<w:titlePg/>'
    '</w:sectPr></w:pPr></w:p>'
)


def build_docx(out_path, body_xml):
    if os.path.exists(out_path):
        os.remove(out_path)
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', CONTENT_TYPES)
        z.writestr('_rels/.rels', ROOT_RELS)
        z.writestr('word/_rels/document.xml.rels', DOCUMENT_RELS)
        z.writestr('word/document.xml', document_xml(body_xml))
        z.writestr('word/styles.xml', STYLES)
        z.writestr('word/numbering.xml', NUMBERING)
        z.writestr('word/settings.xml', SETTINGS_XML)
        z.writestr('word/fontTable.xml', FONT_TABLE)
        z.writestr('word/footer1.xml', FOOTER1)
        z.writestr('word/footer2.xml', FOOTER2)
        z.writestr('docProps/core.xml', CORE_XML)
        z.writestr('docProps/app.xml', APP_XML)
    print(f"Wrote {out_path} ({os.path.getsize(out_path)} bytes)")
