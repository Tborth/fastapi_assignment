from sqlalchemy import Column,Integer,String,Float

from db import Base

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key =True)
    name = Column(String(150))
    contact =Column(String(150))
    place_name = Column(String(150))
    city   = Column(String(150))
    country  = Column(String(150))
    state   = Column(String(150))
    zip     = Column(String(150))
    latitudes =  Column(Float(150))
    longitude =  Column(Float(150))
   
    
    def __repr__(self):
        return '<person %r ' % (self.id)
    