def greet(name, uppercase=False):
    greeting = f"Hello, {name}!"
    return greeting.upper() if uppercase else greeting

if __name__ == "__main__":
    print(greet("GitHub"))
    print(greet("GitHub", uppercase=True))
