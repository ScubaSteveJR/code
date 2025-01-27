import math

print("Welcome to your very own tip calculator!\n")
bill = float(input("How much was the total bill? "))
tipPercent = int(input("What percent would you like to tip? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))
tipAsPercent = tipPercent / 100
tipAmount = bill * tipAsPercent

pay = (tipAmount + bill) / people
payR = round(pay, 2)
payR = "{:.2f}".format(pay)

print(f"Each person will pay: ${payR}")
