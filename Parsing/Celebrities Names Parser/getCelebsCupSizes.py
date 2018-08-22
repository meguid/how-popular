from lxml import html
import requests

def getCelebsCupSizes() :
    pageLink = "http://www.famousfix.com/list/celebrities-by-bra-cup-size"
    searchLink = "http://www.famousfix.com/list/celebrities-with-bra-cup-size-"
    page = requests.get(pageLink)
    splittedUrls = page.content.split(searchLink)
    celebsCupSizes = set()
    for i in range(1,len(splittedUrls)) :
        cupSize = splittedUrls[i].split("\"",1)[0]
        celebsCupSizes.add(cupSize)
    return list(celebsCupSizes)

print(getCelebsCupSizes())
