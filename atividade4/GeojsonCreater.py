import xml.sax
import json


class Listener(xml.sax.ContentHandler):
    def __init__(self, geojson):
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
            point = {
                'type': "Feature",
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(self.nodeLon), float(self.nodeLat)]
                },
                'properties': {
                    'nome': self.nodeName,
                    'tipo': self.nodeType
                }
            }
            geojson["features"].append(point)


parser = xml.sax.make_parser()
geojson = {
    'type': "FeatureCollection",
    'features': []
}

Handler = Listener(geojson)
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("../assets/map.osm")

jsonStr = json.dumps(geojson, indent=2, ensure_ascii=False)
print(jsonStr)

f = open("output.json", "w")
f.write(jsonStr)
f.close()
