def add(a, b):
    """Повертає суму двох чисел."""
    return a + b

def multiply(a, b):
    """Повертає добуток двох чисел."""
    return a * b

if __name__ == "__main__":
    x = 10
    y = 7
    print(f"Sum of {x} and {y} is {add(x, y)}")
    print(f"Product of {x} and {y} is {multiply(x, y)}")
