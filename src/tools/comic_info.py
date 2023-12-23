import os
import re
from xml.etree.cElementTree import Element, SubElement, ElementTree

meta_path = "downloads/meta"

def valid_name(s: str) -> str:
    s = s.strip()
    s = re.sub(r'[\\/:*?"<>|\r\n]', '', s)
    s = s.strip('.')
    s = s.strip()
    return s

def print_book(info):
    # print(info.title)
    # print(info.author)
    # print(info.chineseTeam)
    # print(info.description)
    # print(info.categories)
    # print(info.tags)
    # print(info.eps)
    # print(info.epsDict)

    comic_info = Element("ComicInfo")

    title = SubElement(comic_info, "Title")

    series = SubElement(comic_info, "Series")
    series.text = valid_name(info.title)

    number = SubElement(comic_info, "Number")

    writer = SubElement(comic_info, "Writer")
    writer.text = info.author

    translator = SubElement(comic_info, "Translator")
    translator.text = info.chineseTeam

    languageISO = SubElement(comic_info, "LanguageISO")
    languageISO.text = "zh"

    summary = SubElement(comic_info, "Summary")
    summary.text = info.description

    genre = SubElement(comic_info, "Genre")
    genre.text = ",".join(info.categories)

    tags = SubElement(comic_info, "Tags")
    tags.text = ",".join(info.tags)

    age_rating = SubElement(comic_info, "AgeRating")
    age_rating.text = "R18+"

    for (i, eps) in info.epsDict.items():
        title.text = valid_name(eps.title)
        number.text = str(i)
        tree = ElementTree(comic_info)
        try:
            dir = os.path.join(meta_path, series.text, title.text)
            if not os.path.exists(dir):
                os.makedirs(dir)
            tree.write(os.path.join(dir, "ComicInfo.xml"), encoding="utf-8", xml_declaration=True)
        except Exception as e:
            print(e)

