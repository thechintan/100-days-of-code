marks =[3,5,6, "Harry",True]
print(marks)
print(marks[0])   #alt shift down to paste the line
print(marks[1])
print(marks[2])   #list mutable,tuple immutable
print(marks[3])
print(marks[-3])
 

if 7 in marks: print('yes')
else:print("no")  #7 is not there in list,hence no

if "6" in marks:
     print('yes')
else:
     print("no")  #No because 6 is integer ,not a string

if "arry" in "Harry":
     print('yes')
else:
     print("no")  #same thing is applied for string also

print(marks) #== print (marks[:])

lst= [i*i for i in range (4)]  #To creare a list
print (lst)

lst= [i*i for i in range (10) if i%2==0]  #condition in list
print (lst)
