from nir.parser import NIRParser
from data.model.documentType import DocumentType


parsed = NIRParser.parse(DocumentType.CODICE_CIVILE, "999")
print(parsed)