from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.setup import Base

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    nationality = Column(String)
    
    books = relationship("Book", back_populates="author")
    
    def __repr__(self):
        return f"<Author(name={self.name}, birth_year={self.birth_year}, nationality={self.nationality})>"
