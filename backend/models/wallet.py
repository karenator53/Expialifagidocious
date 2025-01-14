from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class Transaction(BaseModel):
    hash: str
    timestamp: int
    type: str
    tokenSymbol: str
    amount: float
    price: float

class Wallet(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    address: str
    group: Optional[str] = None
    balance: Optional[float] = None
    currentPrice: Optional[float] = None
    transactions: Optional[List[Transaction]] = None
    lastUpdated: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Main Wallet",
                "address": "0x123...",
                "group": "Personal",
                "balance": 100.5,
                "currentPrice": 1800.00,
                "transactions": [],
                "lastUpdated": 1677649200000
            }
        }