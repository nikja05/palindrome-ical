from icalendar import Calendar, Event, vText
from pathlib import Path
from datetime import datetime
import os

class ToiCal:
    """Creates and adds events to iCal in a concise manner

    Methods
    -------
    __init__(name: str)
        Initiates the object, assigns a calendar name.
    
    createAndAddEvent(event_name: str, description: str, date_start: list, date_end: list, place: str)
        Adds and creates an event with all the most important parameters.
    
    saveEvent()
        Saves the event into an .ics file.
    """
    
    def __init__(self, calendar_name):
        # intitiation of the calendar object
        self.cal = Calendar()
        self.cal_name = calendar_name
        # required properties
        self.cal.add('prodid', f'-//{self.cal_name}//')
        self.cal.add('version', '2.0')
        
    def createAndAddEvent(self, event_name, description, date_start, date_end, place):
        
        event = Event()
        
        event.add('name', event_name)
        event.add('description', description)
                                    # yyyy, mm, dd, hh, mm, ss
        event.add('dtstart', datetime(date_start[0], date_start[1], date_start[2], \
                                      date_start[3], date_start[4], date_start[5], \
                                      tzinfo = pytz.utc))
        event.add('dtend', datetime(date_end[0], date_end[1], date_end[2], \
                                      date_end[3], date_end[4], date_end[5], \
                                      tzinfo = pytz.utc))
                                      # can tzinfo = pytz.utc be left out?
        event['location'] = vText(place)
        
        # add event
        self.cal.add_component(event)
        
    def saveEvent(self):
        
        directory = Path.cwd() / f'{self.cal_name}'
        
        try:
            directory.mkdir(parents = True, exist_ok = False)
        except FileExistsError:
            print("Folder already exists")
        else:
            print("Folder was created")
            
        file = open(os.path.join(directory, f'{self.cal_name}.ics'), 'wb')
        file.write(self.cal.to_ical())
        file.close()

to_iCalendar = ToiCal('Mein Probenplan')

# event_name, description, date_start[], date_end[], place
event_name = 'Franz'
event_description = 'Franz Test xy'
date_start = [2024, 9, 27, 11, 0, 0]
date_end = [2024, 9, 27, 15, 0, 0]
place = 'Zimmer xy'

to_iCalendar.createAndAddEvent
to_iCalendar.saveEvent()

e = open('Mein Probenplan/Mein Probenplan.ics', 'rb')
ecal = Calendar.from_ical(e.read())
for component in ecal.walk():
   print(component.name)
e.close()