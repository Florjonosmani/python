from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/")
def read_item():
    return {"items":["item1","item2","item3"]}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Florjon Osmani"}




@app.get("/items/")
def get_itmes(skip:int =0,limit:int =10):
    return {"skip":skip, "limit": limit}

#GET- merr data
#POST - kriju data(dergon te dhena ne server)
#PUT - updata date
#Delete - fshin


@app.put("items/{item_id}")
def update_item(item_id: int, name: str,price:float):
    return {"item_id": item_id, "item_name": name, "item_price":price}


app.post("/items/")
def create_items(name:str, price:float):
    return {"item_name":name, "item_price":price}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {"message": f"{ item_id} deleted"}