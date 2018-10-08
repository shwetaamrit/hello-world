from lxml import html
import requests
page = requests.get('https://www.imdb.com/title/tt7638344/')
tree = html.fromstring(page.content)

character1 = tree.xpath('//td[@class="character"]/a/text()')
character2 = tree.xpath('//td[@class="character"]/text()')

character1.extend(character2)
cast = tree.xpath('//tr[@class="odd" or @class="even"]/td[2]/a/text()')
character1.insert(0, "CHARACTER NAME")
cast.insert(0, "CAST NAME")

cstr = "DHARAK MOVIE"
print ("\n")
print (cstr.center(60, "#"))


i=0
for cast1 in cast:
    print(character1[3])
    print(str(cast1).strip()+ "     " + str(character1[i]).strip())
    i = i + 1
