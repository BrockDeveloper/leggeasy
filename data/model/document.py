from data.static.documents import DOCUMENTS
from data.model.article import Article
from data.model.documentType import DocumentType

class Document():

    def __init__(self, documentType: DocumentType):
        
        self.__dict__ = DOCUMENTS[documentType.value]
        self.type: DocumentType = documentType
        self.articles: dict = {}
    

    def load_articles(self, articles):

        self.articles = articles

    
    def get_article_list(self):

        return list(self.articles.keys())


    def get_article(self, id: str) -> Article:

        try:
            return self.articles[id]
        except KeyError:
            return None