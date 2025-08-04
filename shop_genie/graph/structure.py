from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional

class SpecsComparison(BaseModel):
    processor: str = Field(..., description="Processor type and model, e.g., 'Snapdragon 888'")
    battery: str = Field(..., description="Battery capacity and type, e.g., '4500mAh'")
    camera: str = Field(..., description="Camera specs, e.g., '108MP primary'")
    display: str = Field(..., description="Display type, size, refresh rate, e.g., '6.5 inch OLED, 120Hz'")
    storage: str = Field(..., description="Storage options and expandability, e.g., '128GB, expandable'")

class RatingsComparison(BaseModel):
    overall_rating: float = Field(..., description="Overall rating out of 5, e.g., 4.5")
    performance: float = Field(..., description="Rating for performance out of 5, e.g., 4.7")
    battery_life: float = Field(..., description="Rating for battery life out of 5, e.g., 4.3")
    camera_quality: float = Field(..., description="Rating for camera quality out of 5, e.g., 4.6")
    display_quality: float = Field(..., description="Rating for display quality out of 5, e.g., 4.8")

class Comparison(BaseModel):
    product_name: str = Field(..., description="Name of the product")
    specs_comparison: SpecsComparison
    ratings_comparison: RatingsComparison
    reviews_summary: str = Field(..., description="Summary of key points from user reviews about this product")

class BestProduct(BaseModel):
    product_name: str = Field(..., description="Name of the best product")
    justification: str = Field(..., description="Explanation of why this product is the best choice")

class ProductComparison(BaseModel):
    comparisons: List[Comparison]
    best_product: BestProduct

class Highlights(BaseModel):
    Camera: Optional[str] = None
    Performance: Optional[str] = None
    Display: Optional[str] = None
    Fast_Charging: Optional[str] = None

class SmartphoneReview(BaseModel):
    """A review of a smartphone."""
    title: str = Field(..., description="The title of the product review")
    url: Optional[str] = Field(None, description="The URL of the product review")
    content: Optional[str] = Field(None, description="The main content of the product review")
    pros: Optional[List[str]] = Field(None, description="The pros of the product")
    cons: Optional[List[str]] = Field(None, description="The cons of the product")
    highlights: Optional[dict] = Field(None, description="The highlights of the product")
    score: Optional[float] = Field(None, description="The score of the product")

class ListOfSmartphoneReviews(BaseModel):
    """A list of smartphone reviews."""
    reviews: List[SmartphoneReview] = Field(..., description="List of individual smartphone reviews")

class EmailRecommendation(BaseModel):
    subject: str = Field(..., description="The email subject line, designed to capture the recipient's attention.")
    heading: str = Field(..., description="The main heading of the email, introducing the recommended product.")
    justification_line: str = Field(..., description="A concise explanation of why the product is being recommended.")
