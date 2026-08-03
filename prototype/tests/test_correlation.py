from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.correlation.correlation_engine import CorrelationEngine

events = load_events(EVENTS_FILE)

engine = CorrelationEngine()

groups = engine.correlate(events)

print("\nCyberSphere Correlation Engine\n")

for key, event_list in groups.items():
    print("=" * 60)
    print(f"Source      : {key[0]}")
    print(f"Destination : {key[1]}")
    print(f"Username    : {key[2]}")
    print(f"Events      : {len(event_list)}")

    for event in event_list:
        print(f"  - {event.event_type}")
