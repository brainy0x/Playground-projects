# TODO
#Write a program that calculates the area of circle based on user input of radius using equation provided below. 
#The output must be rounded to 2 decimal places.
import math
r = int(input("Enter Radius: "))
area = math.pi * (r * r)
print(f"The area of circle is: {round (area, 2)}")
