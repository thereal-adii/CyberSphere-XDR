from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.correlation.correlation_engine import CorrelationEngine

events = load_events(EVENTS_FILE)

engine = CorrelationEngine()

incidents = engine.correlate(events)

print("\nCyberSphere XDR Correlation Engine\n")

for incident in incidents:
    print("=" * 50)
    print(f"Incident ID : {incident.incident_id}")
    print(f"Title       : {incident.title}")
    print(f"Severity    : {incident.severity}")
    print(f"Confidence  : {incident.confidence}")
    print(f"Events      : {incident.event_count}")

    print("\nIncluded Events:")

    for event in incident.events:
        print(f"  {event.event_id} -> {event.event_type}")

    print()
