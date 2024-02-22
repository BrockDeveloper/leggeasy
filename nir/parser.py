from data.model.document import Document
from data.model.documentType import DocumentType
from nir.util import NIRUtils
from data.model.article import Article

class NIRParser():


    def parse(type: DocumentType, article: str):

        document = Document(type)
        article = document.article + article

        attachments = NIRUtils.get_attachments(document.filepath)
        raw_content = NIRUtils.find_article_content(attachments, article)
        
        raw_content = NIRUtils.clean_content(raw_content)

        if raw_content:
            return Article.build_from_raw(raw_content)
        else:
            return "Missing article"