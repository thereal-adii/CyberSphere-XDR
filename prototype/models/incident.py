from dataclasses import dataclass, field
from typing import List

from prototype.models.security_event import SecurityEvent


@dataclass
class Incident:
    """
    Represents a correlated security incident.
    """

    incident_id: str
    title: str
    severity: str
    confidence: float

    events: List[SecurityEvent] = field(default_factory=list)

    def add_event(self, event: SecurityEvent):
        self.events.append(event)

    @property
    def event_count(self):
        return len(self.events)
