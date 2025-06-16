#Strings are immutable
a='!!!Har ry !!!'
print(a.upper())
print(a.lower())
print(a.rstrip('!')) #starting exclamation mark will not be removed
print(a.replace('Harry','Chintan'))
print(a.split(' '))

Heading="intrOduction to PytHon"
print(Heading.capitalize())

str1="Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)) )
print(a.count('Harry'))
print(str1.endswith("!!!"))
print(str1.find("aokdjaj"))
print(str1.find('the'))
print(str1.index('the'))
print(str1.isalnum())

str2= "WelcomeToTheConsole"
print(str2.isalnum())
print(str1.isalpha())
print(str1.islower())

str1= "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1= "        "       #using Spacebar
print(str1.isspace())

str1= "World Health Organization"
print(str1.istitle())

str2= "To kill a Mocking bird"
print(str2.istitle())

str1= "Python is a Interpreted Language"
print(str1.startswith("Python"))
print(str1.swapcase())
str1= "His name is Dan. Dan is an honest man."
print(str1.title())
