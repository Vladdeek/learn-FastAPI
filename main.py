from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/")
async def home() -> dict[str, str]:
    return {"data" : "message"}

@app.get("/contacts")
async def contacts() -> int:
    return 34

posts = [
    {"id": 1, "title": "news 1", "body": "text 1"},
    {"id": 2, "title": "news 2", "body": "text 2"},
    {"id": 3, "title": "news 2", "body": "text 3"},
]

@app.get("/items")
async def items() -> list:
    return posts

@app.get("/items/{id}")
async def items(id: int) -> dict:
    for post in posts:
        if post["id"] == id:
            return post
    raise HTTPException(status_code=404, detail="post not found")

@app.get("/search")
async def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post["id"] == post_id:
                return post
        raise HTTPException(status_code=404, detail="post not found")
    else:
        return {"data": "no post id provided"}
    