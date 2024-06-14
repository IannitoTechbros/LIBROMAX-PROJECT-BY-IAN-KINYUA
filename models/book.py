from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    published_year = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    
    author = relationship("Author", back_populates="books")
    
    def __repr__(self):
        return f"<Book(title={self.title}, genre={self.genre}, published_year={self.published_year}, author_id={self.author_id})>"
