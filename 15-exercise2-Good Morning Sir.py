import time
Time=(time.strftime("%H:%M:%S"))
Time = int(time.strftime("%H"))
print("Samay =",Time)

if Time>=6 and Time<11:
  print("Good Morning")
elif (11<=Time<16):
  print("Good Afternoon")
elif (16<=Time<22):
  print("Good Evening")
else:
  print("Sweet Dreams")
