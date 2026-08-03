from dataclasses import dataclass


@dataclass
class GraphEdge:
    source: str
    target: str
    relationship: str
