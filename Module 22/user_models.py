from pydantic import BaseModel,conint,constr

#class User(BaseModel):
#    id: int
#    name: str
#    age:int
#    email:str

#user = User(id=1,name="florjon Osmani", age=20,email='floniflori@gmail.com')
#print(user)


#Modifyning the previous model
class User(BaseModel):
    id: int
    name: str
    age:int = 0
    email:str = "noeemail@example.com"


user = User(id=2,name="John")



user2 = User(id=3,name="Alice",age=25)
print(user2)


class Another_user(BaseModel):
    id: conint(gt=0)#id must be grater than 0
    name: constr(min_length=2,max_length=50)



valid_user = Another_user(id=1,name="florjon")
print(valid_user)


