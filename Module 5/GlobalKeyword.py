

greeting = "Hello"

def greet(name):
    '''Declaring 'Message' as a global variable'''
    global message
    message =f"{greeting}, {name}"
    print(message)

greet("bob")
print(message)


message = f"{greeting},student"
print(message)