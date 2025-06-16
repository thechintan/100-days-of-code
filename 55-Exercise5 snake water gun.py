#                S W G
#computer =      
#player =   S    D w L
#           W    L D w
#           G    w L D

import random
choices= ['snake','water','gun']
user=(input("Your Choice(snake/water/gun): "))
computer= random.choice(choices)
print("Computer's Choice=",computer)

if user==computer:
    print('Match Draw')
elif user=='snake' and computer=='water':
    print("You Won")
elif user=='water' and computer=='gun':
    print("You Won")
elif user=='gun' and computer=='snake':
    print("You Won")
else:
    print("You Lost")

