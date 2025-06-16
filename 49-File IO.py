# #Reading a file
# f= open('myfile.txt','r')
# #print(f)
# text=f.read()
# print(text)
# f.close()

# #Writing a file
# f=open('myfile.txt','w')
# f.write('hello, world!') #file khali karine aa lakhi nakhe
# f.close()

with open('myfile.txt','a') as f:
    f.write("Hey i am inside with")