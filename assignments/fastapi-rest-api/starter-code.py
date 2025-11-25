from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = ""

items: Dict[int, Item] = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, "item": item}

@app.get("/items/")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item
        return {"id": item_id, "item": item}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    return {"error": "Item not found"}
