from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class config():
        orm_mode=True

class PostBase(BaseModel):
    title: str
    body: str
    author_id: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author: User
    class config():
        orm_mode=True
