from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Cloud Run from pugazh "}

@app.get("/health")
def health():
    return {"status": "ok"}
