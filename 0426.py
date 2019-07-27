def my_plus(x,y):
    return x+y
def my_minus(x,y):
    return x-y
def my_mul(x,y):
    return x*y
def my_div(x,y):
    return x/y

def my_calculate(x,y,opcode="+"):
    if opcode=="-":
        return my_minus(x,y)
    elif opcode=="*":
        return my_mul(x,y)
    elif opcode == "/":
        return my_div(x,y)
    else :
        return my_plus(x,y)

print("Input two numbers: ")
x=int(input())
y=int(input())
opcode=input("Input operation: ")
print("Result is ", my_calculate (x,y,opcode))

