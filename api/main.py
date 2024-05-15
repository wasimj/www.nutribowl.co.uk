# main.py

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # List of allowed methods
    allow_headers=["Content-Type", "Authorization"],  # List of allowed headers
)

class Recipe(BaseModel):
    id: int
    name: str

@app.get("/recipes")

def get_recipes():
    recipes = [
        {"id": 1, "name": "Massive Muesli"},
        {"id": 2, "name": "Cauliflower, Chickpea and Kale Curry"},
        {"id": 3, "name": "Bean Chilli"},
        {"id": 4, "name": "Ginger Kombucha"}
    ]
    return {"recipes": recipes}

async def root():
    return get_recipes()

