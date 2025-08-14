from fastapi import FastAPI

app = FastAPI(root_path="/api")


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI 🚀"}
