#Write a program which calculates trip cost for a user
#Create a greeting for the program
# Ask the user for number of days
# Ask the user for hotel price
# Ask the user for flight price
# Ask the user for rental car price
# Ask for other expenses
# Combine all expenses together and print with 2 digits after decimal places

print("Welcome to Trip Cost Calculator!")
days = int(input("Enter duration of stay in days: "))
hotel_price = float(input("Enter price of hotel: $ "))
flight_price = float(input("Enter price of flight: $ "))
rental_car_price = float(input("Enter price of car rental: $ "))
expenses = float(input("Enter amount of other expenses: $ "))

calculation_per_day_hotel = days * hotel_price
calculation_per_day_car = days * rental_car_price
calculation = (flight_price + calculation_per_day_car + calculation_per_day_hotel)

print(f"Total cost of trip: ${calculation}")
