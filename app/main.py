from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "k8s"}