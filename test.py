import xml.etree.ElementTree as ET

PREFIX = r"{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}"

tree = ET.parse("assets/cpp.xml")
root = tree.getroot()

chapters = root.find(PREFIX + "act")
chapters = chapters.find(PREFIX + "body")
chapters = chapters.findall(PREFIX + "chapter")

for chapter in chapters:

    articles = chapter.findall(PREFIX + "article")

    for article in articles:

        # print(article.attrib["eId"])

        if article.attrib["eId"] == "art_12":

            paragraphs = article.findall(PREFIX + "paragraph")
            

            for paragraph in paragraphs:

                # arrivati a questo punto, l'articolo potrebbe avere un content,
                # oppure una list, non so se sono esclusivi o può avere entrambi

                content = paragraph.find(PREFIX + "content")
                list = paragraph.find(PREFIX + "list")


                if content:
                    ps = content.findall(PREFIX + "p")
                    
                    for p in ps:
                        for t in p.itertext():
                            # rint(t)p
                            continue
                else:
                    
                    intro = list.find(PREFIX + "intro")
                    p = intro.find(PREFIX + "p")

                    for t in p.itertext():
                        print(t)

                    points = list.findall(PREFIX + "point")

                    for point in points:
                        
                        content = point.find(PREFIX + "content")
                        
                        ps = content.findall(PREFIX + "p")
                        # l'elenco letterato è da costruire
                        for p in ps:
                            for t in p.itertext():
                                print(t)