from collections import defaultdict

from prototype.models import SecurityEvent


class CorrelationEngine:

    def correlate(self, events: list[SecurityEvent]):

        grouped = defaultdict(list)

        for event in events:
            key = (
                event.source_ip,
                event.destination_ip,
                event.username,
            )

            grouped[key].append(event)

        return grouped
