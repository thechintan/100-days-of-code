# a=int(input("Enter any value between 5 and 9: "))
# if a<5 or a>9 :
#     raise ValueError("Value should be between 5 and 9")


#quick quiz
a=input("Enter any value between 5 and 9: ")
if a=='6' or a=='7' or a=='8' or a=="quit":
    print("Code ran successfully")
else:
    raise ValueError("Value should be between 5 and 9")