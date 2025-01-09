from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.wallet import Wallet
from fastapi import Request, Body

router = APIRouter()

@router.get("/wallets", response_model=List[Wallet])
async def get_wallets(request: Request):
    wallets = []
    cursor = request.app.mongodb["wallets"].find()
    async for document in cursor:
        wallets.append(Wallet(**document))
    return wallets

@router.post("/wallets", response_model=Wallet)
async def create_wallet(request: Request, wallet: Wallet):
    wallet_dict = wallet.dict()
    await request.app.mongodb["wallets"].insert_one(wallet_dict)
    return wallet

@router.delete("/wallets/{wallet_id}")
async def delete_wallet(wallet_id: str, request: Request):
    delete_result = await request.app.mongodb["wallets"].delete_one({"id": wallet_id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Wallet not found")