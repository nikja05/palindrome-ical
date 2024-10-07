import bs4
from datetime import datetime, timedelta

class Parse_and_assign:
    def __init__(self, string):
        self.string = string
        
    def run(self):
        self.create_soup()
        elements = self.get_elements()
        event_list_cleaned = self.assign(elements)
        return event_list_cleaned
        
    def create_soup(self):
        self.soup = bs4.BeautifulSoup(self.string, features="html.parser")
        
    def get_elements(self):
        div_danger = self.soup.find_all(attrs={"class": "v-event v-event-start v-event-end danger white--text"})
        return div_danger
    
    def assign(self, elements_list):
        cleaned_list = []
        
        for element in elements_list:
            # take date and time out of bs object
            start_date, end_date = self.combine_date_and_time(element['data-date'], element.span.text[:5])
            # append start and end date, as well as name of event to list
            event_list = [start_date, end_date, element.span.text[6:]]
            cleaned_list.append(event_list)
        
        return cleaned_list
    
    def combine_date_and_time(self, date, time):
        # split up the bs string into valid datetime syntax
        start_date = datetime(int(date[:4]), int(date[5:7]), int(date[8:]), int(time[:2]), int(time[3:]), 00)
        # add 45 minutes to create end_date
        end_date = start_date + timedelta(minutes = 45)
        return start_date, end_date