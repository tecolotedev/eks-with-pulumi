from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"ok": True, "message": "hi from python"}


@app.get("/api/")
def api():
    return {"ok": True, "message": "hi from api"}
