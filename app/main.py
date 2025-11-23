from fastapi import FastAPI, HTTPException, status
from .model.item import Item
from .service import item_service

app = FastAPI(title="Interview Server")

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    return item_service.items_db

@app.get("/items/{itemId}")
def get_item(itemId: int):
    item = item_service.getItem(itemId)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@app.post("/items")
def add_item(item: Item):
    item_service.addItem(item)
    return {"message": "Item added", "item": item}