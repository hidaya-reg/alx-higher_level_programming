from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):  # This class inherits from the Base created by declarative_base
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
