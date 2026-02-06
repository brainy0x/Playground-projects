#Write a program that prompts the user for hours and rate per hour to compute the gross pay. You need to take into account that the result has exactly two digits after the decimal point 
print("Welcome to the Gross Pay Calculator!")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter rate per hour: $ "))

gross_pay = rate * hours
print(f"Your gross pay is ${gross_pay}")