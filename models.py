from sqlalchemy import Column, Integer, String, ForeignKey #ForeignKey будет ссылаться на поле из другой таблицы 
from sqlalchemy.orm import relationship # для создания связи между полями 
from database import Base # все наше подключение которое которое на основе наших моделей создает таблицы в БД

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)# index=True - поиск по этому столбцу
    name = Column(String, index=True)
    age = Column(Integer)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User")# Доп. поле в которое мы будем помещать информацию про пользователя
    # для этого в схемах в классе Post добавляем author: User


# Этот файл описывает каждую табличку для БД
# на основе этого файла на основе этих классов 
# будут созданы разные таблицы в БД