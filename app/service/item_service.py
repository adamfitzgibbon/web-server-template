from app.model.item import Item

items_db = []

def addItem(item: Item):
    items_db.append(item.model_dump())

def getItem(itemId: int) -> dict | None:
    for i in items_db:
        print(i)
        if i["id"] == itemId:
            return i
    return None