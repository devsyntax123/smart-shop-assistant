
from typing import TypedDict
from graph.structure import SmartphoneReview
from typing import List, Optional

class State(TypedDict):
    query: str
    email: str
    products: list[dict]
    product_schema: list[SmartphoneReview]
    blogs_content: Optional[List[dict]]
    best_product: dict
    comparison: list
    youtube_link: str
