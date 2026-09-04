from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.graph_engine.builder import GraphBuilder


def test_graph_builder():
    events = load_events(EVENTS_FILE)

    builder = GraphBuilder()
    graph = builder.build(events)

    assert len(graph.nodes) == 4
    assert len(graph.edges) == 4
