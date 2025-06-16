def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def fibonacci(n):
    a = 0  
    b = 1  
    for i in range(n):
        print(a)
        a,b= b,a+b
fibonacci(11)
#OR
a = 0  
b = 1  
for i in range(11):
    print(a)
    a,b= b,a+b