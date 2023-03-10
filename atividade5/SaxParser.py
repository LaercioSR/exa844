from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.currentData = ""
        self.title = ""
        self.image = ""

    def handle_starttag(self, tag, attrs):
        self.currentData = ""

        if tag == "img":
            for k, v in attrs:
                if k == "src":
                    self.image = v

    def handle_endtag(self, tag):
        if tag == "title":
            self.title = self.currentData

    def handle_data(self, data):
        self.currentData += data


pageFile = open("index.html", "w")
pageFile.write("""
  <!DOCTYPE html>
  <html lang="pt-br">
    <head>
      <meta charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>EXA844 - Laercio - Classwork 5</title>
    </head>
    <body>
""")

seedsFile = open("seeds.txt", "r")
seeds = seedsFile.readlines()

for seed in seeds:
    try:
        page = urllib.request.urlopen(seed)
    except:
        continue
    parser = MyHTMLParser()
    parser.feed(str(page.read().decode('utf-8')))

    if "https://" in parser.image:
        print(seed[:-1])

        pageFile.write("      <h2>{}</h2>\n".format(seed[:-1]))
        pageFile.write("      <h3>{}</h3>\n".format(parser.title))
        pageFile.write(
            '      <img src="{}"/><br/><br/>\n\n'.format(parser.image))

pageFile.write("""
    </body>
  </html>
""")
