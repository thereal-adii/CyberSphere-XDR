import json
from pathlib import Path

from prototype.models import SecurityEvent


BASE_DIR = Path(__file__).resolve().parent
EVENTS_FILE = BASE_DIR / "sample_events.json"


def load_events(path: Path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [SecurityEvent(**event) for event in data]


if __name__ == "__main__":
    events = load_events(EVENTS_FILE)

    print("\nCyberSphere XDR Event Collector\n")

    for event in events:
        print("=" * 50)
        print(f"Event ID      : {event.event_id}")
        print(f"Time          : {event.timestamp}")
        print(f"Event Type    : {event.event_type}")
        print(f"Source IP     : {event.source_ip}")
        print(f"Destination IP: {event.destination_ip}")
        print(f"Severity      : {event.severity}")
        print(f"MITRE         : {event.mitre_technique}")
        print(f"Description   : {event.description}")
