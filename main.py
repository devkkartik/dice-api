# main.py
from fastapi import FastAPI
import random

app = FastAPI(title="Dice API")

@app.get("/")
def root():
    return {"message": "Dice API — use GET /roll to roll a die"}

@app.get("/roll")
def roll():
    """Return a random integer between 1 and 6."""
    value = random.randint(1, 6)
    return {"value": value}
