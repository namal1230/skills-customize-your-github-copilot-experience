# Starter code for REST APIs with FastAPI assignment

# Install FastAPI and Uvicorn if not already installed
# pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage for items
items = []

# TODO: Implement the endpoints here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
