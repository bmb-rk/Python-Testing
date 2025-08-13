def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
