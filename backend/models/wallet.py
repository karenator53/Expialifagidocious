from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import uuid4

class Wallet(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    address: str
    chain: str
    balance: str
    group_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)