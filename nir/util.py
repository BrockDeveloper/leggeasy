import re
from data.static.pattern import TRASH_CHARS, TRASH_PATTERNS, USELESS_BRACKETS
import xml.etree.ElementTree as ET
from data.static.treeview import TreeView

class NIRUtils:


    def get_attachments(filepath):

        tree = ET.parse(filepath)
        root = tree.getroot()

        return root.find(TreeView.NODE_A).find(TreeView.NODE_B)


    def find_article_content(attachments, article):

        raw_content = []
        
        for attachment in attachments:
            
            doc = attachment.find(TreeView.NODE_C)

            if doc.attrib[TreeView.ATTR_A] == article:
                
                mainBody = doc.find(TreeView.NODE_D)

                for p in mainBody[0].find(TreeView.NODE_E):
                    p_content = ""
                    for inner in p.itertext():
                        p_content += inner
                    raw_content.append(p_content)

        return raw_content


    def clean_content(raw_content):

        content = []

        for c in raw_content:
            splitted = c.split("\n")
            content = content + splitted

        content = [NIRUtils.clean_paragraph(con) for con in content]
        content = [c for c in content if c is not None if c != '']

        return content


    def clean_paragraph(paragraph: str) -> str | None:

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