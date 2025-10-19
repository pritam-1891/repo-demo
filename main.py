from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

@app.get("/")
async def root():
    return {"message": "🚀 FastAPI on Cloud Run - CI/CD test success!! FastAPI on Cloud Run!"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/items")
async def create_item(item: Item):
    return {"created": item}
