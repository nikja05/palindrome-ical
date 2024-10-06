from icalendar import Calendar, Event
from pathlib import Path
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
        
    def createAndAddEvent(self, event_name, description, date_start, date_end):
        
        event = Event()
        
        event.add('summary', event_name)
        event.add('description', description)
        event.add('dtstart', date_start)
        event.add('dtend', date_end)
        
        # add event
        self.cal.add_component(event)
        
    def saveEvent(self):
        
        directory = Path.cwd() / f'{self.cal_name}'
        
        try:
            directory.mkdir(parents = True, exist_ok = False)
        except FileExistsError:
            print("All done.")
        else:
            print("New folder created, all done.")
            
        file = open(os.path.join(directory, f'{self.cal_name}.ics'), 'wb')
        file.write(self.cal.to_ical())
        file.close()
