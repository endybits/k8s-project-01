import os

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "hello": "k8s",
        "from hostname": f"{os.environ.get('HOSTNAME', 'DEFAULT_ENV')}"
    }