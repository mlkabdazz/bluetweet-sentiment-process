from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgres://uuuvydfagounha:0a09d4304d05a75ae81ed01b353d9a2c44e13c41c41a3e0c860b398a80ba25e9@ec2-174-129-255-76.compute-1.amazonaws.com:5432/d6binvd45dcfp8')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import apps.src.models.account_tweet
    import apps.src.models.sentiment
    Base.metadata.create_all(bind=engine)
