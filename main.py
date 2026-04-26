from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


people = {
    1: {
        "name": 'George',
        "age": "24",
        
    }
}



@app.get("/")
def index():
    return {"name": "Data test"}

@app.get("/get-people/{people_id}")
def get_people(people_id: int):
    return people[people_id]