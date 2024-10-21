def add(a, b):
    print(f"adding {a} + {b}")
    return a+b

def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"multiplying {a} + {b}")
    return a*b

def divide(a, b):
    print(f"dividing {a} + {b}")
    return a/b

print('let`s do some math with just functions!')

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq =divide(100, 2)

print(f"age: {age}, heitht: {height}, weight: {weight}, IQ: {iq}")

# a puzzle for the extra credit, type it in anyweay

print("here is a puzzle. ")

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) 

print("the becomes:",  what , "can you do it by hand?")

"""
怎样使用input() 输入自己的值？
记得int(input()) 吧？不过这样也有一个问题，
那就是无法输入浮点数，所以可以试着使用float(input()) 。
"""
