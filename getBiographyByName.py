from lxml import html
import requests

def getBiographyByName(celeb) :
    print(celeb)
    page = requests.get('http://www.famousfix.com/topic/' + celeb + '/wiki')
    splitedWithATag = page.content.split("<a")
    removedTagA = ""
    for i in range(0,len(splitedWithATag)) :
        if i==0 :
            removedTagA += splitedWithATag[i]
        else :
            removedTagA += splitedWithATag[i].split(">",1)[1]

    categories = removedTagA.split("<div class=\"w33pc posl\">")
    for i in range(0,len(categories)) :
#        if i!=0 :
        categories[i] = "<div class=\"w33pc posl\">" + categories[i]
    del categories[0]

    biography = {}
    for category in categories :
        tree = html.fromstring(category)
        biography.update({tree.xpath('//div[@class="w33pc posl"]/text()')[0] : tree.xpath('//div[@class="w60pc posr"]/text()')})
    return biography

celebsFile = open("celebs.txt", "r")
celebsBiographyFile = open("celebs-biography.txt", "w")
celebsList = set()
celebs = celebsFile.readlines()
for celeb in celebs:
    if celeb not in celebsList:
        celebsList.add(celeb)

for celeb in sorted(list(celebsList)):
    celeb_name = celeb.rstrip("\n\r")
    celebsBiographyFile.write("$$$ " + celeb_name + "\n")
    biography = getBiographyByName(celeb_name)
    for key, value in sorted(biography.iteritems(), key=lambda (k,v): (v,k)):
        celebsBiographyFile.write(key + ' $ ')
        celebsBiographyFile.write(str(value) + ' ')
        celebsBiographyFile.write("\n")
    celebsBiographyFile.write("\n")

