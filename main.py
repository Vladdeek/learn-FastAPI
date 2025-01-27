from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
class Post(BaseModel):
    id: int 
    title: str
    body: str
    author: User

users = [
    {"id": 1, "name": "John", "age": 33},
    {"id": 2, "name": "Alex", "age": 32},
    {"id": 3, "name": "Steve", "age": 36},
]

posts = [
    {"id": 1, "title": "news 1", "body": "text 1", "author": users[0]},
    {"id": 2, "title": "news 2", "body": "text 2", "author": users[1]},
    {"id": 3, "title": "news 2", "body": "text 3", "author": users[2]},
]

#@app.get("/items")
#async def items() -> List[Post]:
#    post_objects = []
#   for post in post_objects:
#       post_objects.append(Post(id=post["id"], title=post["title"], body=post["body"]))
#    return post_objects

@app.get("/items")
async def items() -> List[Post]:
    return [Post(**post) for post in posts ]

@app.get("/items/{id}")
async def items(id: int) -> Post:
    for post in posts:
        if post["id"] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="post not found")

@app.get("/search")
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post["id"] == post_id:
                return {"data": Post(**post)}
        raise HTTPException(status_code=404, detail="post not found")
    else:
        return {"data": None}
    