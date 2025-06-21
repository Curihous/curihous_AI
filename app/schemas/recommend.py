from pydantic import BaseModel
from typing import Dict

class RecommendRequest(BaseModel):
    user_id: int
    portfolio: Dict[str, float]
    risk_profile: int

class RecommendResponse(BaseModel):
    stock: str
    action: str
    weight: str