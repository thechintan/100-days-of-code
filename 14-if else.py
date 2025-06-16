# age=int(input('Enter your age: '))
# if age>=18:
#   print('You can drive\nyes')
# else:
#   print('You cannot drive')

n=-8
if n<0:
  print('negative')
elif n==0:
  print('zero')
elif n>0:
  print('positive')
else:
  print("Imaginary")

n=11
if n<0:
  print('negative')
elif n>0:
  if n<=10:
    print('1-10')
  elif 10<n<=20:
    print('11-20')
  else:
    print('greater than 20')
else:
  print(n is zero)