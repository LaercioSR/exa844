import xml.sax
import time


class Listener(xml.sax.ContentHandler):
    def __init__(self):
        self.nodeName = ""
        self.nodeType = None
        self.nodeLat = ""
        self.nodeLon = ""

    def startElement(self, tag, attributes):
        if tag == "node":
            self.nodeName = ""
            self.nodeType = None
            self.nodeLat = attributes.get("lat")
            self.nodeLon = attributes.get("lon")
        if tag == "tag":
            if attributes.get("k") == "amenity":
                self.nodeType = attributes.get("v")
            elif attributes.get("k") == "name":
                self.nodeName = attributes.get("v")

    def endElement(self, tag):
        if tag == "node" and self.nodeType:
            print("Nome:", self.nodeName)
            print("Tipo:", self.nodeType)
            print("Latitude:", self.nodeLat)
            print("Longitude:", self.nodeLon)
            print("\n")


start = time.time()
parser = xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")

end = time.time()
print(end - start, "s")
