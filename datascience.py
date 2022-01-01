# Assignment by Jawan Pakistan Data Science

# Write a Program to Get Current Version of Python
import sys
print(sys.version)

# Write a program to see format of string in specific format(Given in question)
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Write a program to get date and time
from datetime import datetime
now = datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Addition of two Number
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

# Accept First And Last Name From User And Print it on reverse way
firstName = input("Enter your first Name\n")
lastName =  input("Enter your last name\n")
firstLast = print(f"{firstName} {lastName}" [::-1])

# Taken input from user and compute the area . In my case I calculate the area of ellipse
class ellipse():

    pie = 3.14
    #class objec attributes

    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis


    def area(self):
        return self.pie*self.major_axis*self.minor_axis


my_ellipse = ellipse(major_axis=int(input('Enter major axis')), minor_axis=int(input('Enter minor axis')))

print(my_ellipse.area())


