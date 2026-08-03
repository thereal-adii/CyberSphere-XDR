from dataclasses import dataclass


@dataclass
class GraphEdge:
    """
    Represents a relationship between two graph nodes.
    """

    source: str
    target: str
    relationship: str
