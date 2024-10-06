from toiCal import ToiCal
from getHtml import GetHtml
from setup import Setup
from parse_and_asign import Parse_and_asign as paa

setup = Setup()
#setup.install_packages()

to_iCalendar = ToiCal('Mein Probenplan')
get_HTML = GetHtml()
p_a_a = paa()

URL = 'https://intern.gymkirchenfeld.ch/myregister'
USERNAME = 'nikolaj.veljkovic@mygymer.ch'
PASSWORD = 'W1rs1ndd0ch4lle'

HTML_source = get_HTML.run(URL, USERNAME, PASSWORD)

with open('testfile.txt', 'w') as tf:
    tf.write(HTML_source)

"""
# event_name, description, date_start[], date_end[], place
event_name = 'Franz'
event_description = 'Franz Test xy'
date_start = [2024, 10, 06, 11, 0, 0]
date_end = [2024, 10, 06, 15, 0, 0]
place = 'Zimmer xy'

to_iCalendar.createAndAddEvent(event_name, event_description, date_start, date_end, place)
to_iCalendar.saveEvent()
"""