from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"Message": "Hello world"}


@app.get("/greet/")
def read_root(name: str):
    return {"Message": f"Hello,{name}"}

