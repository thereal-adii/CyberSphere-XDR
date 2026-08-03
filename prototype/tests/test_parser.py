from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.parser.event_parser import EventParser

events = load_events(EVENTS_FILE)

parser = EventParser()

print("\nCyberSphere XDR Event Parser\n")

for event in events:
    parsed = parser.parse(event)

    print(f"{parsed.event_id} -> {parsed.event_type}")
