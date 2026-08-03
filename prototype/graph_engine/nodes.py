from dataclasses import dataclass


@dataclass
class GraphNode:
    node_id: str
    node_type: str
    label: str
