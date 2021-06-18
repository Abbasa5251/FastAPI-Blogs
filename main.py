from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.get("/")
def index():
    return {
        "data": "blog list"
    }

@app.get("/blog/unpublished")
def unpublished():
    return {
        "data": [
            "unpublished blogs"
        ]
    }

@app.get("/blog/{id}")
def blog(id: int):
    return {
        "data": {
            "id": id,
        }
    }

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {
        "data": {
            "id": id,
            "comments": [
                "comment 1",
                "comment 2",
                "comment 3",
            ]
        }
    }

@app.post("/blog")
def create_blog(blog: Blog):
    return blog