import xml.etree.ElementTree as ET
from utils import Utils

PREFIX = r"{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}"

tree = ET.parse("assets/cc.xml")
root = tree.getroot()  # akomantoso

attachments = root.find(PREFIX + "act").find(PREFIX + "attachments")


trova = "CODICE CIVILE-art. 44"

for attachment in attachments:

    doc = attachment.find(PREFIX + "doc")
    if doc.attrib["name"] == trova:
        
        mainBody = doc.find(PREFIX + "mainBody")

        contenuto = []

        # solo il primo paragrafo contiene l'articolo
        for p in mainBody[0].find(PREFIX + "content"):

            inner: str
            for inner in p.itertext():
                contenuto.append(inner)

contenuto_effettivo = []
c: str
for c in contenuto:
    splitted = c.split(" \n \n")
    contenuto_effettivo = contenuto_effettivo + splitted

# arrivati a questo punto si ha un raw data, grezzo

contenuto_effettivos = [Utils.clean_paragraph(con) for con in contenuto_effettivo]

# attenzione all'intestazione, sti bastardi sbagliano pure quella
print(contenuto_effettivos)