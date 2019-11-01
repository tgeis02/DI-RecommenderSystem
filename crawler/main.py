from sqlalchemy import create_engine

from base import Base
import languages
import repositories

engine = create_engine('postgresql://admin:password@localhost:5432/recommenderdb', echo=True)
Base.metadata.create_all(engine)
