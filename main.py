from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test_app():
    return ("HELLO-WORLD")