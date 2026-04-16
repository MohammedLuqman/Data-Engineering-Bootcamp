import asyncio
from fastapi import FastAPI
from app import api 
from app.scraper import scrape_and_store 

app = FastAPI()
app.include_router(api.router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(asyncio.to_thread(scrape_and_store))
