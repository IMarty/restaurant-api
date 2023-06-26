from fastapi import FastAPI, HTTPException, status, Header
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
restaurant_list= [
    {"name": "Mac Donalds", "likes": 10, "currentlyOpen": True},
    {"name": "Burger King", "likes": 15, "currentlyOpen": True},
    {"name": "Pizza Hut", "likes": 8, "currentlyOpen": False},
    {"name": "Subway", "likes": 12, "currentlyOpen": True},
    {"name": "KFC", "likes": 20, "currentlyOpen": True},
    {"name": "Taco Bell", "likes": 5, "currentlyOpen": False},
    {"name": "Chipotle", "likes": 18, "currentlyOpen": True},
    {"name": "Wendy's", "likes": 7, "currentlyOpen": False},
    {"name": "Starbucks", "likes": 25, "currentlyOpen": True},
    {"name": "Dunkin' Donuts", "likes": 6, "currentlyOpen": False}
]

class Restaurant(BaseModel):
    name: str
    likes: int
    currentlyOpen: bool

@app.get("/restaurants")
def get_all_restaurants():
    return restaurant_list


@app.get("/restaurants/{item_id}")
def get_restaurant(item_id: int):
    try: 
        corresponding_product = restaurant_list[item_id] #parce id commence à 1 et index commence à 0
        return corresponding_product
    except:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return 

@app.post("/restaurants", status_code=201)
def add_restaurant(body:Restaurant):
    if(body.name !=""):
        restaurant_list.append(body.dict())
        return
    else : 
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Go away, Bitch"
        )  

@app.delete("/restaurants", status_code=204)
def restore_restaurants(secret:str):
    if(secret=="cap4lab"):
        restaurant_list= [
            {"name": "Mac Donalds", "likes": 10, "currentlyOpen": True},
            {"name": "Burger King", "likes": 15, "currentlyOpen": True},
            {"name": "Pizza Hut", "likes": 8, "currentlyOpen": False},
            {"name": "Subway", "likes": 12, "currentlyOpen": True},
            {"name": "KFC", "likes": 20, "currentlyOpen": True},
            {"name": "Taco Bell", "likes": 5, "currentlyOpen": False},
            {"name": "Chipotle", "likes": 18, "currentlyOpen": True},
            {"name": "Wendy's", "likes": 7, "currentlyOpen": False},
            {"name": "Starbucks", "likes": 25, "currentlyOpen": True},
            {"name": "Dunkin' Donuts", "likes": 6, "currentlyOpen": False}
        ]
        return
    else : 
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail="Go away, Bitch"
        ) 