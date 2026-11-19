from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hi through Docker Volume"}

@app.get("/students")
def get_students():
    return [
        {"id": 1, "name": "Rahul"},
        {"id": 2, "name": "Priya"}
    ]