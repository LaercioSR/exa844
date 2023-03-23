from xml.dom.minidom import parse
import time

start = time.time()
osmDocument = parse('../assets/map.osm')

print("Starting DOM Parser...")
for node in osmDocument.getElementsByTagName("node"):
    typeNode = None
    nameNode = ""
    for tag in node.getElementsByTagName("tag"):
        if tag.getAttribute("k") == "amenity":
            typeNode = tag.getAttribute("v")
        elif tag.getAttribute("k") == "name":
            nameNode = tag.getAttribute("v")

    if typeNode:
        print("Nome:", nameNode)
        print("Tipo:", typeNode)
        print("Latitude:", node.getAttribute("lat"))
        print("Longitude:", node.getAttribute("lon"))
        print("\n")

end = time.time()
print(end - start, "s")
