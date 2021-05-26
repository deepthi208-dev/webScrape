from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

class searchGoogle():

    def _init_(self):
        self.searchStr = 'duck'
        self.url = "http://www.google.com"
        self.xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        self.driver = webdriver.Firefox()
        self.logger = logging.getLogger('search')

    def searchstring(self):
        self.driver.get(self.url)
        input_box = self.driver.find_element_by_xpath(self.xpath)
        input_box.send_keys(self.searchStr)
        input_box.send_keys(Keys.RETURN)

    def getLinksWithDuck(self):
        try:
            self.searchstring()
            links = self.driver.find_elements_by_tag_name('h3')
            for link in links:
                rsp = re.search(r'duck', str(link.text))
                if rsp:
                   self.logger.info(link.text)
        except Exception as error:
            self.logger.error('error occured:{0}'.format(error))
            self.closeDriver()

    def searchPageText(self):
        self.searchstring()
        count = 0
        time.sleep(2)
        el = self.driver.find_element_by_tag_name("body")
        lines = el.text.splitlines()
        for line in lines:
            if 'duck' in line:
                count += 1
        self.logger.info('total no. of duck string found:{0}'.format(count))

    def closeDriver(self):
        self.driver.close()


if __name__ == '__main__':
    search = searchGoogle()
    # search.getLinksWithDuck()
    search.searchPageText()
    search.closeDriver()