from lxml import html
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getCupSizes() : # Step 1
    pageLink = "http://www.famousfix.com/list/celebrities-by-bra-cup-size"
    searchLink = "http://www.famousfix.com/list/celebrities-with-bra-cup-size-"
    page = requests.get(pageLink)
    splittedUrls = page.content.split(searchLink)
    celebsCupSizes = set()
    for i in range(1,len(splittedUrls)) :
        cupSize = splittedUrls[i].split("\"",1)[0]
        celebsCupSizes.add(cupSize)
    return list(celebsCupSizes)

def parseNamesByCupsize(cupsizes) :  # Step 2
    browser = webdriver.Chrome('/Users/ahmedabdelmeguid/downloads/chromedriver') # change with your driver
    for cupsize in cupsizes:
        browser.get("http://www.famousfix.com/list/celebrities-with-bra-cup-size-" + cupsize)
        elem = browser.find_element_by_tag_name("body")
        
        celebs = set()
        filename = "celebs_" + cupsize + ".txt"
        f= open(filename,"w+")
        
        while 1:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.02)
            elements = browser.find_elements_by_tag_name("a")
            for element in elements:
                celebUrl = ("%s" % element.get_attribute("href"))
                if "http://www.famousfix.com/topic/" in celebUrl:
                    celebName = celebUrl[31:]
                    if celebName not in celebs:
                        celebs.add(celebName)
                        print(celebName, len(celebs))
                        f.write("%s\n" % celebName)

def parseNamesIntoOneFile(cupSizes): # Step 3
    fullCelebsList = set()
    fullCelebsFile = open("celebs.txt", "w")
    fullCelebsFileNumbered = open("celebs_numbered.txt", "w")
    for cupsize in cupSizes:
        celebsFile = open("celebs_" + cupsize + ".txt", "r")
        celebs = celebsFile.readlines()
        for celeb in celebs:
            if celeb not in fullCelebsList:
                fullCelebsList.add(celeb)
    index = 1
    for celeb in sorted(fullCelebsList):
        fullCelebsFile.write(celeb)
        fullCelebsFileNumbered.write(str(index) + ": " + celeb)
        index += 1
    return sorted(list(fullCelebsList))

#cupsizes = getCupSizes() # Get the list of available cupsizes
#parseNamesByCupsize(cupSizes) # Parse celebrities usernames into files by cupsize
#celebs_names = parseNamesIntoOneFile(cupsizes) # Merge all the celebrities usernames into one file

