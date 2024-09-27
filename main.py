from toiCal import ToiCal

to_iCalendar = ToiCal('Mein Probenplan')

# event_name, description, date_start[], date_end[], place
event_name = 'Franz'
event_description = 'Franz Test xy'
date_start = [2024, 9, 27, 11, 0, 0]
date_end = [2024, 9, 27, 15, 0, 0]
place = 'Zimmer xy'

to_iCalendar.createAndAddEvent(event_name, event_description, date_start, date_end, place)
to_iCalendar.saveEvent()