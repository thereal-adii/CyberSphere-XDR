from fastapi import FastAPI

from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.graph_engine.builder import GraphBuilder
from prototype.correlation.correlation_engine import CorrelationEngine
from prototype.risk_engine import RiskEngine

app = FastAPI(
    title="CyberSphere XDR",
    description="Enterprise Attack Simulation, Detection & Security Research Platform",
    version="0.2.0",
)


@app.get("/")
def root():
    return {
        "project": "CyberSphere XDR",
        "status": "running",
        "version": "0.2.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/graph/summary")
def graph_summary():

    events = load_events(EVENTS_FILE)

    builder = GraphBuilder()

    graph = builder.build(events)

    return {
        "nodes": len(graph.nodes),
        "edges": len(graph.edges),
    }


@app.get("/incidents")
def incidents():

    events = load_events(EVENTS_FILE)

    correlation_engine = CorrelationEngine()

    risk_engine = RiskEngine()

    incidents = correlation_engine.correlate(events)

    response = []

    for incident in incidents:

        risk = risk_engine.calculate(incident)

        response.append(
            {
                "incident_id": incident.incident_id,
                "title": incident.title,
                "severity": incident.severity,
                "confidence": incident.confidence,
                "event_count": incident.event_count,
                "risk_score": risk["score"],
                "risk_level": risk["level"],
                "events": [
                    {
                        "event_id": event.event_id,
                        "event_type": event.event_type,
                        "source_ip": event.source_ip,
                        "destination_ip": event.destination_ip,
                        "mitre_technique": event.mitre_technique
                    }
                    for event in incident.events
                ],
            }
        )

    return response
