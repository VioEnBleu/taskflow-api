from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "API V2 is up and running",
        "status": "ok"
    }

@app.get("/hello")
def hello_endpoint():
    return {
        "message": "Hello, World!"
    }

@app.get("/snake")
def snake_endpoint():
    with open ("snake.html", "r") as file:
        snake_game = file.read()
    
    return HTMLResponse(content=snake_game, status_code=200)