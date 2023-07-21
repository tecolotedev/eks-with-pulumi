from fastapi import FastAPI
import os

app = FastAPI()

SERVER_NAME = os.getenv("SERVER_NAME", "DEFAULT NAME")


@app.get("/")
def home():
    return {"ok": True, "message": f"hi from {SERVER_NAME}"}


@app.get("/api/")
def api():
    return {"ok": True, "message": "hi from api"}
