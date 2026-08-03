from prototype.collector.collector import EVENTS_FILE, load_events
from prototype.graph_engine.builder import GraphBuilder

events = load_events(EVENTS_FILE)

builder = GraphBuilder()

for event in events:
    builder.process_event(event)

graph = builder.get_graph()

graph.summary()
