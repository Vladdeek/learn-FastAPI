from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Optional, List, Dict, Annotated
from sqlalchemy.orm import Session

#импорт наших классов
from models import Base, User, Post
from database import engine, session_local
from schemas import UserCreate, User as DbUser, PostCreate, Post as DbPost # "as" создает песевдоним для того что бы названия не конфликтовали 


app = FastAPI()

Base.metadata.create_all(bind=engine)


# функция создает сессию для подключения к ДБ
def get_db():
    db = session_local()
    try:
        yield db 
    finally:
        db.close()


@app.post("/users/", response_model=DbUser) # response_model=DbUser указывает, что ответ на запрос будет соответствовать модели DbUser(User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> DbUser:     
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@app.post("/posts/", response_model=DbPost)
async def create_post(post: PostCreate, db: Session = Depends(get_db)) -> DbPost:     
    db_user = db.query(User).filter(User.id == post.author_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post
    

# Вывод всех данных
@app.get("/users/", response_model=List[DbUser])
async def users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/posts/", response_model=List[DbPost])
async def posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


# Самостоятельная работа, я захотел попробовать сделать вывод конкретных пользователей и постов по id
@app.get("/user/{id}", response_model=DbUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/post/{id}", response_model=DbPost)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="User not found")
    return post

