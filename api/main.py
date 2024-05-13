# main.py

from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

app = FastAPI()

class Recipe(BaseModel):
    id: int
    name: str

@app.get("/recipes")

def get_recipes():
    recipes = [
        {"id": 1, "name": "Massive Muesli"},
        {"id": 2, "name": "Cauliflower, Chickpea and Kale Curry"},
        {"id": 3, "name": "Bean Chilli"}
    ]
    return {"recipes": recipes}

async def root():
    return get_recipes()

