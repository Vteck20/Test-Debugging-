#add 2 numbers
def  add(x, y):
    return x + y

#subtract 2 numbers
def sub(x, y):
    return x - y

#multiple 2 numbers
def mul(x,y):
    return x * y

#divide 2 numbers
def div(x,y):
    if y == 0:
        raise ValueError("Can not be divdie by 0")
    return x / y

