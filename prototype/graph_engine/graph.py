import networkx as nx

from .nodes import GraphNode
from .edges import GraphEdge


class AttackGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node: GraphNode):
        self.graph.add_node(
            node.node_id,
            type=node.node_type,
            label=node.label,
        )

    def add_edge(self, edge: GraphEdge):
        self.graph.add_edge(
            edge.source,
            edge.target,
            relationship=edge.relationship,
        )

    def summary(self):
        print("\nCyberSphere Attack Graph\n")

        print(f"Nodes : {self.graph.number_of_nodes()}")
        print(f"Edges : {self.graph.number_of_edges()}")

        print("\nNode List")

        for node, data in self.graph.nodes(data=True):
            print(f"- {node} ({data['type']})")

        print("\nRelationships")

        for source, target, data in self.graph.edges(data=True):
            print(f"{source} --[{data['relationship']}]--> {target}")
