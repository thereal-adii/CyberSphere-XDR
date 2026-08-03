from prototype.graph_engine.graph import AttackGraph
from prototype.graph_engine.nodes import GraphNode
from prototype.graph_engine.edges import GraphEdge
from prototype.models import SecurityEvent


class GraphBuilder:

    def build(self, events: list[SecurityEvent]):

        graph = AttackGraph()

        for event in events:

            source = GraphNode(
                node_id=event.source_ip,
                node_type="IP",
                label=event.source_ip,
            )

            destination = GraphNode(
                node_id=event.destination_ip,
                node_type="Host",
                label=event.destination_ip,
            )

            event_node = GraphNode(
                node_id=event.event_id,
                node_type="Event",
                label=event.event_type,
            )

            graph.add_node(source)
            graph.add_node(destination)
            graph.add_node(event_node)

            graph.add_edge(
                GraphEdge(
                    source.source_id if False else source.node_id,
                    event_node.node_id,
                    "generated",
                )
            )

            graph.add_edge(
                GraphEdge(
                    event_node.node_id,
                    destination.node_id,
                    "targeted",
                )
            )

        return graph
