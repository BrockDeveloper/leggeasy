
from data.model.article import Article
from data.static.documents import DOCUMENTS
from data.model.documentType import DocumentType


class Document():

    '''
    Define a single NIR document.
    A document is basically a collection of articles.
    '''


    def __init__(self, documentType: DocumentType):

        '''
        Based on the document type, this class loads information
        from the document definition.
        '''
        
        self.__dict__ = DOCUMENTS[documentType.value]

        self.type: DocumentType = documentType
        self.articles: dict[str, Article] = {}
    

    def load_articles(self, articles: dict[str, Article]):

        '''
        Load articles from a given dictionary.
        '''

        self.articles = articles

    
    def get_ids(self) -> list[str]:

        '''
        Get the list of ids, i.e. keys, from articles dictionary.
        '''

        ids_html = ""

        for id in self.articles.keys():
            ids_html = ids_html + '<option value="'+ id + '">' + id + '</option>'

        # return list(self.articles.keys())
        return ids_html


    def get_article_from_id(self, id: str) -> Article:

        '''
        Return the article from the given id.
        Is None if the article doesn't exist.
        '''

        try:
            return self.articles[id]
        except KeyError:
            return None