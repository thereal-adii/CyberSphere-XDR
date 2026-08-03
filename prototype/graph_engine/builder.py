from prototype.graph_engine.graph import AttackGraph
from prototype.graph_engine.nodes import GraphNode
from prototype.graph_engine.edges import GraphEdge
from prototype.models import SecurityEvent


class GraphBuilder:

    def __init__(self):
        self.graph = AttackGraph()

    def process_event(self, event: SecurityEvent):

        source = GraphNode(
            node_id=event.source_ip,
            node_type="ip_address",
            label=event.source_ip,
        )

        destination = GraphNode(
            node_id=event.destination_ip,
            node_type="host",
            label=event.hostname,
        )

        security_event = GraphNode(
            node_id=event.event_id,
            node_type="security_event",
            label=event.event_type,
        )

        self.graph.add_node(source)
        self.graph.add_node(destination)
        self.graph.add_node(security_event)

        self.graph.add_edge(
            GraphEdge(
                source.node_id,
                security_event.node_id,
                "generated",
            )
        )

        self.graph.add_edge(
            GraphEdge(
                security_event.node_id,
                destination.node_id,
                "targeted",
            )
        )

    def get_graph(self):
        return self.graph
