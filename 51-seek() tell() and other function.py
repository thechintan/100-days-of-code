# with open('myfile.txt','r') as f:
#     print(type(f))
#     f.seek(10) #move to the 10th byte of the file
#     print (f.tell())
#     data=f.read(5) #read the next 5 bytes
#     print(data)

with open('myfile.txt','w') as f:
    f.write('Hello world')
    f.truncate(8)