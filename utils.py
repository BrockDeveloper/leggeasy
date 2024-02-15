import re
from constants import TRASH_CHARS, TRASH_PATTERNS, ILLEGAL_PARAGRAPHS

class Utils:

    def clean_paragraph(paragraph: str) -> str | None:

        if "---" in paragraph:
            return None
        

        for char in TRASH_CHARS:
            paragraph = paragraph.replace(char[0], char[1])

        for pattern in TRASH_PATTERNS:
            paragraph = re.sub(pattern, "", paragraph)

        paragraph = paragraph.replace("((", "")
        paragraph = paragraph.replace("))", "")

        
        if len(paragraph) == paragraph.count(" "):
            return None
        elif paragraph not in ILLEGAL_PARAGRAPHS:
            return paragraph.strip()
        else:
            return None
