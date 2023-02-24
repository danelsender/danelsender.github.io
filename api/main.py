from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import settings

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"];
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html", {"request": request})

@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}!"

@app.get("/code", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("code.html", {"request": request})

@app.get("/cv", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("cv.html", {"request": request})

@app.get("/gallery", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("gallery.html", {"request": request})

@app.get("/publications", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("publications.html", {"request": request})

class SampleInput(BaseModel):
    x: int

@app.post("/sample")
async def sample(input: SampleInput):
    return input.x**2