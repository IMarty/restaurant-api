from fastapi import FastAPI, HTTPException, status, Header
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
global restaurant_list

# Description
api_description = """ 
Restaurant API helps you do awesome stuff. 

## Restaurants

You will be able to :
* Create new restaurant.
* Get list of Restaurants.


## Testimonials

You will be able to :
* Post new testimonials.
* Get list of all Testimonials.

"""


# Liste des tags utilises dans la doc
tags_metadata = [
    {
        "name" : "Restaurants",
        "description" : " Manage Restaurants List."
    },
    {
        "name" : "Testimonials",
        "description" : " Manage Application Testimonials."
    },
]

app = FastAPI(title="Restaurants API", description=api_description, openapi_tags=tags_metadata)
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

@app.get("/restaurants", tags=["Restaurants"])
def get_all_restaurants():
    return restaurant_list


@app.post("/restaurants", status_code=201, tags=["Restaurants"])
def add_restaurant(body:Restaurant):
    if(body.name !=""):
        restaurant_list.append(body.dict())
        return
    else : 
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="No empty name, thanks"
        )  

@app.delete("/restaurants", status_code=204, tags=["Restaurants"])
def restore_restaurants(secret:str):
    if(secret=="cap4lab"):
        restaurant_list.clear()
        restaurant_list.extend([
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
        ])
        return
    else:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail="Not the good password. Bad Student."
        )  

# Testimonials

testimonials_list  = [
    {
        "name": "John Smith",
        "testimonial": "I love using the delivery restaurant app! It's so convenient and easy to use. I can order food from my favorite restaurants with just a few taps on my phone. The app also provides real-time updates on the status of my order, which is really helpful.",
        "rating": 4.5
    },
    {
        "name": "Emily Johnson",
        "testimonial": "This delivery restaurant app has changed the way I order food. It offers a wide range of restaurants to choose from, and the user interface is clean and intuitive. I particularly appreciate the option to customize my orders and save my favorite meals for quick reordering.",
        "rating": 5.0
    },
    {
        "name": "David Thompson",
        "testimonial": "I highly recommend the delivery restaurant app to everyone who loves good food and convenience. It's a game-changer! The app's search feature makes it effortless to discover new restaurants in my area, and the delivery service is always prompt and reliable. I'm a satisfied customer!",
        "rating": 4.8
    }
]

class Testimonials(BaseModel):
    name: str
    testimonial: str
    rating: float

@app.get("/testimonials", tags=["Testimonials"])
def get_all_testimonials():
    return testimonials_list


@app.post("/testimonials", status_code=201, tags=["Testimonials"])
def add_testimonial(body:Testimonials):
    if(body.name !="" and body.testimonial !=""):
        testimonials_list.append(body.dict())
        return
    else : 
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="No empty name or testimonial, thanks"
        )  

@app.delete("/testimonials", status_code=204, tags=["Testimonials"])
def restore_testimonials(secret:str):
    if(secret=="cap4lab"):
        testimonials_list.clear()
        testimonials_list.extend([
    {
        "name": "John Smith",
        "testimonial": "I love using the delivery restaurant app! It's so convenient and easy to use. I can order food from my favorite restaurants with just a few taps on my phone. The app also provides real-time updates on the status of my order, which is really helpful.",
        "rating": 4.5
    },
    {
        "name": "Emily Johnson",
        "testimonial": "This delivery restaurant app has changed the way I order food. It offers a wide range of restaurants to choose from, and the user interface is clean and intuitive. I particularly appreciate the option to customize my orders and save my favorite meals for quick reordering.",
        "rating": 5.0
    },
    {
        "name": "David Thompson",
        "testimonial": "I highly recommend the delivery restaurant app to everyone who loves good food and convenience. It's a game-changer! The app's search feature makes it effortless to discover new restaurants in my area, and the delivery service is always prompt and reliable. I'm a satisfied customer!",
        "rating": 4.8
    }
])
        return
    else:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail="Not the good password. Bad Student."
        )  