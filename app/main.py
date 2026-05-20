from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "API V2 is up and running",
        "status": "ok"
    }

def hello():
    print("hello")