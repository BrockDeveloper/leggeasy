

class Article():

    def __init__(self, id: str, desc: str, paragraphs: list[str]):

        self.id: str = id
        self.desc: str = desc
        self.paragraphs: list[str] = paragraphs