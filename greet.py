def greet(name: str, age: int) -> str:
    if len(name) == 0:
        print("No name was given, please try again")
        return
    elif age <= 0:
        print("Please enter an appropriate age")
        return
    else:
        return f"Hello, {name}!  You are {age} years old."  # here you should return the final string "Hello, [name]! You are [age] years old."


print(greet("Frank", 55))
