import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetHtml:
    
    """
    Requests page, fills out Microsoft login
    ---
    
    login()
    fill_field()
    """
    
    def __init__(self, system):
        if system == 'windows':
            self.browser = webdriver.Edge()
        elif system == 'mac':
            self.broser = webdriver.Safari()
        else:
            raise Exception("windows oder mac. sonst geht's nicht.")
    
    def run(self, url, username, password):
        self.url = url
        self.uname = username
        self.pwd = password
        
        self.login()
        self.go_to_page('PROBENPLAN')
        source_of_page = self.get_source('.danger')
        return source_of_page
        
    def login(self):
        self.browser.get(self.url)
        self.fill_field('i0116', self.uname)
        self.fill_field('i0118', self.pwd)
            
    def fill_field(self, element_id, content):
        """
        Can fill out a text field
        ---
        Uses WebDriverWait to wait until element is found
        Pastes content into text element
        "Presses" Enter when finished
        """
        try:
            # buffer because button gets clicked before it shows
            # the div is hidden in the source, webdriverwait doesn't understand
            time.sleep(2)
            # wait for element to load
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, element_id)))
            # fill in the field
            field = self.browser.find_element(By.ID, element_id)
            field.send_keys(content)
            field.send_keys(Keys.RETURN)
        except:
            print('Damn. While filling out the login field, something failed. \n Please tell Nikolaj about this. \n \
            Two possibilites: either something crashed, or you were already logged in and the program should have run smoothly anyways.')
    
    def go_to_page(self, page_name):
        # waits until unique page name appears (probenplan)
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, page_name)))
        link = self.browser.find_element(By.LINK_TEXT, page_name)
        link.click()
        
    def get_source(self, unique_selector):
        # waits until unique event selector appears (only in exam div)
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, unique_selector)))
        return self.browser.page_source

# TODO: replace dirty way of pausing with webdriverwait