import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://intern.gymkirchenfeld.ch/myregister'
USERNAME = 'nikolaj.veljkovic@mygymer.ch'
PASSWORD = 'W1rs1ndd0ch4lle'

class GetHtml:
    
    """
    Requests page, fills out Microsoft login
    ---
    
    login()
    fill_field()
    """
    
    def __init__(self, url, username, password):
        self.url = url
        self.uname = username
        self.pwd = password
        
        self.browser = webdriver.Chrome()
        
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
            # buffer because of COMPUTERSTOOFASTTT
            time.sleep(2)
            # wait for element to load
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, element_id)))
            # fill in the field
            field = self.browser.find_element(By.ID, element_id)
            field.send_keys(content)
            field.send_keys(Keys.RETURN)
        except:
            print('Damn. While filling out the login field, something failed. \n Please tell Nikolaj about this.')
    
    def go_to_page(self, page_name):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, page_name)))
        link = self.browser.find_element(By.LINK_TEXT, page_name)
        link.click()
        
getit = GetHtml(URL, USERNAME, PASSWORD)
getit.login()
getit.go_to_page('PROBENPLAN')

# TODO: make exams actually load
# TODO: replace dirty way of pausing with webdriverwait