from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Sale(name='{self.name}', price={self.price}, date='{self.date}')>"
