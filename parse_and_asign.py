import bs4

class Parse_and_assign:
    def __init__(self, string):
        self.string = string
        
    def run(self):
        self.create_soup()
        elements = self.get_elements()
        self.assign(elements)
        
    def create_soup(self):
        self.soup = bs4.BeautifulSoup(self.string, features="html.parser")
        
    def get_elements(self):
        div_danger = self.soup.find_all(attrs={"class": "v-event v-event-start v-event-end danger white--text"})
        return div_danger
    
    def assign(self, elements_list):
        cleaned_list = [[]]
        for element in elements_list:
            print(element['data-date'])

with open('testfile.txt', 'r') as tf:
    string_test_file = tf.read()

parsing = Parse_and_assign(string_test_file)
parsing.run()