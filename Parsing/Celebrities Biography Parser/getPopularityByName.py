import urllib2
from bs4 import BeautifulSoup

def getFansFromPhrase(phrase):
    splits = phrase.split('has ')
    rightSplit = splits[len(splits)-1]
    fans = rightSplit.split(' fan')[0]
    return int(''.join(c for c in fans if c.isnumeric()))

def getPopularityByName(celeb) :
    quote_page = 'http://www.famousfix.com/topic/' + celeb + '/fans'
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_boxes = soup.findAll('div', attrs={'class': 'pb10'})
    for name_box in name_boxes:
        name = name_box.text.strip()
        if name != '':
            return getFansFromPhrase(name)

celebsFile = open("celebs.txt", "r")
celebsList = set()
celebs = celebsFile.readlines()
for celeb in celebs:
    if celeb not in celebsList:
        celebsList.add(celeb)

celebPopularityFile = open("celebs-popularity.txt", "a+")
celebPopularitySortedFile = open("celebs-popularity-sorted.txt", "a+")

sublist = sorted(list(celebsList))[6025:]
print(sublist)
for celeb in sublist:
    celeb_name = celeb.rstrip("\n\r")
    fansCount = getPopularityByName(celeb_name)
    celebPopularityFile.write(celeb_name + ' ' + str(fansCount) + "\n")
    print(celeb_name + ": " + str(fansCount))
