from sqlalchemy import Column, Integer, String, Text, Enum, DateTime

from base import Base


class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column(String)


