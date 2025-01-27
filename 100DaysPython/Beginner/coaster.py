print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0


if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age > 44 and age < 56:
        print("Congratulations! Your ride is free!")
    else:
        bill = 12
        print("Adult tickets are $12.")

wants_photo = input("Do you want a photo taken? Y or N. ")
wants_photo = wants_photo.capitalize()
if wants_photo == "Y":
    bill = bill + 3  # or bill += 3

print(f"Your final bill is ${bill}")
