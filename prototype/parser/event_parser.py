from prototype.models import SecurityEvent


class EventParser:
    """
    Normalizes incoming security events into the
    CyberSphere XDR internal SecurityEvent model.
    """

    def parse(self, event: SecurityEvent) -> SecurityEvent:
        return event
