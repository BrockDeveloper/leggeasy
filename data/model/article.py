
import re
import json


class Article():

    '''
    Define a single article of a document. Every article must have an
    identifiers, possibly a description, and a content i.e. a collection
    of paragraphs.
    '''


    def __init__(self, id: str, desc: str, paragraphs: list[str]):

        self.id: str = id
        self.desc: str = desc
        self.paragraphs: list[str] = paragraphs
    

    def build_from_raw(raw_content: str):

        '''
        Build an article from a raw content, parsed from a NIR document.
        '''

        id = raw_content[0].replace("Art. ", "").replace(".", "")
        
        desc = raw_content[1].replace("(", "").replace(").", "").replace(")", "")

        if not raw_content[-1].endswith("."):
            raw_content[-1] = raw_content[-1] + "."

        article = Article(id, desc, raw_content[2:])
        article.bullet()
        return article
    

    def bullet(self):

        normalized_paragraphs = []
        reg = "^^(?:\d+|[a-z])\).*"

        bullets = None
        for p in self.paragraphs:

            if re.search(reg, p):

                if bullets is None:
                    bullets = [p]
                else:
                    bullets.append(p)  
            else:

                if bullets is None:
                    normalized_paragraphs.append(p)
                else:
                    normalized_paragraphs.append(bullets)
                    normalized_paragraphs.append(p)
                    bullets = None
        
        self.paragraphs = normalized_paragraphs
    

    def json(self):

        '''
        Return the article in json format.
        '''

        html = "<b>Articolo " + self.id + "</b><br>"
        html = html + "<i>" +  self.desc + "</i><br><br>"

        for p in self.paragraphs:

            if isinstance(p, list):

                ul = "<ul>"

                for subp in p:
                    ul = ul + "<li>" + subp + "</li>"

                ul = ul + "</ul>"

                html = html + ul

            else:
                html = html + "<p>" + p + "</p>"

        print(html)
        return html

        # return self.__dict__