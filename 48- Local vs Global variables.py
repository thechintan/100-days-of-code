# x=4  #global variable
# print(x)

# def hello():
#     x=5  #local variable
#     print("The local variable x is",x)

# print(f"The global variable x is {x}")
# hello()
# x=6
# print(f"The global x is {x}")

x=10

def my_function():
    global x #global is a keyword
    x=4 #changing global variable
    y=5 #lical variable
    print(y)

my_function()
print(x)
print(y) #throws erro as it's not a global variable
