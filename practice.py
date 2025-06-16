# #Q1: Print numbers from 1 to 10
# a=0
# while a<10:
#     print (a+1)
#     a+=1

## Q2: Guess the secret number (let's say the number is 5)
# secret=5
# for i in range (10):
#     guess=int(input("guess the number: "))
#     if guess==secret:
#         print("correct")
#         break
#     else: 
#         print("incorrect")
#or
# secret=5
# while True:  #true lakh ke i<5 lakh,kai fark naa pade,i+=1 lakh to limit lagi jay input devani nahitar infinite input aapi shakay
#     guess=int(input("guess the number: "))
#     if guess==secret:
#         print("correct")
#         break
#     else: 
#         print("incorrect")
    
##Q3: Print each character of "Hello"
# for i in "Hello":
#     print(i)

# Q4: Print elements with index
# list=['Apple','Banana','Mango']
# for i in range(len(list)):
#     print(list[i])

#Q5: Check even/odd (input: 7)
# i=int(input("enter the number: "))
# if i%2==0:
#     print("even")
# else:
#     print("odd")

# # Q6: Grade remarks (input: B)
# grade=str(input("your grade: "))
# if grade=='A':
#     print('excellent')
# elif grade=="B":
#     print("Good job")
# else:
#     print("Fail")

#Q7: Even numbers in [1, 2, 3, 4, 5, 6]
# list=[1, 2, 3, 4, 5, 6]
# for i in range(1,6,2):
#     print(list[i])

#Q8: Modify a list
# list= [10, 20, 30]
# list.append(40)
# print(list)
# list.remove(20)
# print(list)
# list.insert(1,25)
# print(list)
# list.remove(40)
# print(list)
# list.pop(1)
# print(list)

#Q9: Reverse a string (input: "Python")
# string="Python"
# print(string.replace("Python","nohtyP"))
# #or
# text = "Python"
# reversed_text = text[::-1]
# print("Reversed string:", reversed_text)

#Q10: Count a letter (input: "banana", count of "a")
# string="banana"
# print(f"a appears {string.count('a')} times")

#Q13: Print each item
# tuple=('Red','Green','Blue','Yellow','Black')
# for i in range (len(tuple)):
#     print(tuple[i])

#Q15: Factorial of 5
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# Q16: Write a function that takes a list of numbers and returns only the even numbers
# list=[1,2,3,4,5,7,8,9]
# def even(numbers):
#     for n in numbers:
#         if n%2==0:
#             print(n)
# even(list)
#     #or
# def even(list):
#     for n in list:
#         if n%2==0:
#             print(n)
# even(list)

#Q17:wap if number is even then find square and if number is odd then find a cube

# for i in range (1,11):
#     if i%2==0:
#         print(i*i)
#     else:
#         print(i*i*i)

#Q.18

# def triangle():
#     for i in range(1,6):
#         print("*"*i)
# triangle()

def count_distinct_prime_factors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1  # remaining n is a prime number
    return count

# Example usage
n = int(input("Enter a number: "))
print("Count of distinct prime factors:", count_distinct_prime_factors(n))
