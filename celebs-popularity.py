import urllib2
from bs4 import BeautifulSoup

def parseFansCount(phrase):
    splits = phrase.split('has ')
    rightSplit = splits[len(splits)-1]
    fans = rightSplit.split(' fan')[0]
    return int(''.join(c for c in fans if c.isnumeric()))

def getCelebrityFans(celeb) :
    quote_page = 'http://www.famousfix.com/topic/' + celeb + '/fans'
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_boxes = soup.findAll('div', attrs={'class': 'pb10'})
    for name_box in name_boxes:
        name = name_box.text.strip()
        if name != '':
            return parseFansCount(name)

def getPopularityData():
    celebsFile = open("celebs.txt", "r")
    celebsList = set()
    celebs = celebsFile.readlines()
    for celeb in celebs:
        if celeb not in celebsList:
            celebsList.add(celeb)
    celebPopularityFile = open("celebs-popularity.txt", "a+")
    popularity = {}
    for celeb in sorted(list(celebsList)):
        celeb_name = celeb.rstrip("\n\r")
        fansCount = getCelebrityFans(celeb_name)
        popularity.update({ celebName : fansCount})
        print(celeb_name + ": " + str(fansCount))
    for name, fans in reversed(sorted(popularity.iteritems(), key=lambda (k,v): (v,k))):
        celebPopularityFile.write(name + ' ' + str(fans) + "\n")
