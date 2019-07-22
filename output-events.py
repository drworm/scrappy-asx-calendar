import os
import yaml
from datetime import date
from icalendar import Calendar, Event

with open("data/events.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

cal = Calendar()
cal.add('prodid', '-//investorwag.com//Scrappy ASX Calendar//EN')
cal.add('version', '2.0')
cal.add('calscale', 'GREGORIAN')
cal.add('method', 'PUBLISH')

uid = 0
for json_event in data['events']:
    event = Event()
    event['uid'] = 'scrappy-asx-calendar-%s' % (uid)
    event['summary'] = json_event['summary']
    event['description'] = json_event['description']
    event['transp'] = 'TRANSPARENT' # not seen as busy event

    date_string = json_event['date'].strftime('%Y%m%d')
    event['dtstart'] = date_string

    cal.add_component(event)
    uid += 1

filename = "output/scrappy-asx-fy19-calendar.ics"
os.makedirs(os.path.dirname(filename), exist_ok=True)
f = open(filename, 'wb')
f.write(cal.to_ical())
f.close()
