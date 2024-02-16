from data.model.document import Document
from data.model.documentType import DocumentType
from nir.util import NIRUtils

class NIRParser():


    def parse(type: DocumentType, article: str):

        document = Document(type)
        article = document.article + article

        attachments = NIRUtils.get_attachments(document.filepath)
        raw_content = NIRUtils.find_article_content(attachments, article)
        
        if raw_content:
            return NIRUtils.clean_content(raw_content)
        else:
            return "Missing article"