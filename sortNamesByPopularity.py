import urllib2
from bs4 import BeautifulSoup

def sortNamesByPopularity() :

    celebPopularitySortedFile = open("celebs-popularity-sorted.txt", "w")
    celebsFile = open("celebs-popularity.txt", "r")
    celebs = celebsFile.readlines()
    celebsList = set()
    popularity = {}
    for celeb in celebs:
        celebName, fans = celeb.split(' ')
        fansCount = int(fans)
        print(celebName, fansCount)
        popularity.update({ celebName : fansCount})
    for name, fans in reversed(sorted(popularity.iteritems(), key=lambda (k,v): (v,k))):
        celebPopularitySortedFile.write(name + ' ' + str(fans) + "\n")


sortNamesByPopularity()
