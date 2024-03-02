from data.model.document import Document
from data.model.documentType import DocumentType
from nir.util import NIRUtils
from data.model.article import Article
import xml.etree.ElementTree as ET
from data.static.treeview import TreeView

class NIRParser():


    def parse(type: DocumentType):

        # Create a new document, based on the document type passed by.
        # The articles list is empty now, need to be parsed.
        document = Document(type)

        tree = ET.parse(document.filepath)
        root = tree.getroot()

        # The first type of NIR documents are attachment-oriented, so
        # every article is simply an attachment, every article
        # is made of paragraphs.
        attachments = root.find(TreeView.NODE_A).find(TreeView.NODE_B)


        # Every article needs to be parsed reading every line.
        # The raw content is a list of paragraph i.e. strings.
        articles: dict[str, Article] = {}
        
        for attachment in attachments:

            raw_content = []
            doc = attachment.find(TreeView.NODE_C)

            mainBody = doc.find(TreeView.NODE_D)

            for p in mainBody[0].find(TreeView.NODE_E):
                p_content = ""
                for inner in p.itertext():
                    p_content += inner
                raw_content.append(p_content)

            raw_content = NIRUtils.clean_content(raw_content)

            article = Article.build_from_raw(raw_content)
            articles[article.id] = article

        document.load_articles(articles)
        return document