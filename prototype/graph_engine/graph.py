from prototype.graph_engine.nodes import GraphNode
from prototype.graph_engine.edges import GraphEdge


class AttackGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node: GraphNode):
        self.nodes[node.node_id] = node

    def add_edge(self, edge: GraphEdge):
        self.edges.append(edge)

    def summary(self):
        print("\nCyberSphere Attack Graph\n")

        print(f"Nodes : {len(self.nodes)}")
        print(f"Edges : {len(self.edges)}")

        print("\nNode List")

        for node in self.nodes.values():
            print(f"- {node.label} ({node.node_type})")

        print("\nRelationships")

        for edge in self.edges:
            print(
                f"{edge.source} --[{edge.relationship}]--> {edge.target}"
            )
