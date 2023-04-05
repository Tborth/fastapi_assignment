from fastapi import APIRouter,Request,Depends,Form,status
routes = APIRouter()
import models
from db import engine,sessionlocal
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)
import json

def get_obj():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
@routes.get("/")
async def read_something():
    return {"msg":"Hello , please go to /docs route"}

@routes.get("/address",tags=["address"])
async def home(request:Request,db:Session = Depends(get_obj)):
    person = db.query(models.Person)
    # .order_by(models.User.id.dest())
    person_list=[]
    for person_obj in person:
        per=[]
        per.append(person_obj.id)
        per.append(person_obj.name)
        per.append(person_obj.contact)
        per.append(person_obj.place_name)
        per.append(person_obj.city)
        per.append(person_obj.country)
        per.append(person_obj.state)
        per.append(person_obj.zip)
        per.append(person_obj.latitudes)
        per.append(person_obj.longitude)
        person_list.append(per)
    print(person_list)
    return {"msg":person_list}


@routes.post("/add",tags=["add"])
async def add(request: Request, name: str, contact: str, place_name: str,  city: str ,\
    country: str ,state: str ,zip: str ,latitudes: float ,longitude:float, db: Session = Depends(get_obj)):
    users = models.Person(name=name, contact=contact, place_name=place_name,city=city,country=country,state=state,zip=zip,latitudes=latitudes,longitude=longitude)
    db.add(users)
    db.commit()
    return "user added"

@routes.post("/update/{person_id}",tags=["update"])
async def update(request: Request, person_id: int,name: str, contact: str, place_name: str,  city: str ,\
    country: str ,state: str ,zip: str ,latitudes: float ,longitude:float, db: Session = Depends(get_obj)):
    person = db.query(models.Person).filter(models.Person.id == person_id).first()
    person.name = name if name else person.name
    person.contact = contact if contact else person.contact
    person.place_name = place_name if place_name else person.place_name
    person.city = city if city else person.city
    person.country = country if country else person.country
    person.state= state if state else person.state
    person.zip=zip if zip else person.zip
    person.latitudes=latitudes if latitudes else person.latitudes
    person.longitude=longitude if longitude else person.longitude
    db.commit()
    return f"update the person id {person_id}"

@routes.get("/delete/{person_id}",tags=["delete"])
async def delete(request: Request, person_id: int, db: Session = Depends(get_obj)):
    person = db.query(models.Person).filter(models.Person.id == person_id).first()
    db.delete(person)
    db.commit()
    return  f" user id deleted { person_id }"
    