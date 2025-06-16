a=(input("Enter the number: "))
print(f"multiplication table of {a} is: ")

try:
  for i in range (1,11):
    print(f"{float(a)} x {i} = {float(a)*i}")
except Exception as e:
    print(e) #==priint("Invalid Input")
print("Please Enter Numbers Only")

#except ValueError:
#except IndexError:
