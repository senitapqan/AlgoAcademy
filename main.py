from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def read_root():
    return {"message": "Hello, World!"}