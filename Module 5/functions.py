from pandas.core.computation.common import result_type_many


def greet():
    print("hello world!")

greet()


def greet_person(name):
    print("Hello,",name)

greet_person("Ron Baba")
greet_person("Florjon Baba")

'''
def add (x,y):
   z=x+y
   :return z
   
add(3,7)   
'''


def add(x,y):
    z = x + y
    return z
result= add(3, 7)

print("The result of 3+7= ", result)

