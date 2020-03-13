#Ask user for name

name = input("what is your name?: ")
print(name)



#Ask user for age

age = input("What is your age?: ")
print(age)

#Ask user for city
city = input("City living in?: ")
print(city)


#Ask user what they enjoy
love= input ("what do you love doing?: ")
print(love)
#Create output text

string = "your name is {} and you are {}. you live in {} and you love {}"
output = string.format(name, age, city, love)
#print output to screen


print(output)
