from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.98,
        "brand": "Regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of item.", max_length=2)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}