from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class SimCard(BaseModel):
    sim_number: str
    phone_number: str
    status: bool
    activation_date: Optional[datetime]
    