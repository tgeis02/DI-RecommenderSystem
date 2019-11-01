import enum
from sqlalchemy import Column, Integer, String, Text, Enum, DateTime
from base import Base

class PlatformEnum(enum.Enum):
    github = 1
    gitlab = 2
    bitbucket = 3

class Repository(Base):
    __tablename__ = 'repositories'

    platform_id = Column(Integer, primary_key=True)
    platform = Column(Enum(PlatformEnum), primary_key=True)
    name = Column(String)
    owner = Column(String)
    created = Column(DateTime)
    description = Column(Text)
    issues = Column(Integer)
    commits = Column(Integer)
    releases = Column(Integer)
    last_updated = Column(DateTime)
