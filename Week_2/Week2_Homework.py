#Problem #2

'''
print("Welcome to an Area of Circle Calculator! Please respond with the following values.")
PI = float(3.14) #Constant values get Capital letters!
radius = (float(input("What is your radius?: ")))
area_of_circle = (PI*radius**2)
print ("The area of your circle is: ", area_of_circle)
'''

#Problem #3
'''
print ("Welcome to the kilometers to miles calculator! Please Respond with the following values.")
kilometers = float(input("Kilometers to convert?: "))
miles = kilometers / float("1.61")
print (miles)
'''

#problem #4
'''
print("Welcome to the minutes to seconds converter! PLease respond with s following values.")
minutes = float(input("How many minutes would you like to convert?: "))
seconds = float(input("How many seconds would you like to convert?: "))
minutes_conversion = (minutes*60)
total = (minutes_conversion+seconds)
print("Your conversion is: ", total, "Seconds.")
'''

#Additional Practice #1

'''
a = "6"
temp = a
b = "4"
print (a)
print (b)
print ("Here are the variables unchanged!")
a=b
b = temp
print (a)
print(b)
print ("Here is the variables swapped! ")
'''

#Additional Practice #2
'''
input_1 = int(input ("What is the first number you would like to have averaged?: "))
input_2 = int(input ("What is the second number you would like to have averaged?: "))
average = (input_1 + input_2) /2
print (average)
'''

#Additional Practice #3
'''
first_name = input ("What is your first name?: ") 
last_name = input("What is your last name?: ")
country = input("What country do you live in?: ")
age = input ("What is your current age?: ")
print ("Hello", first_name, last_name, "Your current age is", age, "and you live in", country)
'''

#Additional Practice #4
'''
kilometers = int(input ("How many kilometers did you run?: "))
hours = int(input ("How many hours did that take?: "))
minutes = int(input ("How many minutes?: "))
seconds = int(input ("How many seconds?: "))
convert_hours = hours + (minutes/60) + (seconds/3600)
miles = (kilometers/ float(1.61))
print ("You ran", miles, " miles in this many hours:", convert_hours)
mph = (miles /convert_hours)
print ("Here is your time in miles per hour:", mph)
'''