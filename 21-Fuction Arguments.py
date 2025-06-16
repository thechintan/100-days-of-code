# def average(a=9,b=1):   #default Arguments
#     print("Average is", (a+b)/2)
# average(1,5)  #banne jagya ae values put kari chhe to default argument ignore thase
# average(b=7) #a ni value default argu. ma thi levama aavse
# average(b=7,a=21) #Order change thai gyo, order ki parwah nahi karni hai

# #Reqired arguments::--
# def average(a,b,c=1):
#     print("Average is", (a+b+c)/2)
# average(5,6)

#vadhare padta numbers na average mate
def average(*numbers):   #numbers are taken as a tuple
    sum=0
    for i in numbers:
        sum+=i
    print("Average is :",sum/len(numbers))
average (5,6,7,1)

#or we can write it as return
def average(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum/len(numbers)
c=average (5,6,7,1)
print(c)

# def name (**name):  #name type=dictionary
#     print ("Jay swaminarayan",
#     name ['fname'],name['mname'],name['lname'])
    
# name(mname='Chintan',lname='Kirtibhai',fname='Boghani')
