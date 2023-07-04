from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from enum import Enum  
app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

class Category(Enum):
    TOOLS="tools"
    CONSUMABLES="consumables"

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    Category: Category

items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, Category=Category.TOOLS),
    1: Item(name="Nails", price=5.99, count=100, id=1, Category=Category.CONSUMABLES),  
    2: Item(name="Piers", price=9.99, count=20, id=2, Category=Category.TOOLS),
}

@app.get('/')
def index() -> dict[str, dict[int, Item]]:
    return {'items': items}