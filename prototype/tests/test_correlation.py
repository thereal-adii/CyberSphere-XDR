from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.correlation.correlation_engine import CorrelationEngine


def test_correlation():
    events = load_events(EVENTS_FILE)

    engine = CorrelationEngine()
    incidents = engine.correlate(events)

    assert len(incidents) == 1
    assert incidents[0].incident_id == "INC-0001"
    assert incidents[0].event_count == 2
