from nir.parser import NIRParser
from data.model.documentType import DocumentType
from data.model.document import Document

parsed: Document = NIRParser.parse(DocumentType.CODICE_PENALE)

print(parsed.get_article_list())