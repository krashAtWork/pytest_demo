def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def division(a, b):
    if b !=0:
        return a//b
    else:
        raise ZeroDivisionError("Zero division error")
    
def subtract(a, b):
    return a - b