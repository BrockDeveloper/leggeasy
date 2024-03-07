import re
from data.static.pattern import TRASH_CHARS, TRASH_PATTERNS, USELESS_BRACKETS
import xml.etree.ElementTree as ET
from data.static.treeview import TreeView

class NIRUtils:        


    def clean_content(raw_content):

        content = []

        for c in raw_content:
            splitted = c.split("\n")
            content = content + splitted

        content = [NIRUtils.clean_paragraph(con) for con in content]
        content = [c for c in content if c is not None if c != '']

        return content


    def clean_paragraph(paragraph: str) -> str:

        for char in TRASH_CHARS:
            paragraph = paragraph.replace(char[0], char[1])

        for pattern in TRASH_PATTERNS:
            paragraph = re.sub(pattern, "", paragraph)

        for bracket in USELESS_BRACKETS:
            paragraph = paragraph.replace(bracket, "")
        
        if len(paragraph) == paragraph.count(" "):
            return None
        else:
            return paragraph.strip()
