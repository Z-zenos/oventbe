"""
Minimal FastAPI application taken directly from the tutorial.
https://fastapi.tiangolo.com/
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str = ""
    is_offer: bool = False


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None) -> dict[str, str | None]:
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item) -> dict[str, int]:
#     return {"item_name": item.name, "item_id": item_id}
