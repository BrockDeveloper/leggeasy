

class Article():

    def __init__(self, id: str, desc: str, paragraphs: list[str]):

        self.id: str = id
        self.desc: str = desc
        self.paragraphs: list[str] = paragraphs
    

    def build_from_raw(raw_content: str):

        id = raw_content[0].replace("Art. ", "").replace(".", "")
        desc = raw_content[1].replace("(", "").replace(").", "").replace(")", "")

        return Article(
            id,
            desc,
            raw_content[2:]
        )
    

    def __str__(self):

        string = "Articolo: " + self.id + "\n\r"
        string += self.desc + "\n\r\n\r"

        for paragraph in self.paragraphs:
            string += paragraph + "\n\r"

        return string