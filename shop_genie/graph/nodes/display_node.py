from graph.state import State
from logger import logger

def display_node(state: State):
  if "comparison" in state and state['comparison']:


      return {
        "products": state["product_schema"],
        "best_product": state["best_product"],
        "comparison": state["comparison"],
        "youtube_link": state["youtube_link"]
    }
  else:
    logger.info("comparison not available")
