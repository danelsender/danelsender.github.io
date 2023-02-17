from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def homepage():
    return f"Hello, World!"

@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}!"