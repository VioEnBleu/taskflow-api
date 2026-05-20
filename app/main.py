from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "hello world",
        "status": "ok"
    }

def hello():
    print("hello")