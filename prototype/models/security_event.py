from datetime import datetime

from pydantic import BaseModel


class SecurityEvent(BaseModel):
    event_id: str
    timestamp: datetime

    source_ip: str
    destination_ip: str

    hostname: str
    username: str

    event_type: str
    severity: str

    description: str

    mitre_technique: str | None = None
