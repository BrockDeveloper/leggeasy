
ILLEGAL_PARAGRAPHS = ["&lt;![CDATA[----------------- ]]&gt;",
                      "&lt;![CDATA[---------------- ]]&gt;"]

TRASH_PATTERNS = [r"\(\(\d+\)\)",
                  r"\(\d+\)",
                  r"\(\d+[a-z]\)",
                  r"\(\)"]

TRASH_CHARS = [["a'","à"],
               ["e'","è"],
               [" e' ","é"],
               ["i'","ì"],
               ["o'","ò"],
               ["u'","ù"],
               ["  "," "],
               [" \n", ""]]

INTRO_PATTERN = r"(Art\.\s+)([0-9]+)"