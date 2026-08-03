from dataclasses import dataclass


@dataclass
class GraphNode:
    """
    Represents an entity in the attack graph.
    """

    node_id: str
    node_type: str
    label: str
