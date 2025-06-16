letter="Hey my name is {} and i am from {}"
country="India"
name="Harry"
print(letter.format(name,country))

#or

letter="Hey my name is {1} and i am from {0}"
country="India"
name="Harry"
print(letter.format(country,name))

#OR Using f-string
country="India"
name="Harry"
print(f"Hey my name is {name} and i am from {country}")

#curly brackers print karavva hoi to
print(f"Hey my name is {{name}} and i am from {{country}}")

#what is :.3f?
price=49.9806543217
print(f"An apple for only {price:.3f} rupees ")
#OR
text=f'An apple for only {price:.1f} rupees'
print(text)
#OR
print(f"An apple for only {price:.0f} rupees ")
#OR
print(f"An apple for only {price:.2f} rupees ")

print(2*30) #type=int
print(type(2*30))
print(f"{2*30}") #type=string
print(type(f"{2*30}"))

