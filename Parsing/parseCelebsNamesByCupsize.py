import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def parseCelebsNamesByCupsize(cupsize) :
    
    browser = webdriver.Chrome('/Users/ahmedabdelmeguid/downloads/chromedriver') # change with your driver
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
