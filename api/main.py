from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import settings

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

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