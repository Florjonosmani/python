greeting = "Hello"
name = "Bob"

def greet():
    global greeting
    name = "Florjon Baba"

    message = f"{greeting}, {name}"
    print(message)

greet()

print(greeting)

print(name)