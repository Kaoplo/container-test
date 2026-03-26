import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "success", "message": "Hello from FastAPI + uv!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "query": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
