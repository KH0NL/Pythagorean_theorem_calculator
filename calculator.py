import math
print("Pythagorean theorem calculator")
def find_c(a,b):
    print("a² + b² = c²")
    print(f"({a}cm)² + ({b}cm)² = c²")
    print(f"{a*a}cm² + {b*b}cm² = c²")
    result = (a*a) + (b*b)
    print(f"{a*a}cm² + {b*b}cm² = {result}cm²")
    print("c = √c²")
    print(f"c = √{result}")
    result2 = math.sqrt(result)
    print(f"c = {result2}cm")
def find_a(b,c):
    print("a² + b² = c²")
    print(f"a² + ({b}cm)² = ({c}cm)²")
    print(f"a² + {b*b}cm² = {c*c}cm²")
    result = (c*c) - (b*b)
    print(f'a² = b² - c²')
    print(f'a² = {b*b}cm² - {c*c}cm²')
    print(f'a² = {result}cm²')
    print(f'a = √a²')
    print(f'a = √{result}cm²')
    result2 = math.sqrt(result)
    print(f'a = {result2}cm')
def find_b(a,c):
    print("a² + b² = c²")
    print(f'({a}cm)² + b² = ({c}cm)²')
    print(f'{a*a}cm² + b² = {c*c}cm²')
    result = (c*c) - (a*a)
    print(f'b² = a² - c²')
    print(f'b² = {a*a}cm² - {c*c}cm²')
    print(f'b² = {result}cm²')
    print('b = √b²')
    print(f'b = √{result}cm²')
    result2 = math.sqrt(result)
    print(f'b = {result2}cm')

def str_to_int_float(x):
    if "." in x:
        return float(x)
    else:
        return int(x)
def mode1():
    x = input("a = ")
    y = input("b = ")
    x = str_to_int_float(x)
    y = str_to_int_float(y)
    find_c(x,y)
def mode2():
    x = input("b = ")
    y = input("c = ")
    x = str_to_int_float(x)
    y = str_to_int_float(y)
    find_a(x,y)
def mode3():
    x = input("a = ")
    y = input("c = ")
    x = str_to_int_float(x)
    y = str_to_int_float(y)
    find_b(x,y)
    
while True:
    print(" ")
    print(" 1 - find c \n 2 - find a \n 3 - find b")
    inp = input()
    if inp == "1":
        mode1()
    else:
        if inp == "2":
            mode2()
        else:
            if inp == "3":
                mode3()
