import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://laerciosr.github.io/exa844/')

html = str(page.read().decode('utf-8'))

soup = BeautifulSoup(html, 'lxml')

print("Título:", soup.title.string)
for img in soup.find_all('img'):
    print("src: ", img.attrs.get("src"))
    break
