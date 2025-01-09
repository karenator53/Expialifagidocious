from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase
from dotenv import load_dotenv
import os
from routers import wallets

# Load environment variables
load_dotenv()

app = FastAPI(title="Crypto Wallet Tracker API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "wallet_tracker")

@app.on_event("startup")
async def startup_db_client():
    try:
        app.mongodb_client: AgnosticClient = AsyncIOMotorClient(MONGODB_URL)
        app.mongodb: AgnosticDatabase = app.mongodb_client[DB_NAME]
        # Verify the connection
        await app.mongodb_client.admin.command('ping')
        print("Successfully connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e

@app.on_event("shutdown")
async def shutdown_db_client():
    if hasattr(app, 'mongodb_client'):
        app.mongodb_client.close()
        print("MongoDB connection closed")

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# Include routers
app.include_router(wallets.router, prefix="/api")