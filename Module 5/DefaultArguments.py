


def greet_person(name,greeting="Hello"):
    message = f"{greeting},{name}"
    return message

default_greeting = greet_person("Alice")

print(default_greeting)

custom_greeating = greet_person("Bob","Hi")

print(custom_greeating)