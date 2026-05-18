"""Главная сборка дипломной работы."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from docx_build import build_docx, SECT_PR_FIRST
from content_intro import title_page, toc, introduction
from content_ch1 import chapter1
from content_ch2 import chapter2
from content_ch3 import chapter3
from content_ch4 import chapter4
from content_outro import conclusion, references, appendix_a, appendix_b


def main():
    print("Building diploma...")

    # Собираем body документа
    parts = []
    parts.append(title_page())
    parts.append(toc())
    # Вставляем разделительный sectPr — заканчивается первая секция (титул + содержание),
    # с пустым footer (rId5). Дальше начинается секция с нумерацией страниц (rId6, footer2).
    parts.append(SECT_PR_FIRST)
    parts.append(introduction())
    parts.append(chapter1())
    parts.append(chapter2())
    parts.append(chapter3())
    parts.append(chapter4())
    parts.append(conclusion())
    parts.append(references())
    parts.append(appendix_a())
    parts.append(appendix_b())

    body = ''.join(parts)
    print(f"Total body XML size: {len(body)} bytes")

    out_path = '/projects/sandbox/tes/Соловьёв_Диплом.docx'
    build_docx(out_path, body)
    print(f"Done: {out_path}")


if __name__ == "__main__":
    main()
