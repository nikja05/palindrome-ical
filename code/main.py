from setup import Setup
setup = Setup()
setup.install_packages()

from toiCal import ToiCal
from getHtml import GetHtml
from parse_and_assign import Parse_and_assign as paa

URL = 'https://intern.gymkirchenfeld.ch/myregister'
USERNAME = input('Deine mygymer E-Mail Adresse: ').strip()
PASSWORD = input('Das Passwort dazu: ').strip()
SYSTEM = input('Brauchst du MAC oder Windows? ').strip().lower()

get_HTML = GetHtml(SYSTEM)
HTML_source = get_HTML.run(URL, USERNAME, PASSWORD)

p_a_a = paa(HTML_source)
events_list = p_a_a.run()

to_iCalendar = ToiCal('Mein Probenplan')

for event_list in events_list:
    date_start = event_list[0]
    date_end = event_list[1]
    event_name = event_list[2]
    event_description = event_list[2]

    to_iCalendar.createAndAddEvent(event_name, event_description, date_start, date_end)
    to_iCalendar.saveEvent()