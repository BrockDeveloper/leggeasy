from nir.parser import NIRParser
from data.model.documentType import DocumentType


parsed = NIRParser.parse(DocumentType.CODICE_PROCEDURA_PENALE, "100")
print(parsed)