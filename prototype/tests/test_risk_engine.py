from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.correlation.correlation_engine import CorrelationEngine
from prototype.risk_engine import RiskEngine

events = load_events(EVENTS_FILE)

correlation = CorrelationEngine()
incidents = correlation.correlate(events)

risk_engine = RiskEngine()

print("\nCyberSphere XDR Risk Engine\n")

for incident in incidents:

    risk = risk_engine.calculate(incident)

    print("=" * 50)
    print(f"Incident ID : {incident.incident_id}")
    print(f"Severity    : {incident.severity}")
    print(f"Confidence  : {incident.confidence}")
    print(f"Events      : {incident.event_count}")
    print(f"Risk Score  : {risk['score']}")
    print(f"Risk Level  : {risk['level']}")
    print()
