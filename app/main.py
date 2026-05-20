from fastapi import FastAPI
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
    
    return {
        snake_game
    }

def test_failure():
    assert 1 == 2