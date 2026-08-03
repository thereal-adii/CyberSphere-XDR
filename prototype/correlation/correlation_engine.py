from collections import defaultdict

from prototype.models import Incident, SecurityEvent


class CorrelationEngine:

    def correlate(self, events: list[SecurityEvent]):

        grouped = defaultdict(list)

        # Group events by source, destination and username
        for event in events:
            key = (
                event.source_ip,
                event.destination_ip,
                event.username,
            )

            grouped[key].append(event)

        incidents = []

        for index, (_, correlated_events) in enumerate(grouped.items(), start=1):

            severity = "Medium"

            if len(correlated_events) >= 3:
                severity = "High"

            incident = Incident(
                incident_id=f"INC-{index:04d}",
                title="Correlated Security Activity",
                severity=severity,
                confidence=0.80,
            )

            for event in correlated_events:
                incident.add_event(event)

            incidents.append(incident)

        return incidents
