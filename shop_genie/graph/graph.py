from langgraph.graph import StateGraph, START, END
from graph.state import State
from graph.nodes.display_node import display_node
from graph.nodes.product_comparison_node import product_comparison_node
from graph.nodes.schema_mapping_node import schema_mapping_node
from graph.nodes.tavily_search_node import tavily_search_node
from graph.nodes.youtube_review_node import youtube_review_node
from graph.nodes.send_email_node import send_email_node 
from IPython.display import Image, display

# Build the LangGraph
builder = StateGraph(State)
builder.add_node("tavily_search", tavily_search_node)
builder.add_node("schema_mapping", schema_mapping_node)
builder.add_node("product_comparison", product_comparison_node)
builder.add_node("youtube_review", youtube_review_node)
builder.add_node("display", display_node)
builder.add_node("send_email", send_email_node)
# Define edges to control flow between nodes
builder.add_edge(START, "tavily_search")
builder.add_edge("tavily_search", "schema_mapping")
builder.add_edge("schema_mapping", "product_comparison")
builder.add_edge("product_comparison", "youtube_review")
builder.add_edge("youtube_review", "display")
builder.add_edge("display", END)
builder.add_edge("youtube_review","send_email")
builder.add_edge("send_email",END)
     
graph = builder.compile()
graph.get_graph().draw_mermaid_png(output_file_path="graph.png")