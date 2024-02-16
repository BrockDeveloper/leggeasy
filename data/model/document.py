from data.static.documents import DOCUMENTS
from data.model.documentType import DocumentType

class Document():

    def __init__(self, type: DocumentType):

        self.__dict__ = DOCUMENTS[type.value]