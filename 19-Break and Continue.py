# for i in range (13):
#     print('5 x',i+1,'=',5*(i+1))
#     if i==9:  #continue statement
#         break # i ni value 9 thai tyare loop chhodi deshe

# second way
# for i in range(1,12):
#     print ("5 x",i,"=",5*i)
#     if i==10:
#         break
    
# for i in range(1,12):
#     if i==10:
#         print("skip the iteration")
#         continue    
#     print ("5 x",i,"=",5*i)

i=1
while True:    #while true lakhva thi infinite loop thai jai
    print (i)
    i+=1
    if i%10==0:
        break  
    
