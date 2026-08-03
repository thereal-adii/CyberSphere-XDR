from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.models import Incident

events = load_events(EVENTS_FILE)

incident = Incident(
    incident_id="INC-0001",
    title="SSH Authentication Activity",
    severity="Medium",
    confidence=0.80,
)

for event in events:
    incident.add_event(event)

print("\nCyberSphere Incident\n")
print(f"Incident ID : {incident.incident_id}")
print(f"Title       : {incident.title}")
print(f"Severity    : {incident.severity}")
print(f"Confidence  : {incident.confidence}")
print(f"Events      : {incident.event_count}")

print("\nIncluded Events:")

for event in incident.events:
    print(f"- {event.event_id}: {event.event_type}")
