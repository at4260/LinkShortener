"""
To create the initial table:
    python -i model.py
    engine = create_engine("sqlite:///database.db", echo=True)
    Base.metadata.create_all(engine)
"""

from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

engine = create_engine("sqlite:///database.db", echo=True)
session = scoped_session(sessionmaker(
    bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    original_link = Column(String(500), nullable=False)
    shortened_link = Column(String(500), nullable=False)
    
    def __repr__(self):
        return "<Link ID=%s Shortened Link=%s>" % (
            self.id, self.shortened_link)

def main():
    pass

if __name__ == "__main__":
    main()