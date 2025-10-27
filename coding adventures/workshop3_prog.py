age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
    input("Press Enter to continue")
    
age = int(input("Enter your age: "))

if age >= 21:
    print("You are an adult.")
else:
    print("You are a minor.")
    
    
score = int(input("Enter your test score (0-100): "))

if score == 100:
    print("Grade = A")
    print("Perfect score! Outstanding performance!")
elif score >= 90:
    print("Grade = A")
elif score >= 80:
    print("Grade = B")
elif score >= 70:
    print("Grade = C")
elif score >= 60:
    print("Grade = D")
else:
    print("Grade = F")
    

    
temp = float(input("Enter the temperature (°C): "))
raining = input("Is it raining? (yes/no): ").strip().lower()

if temp < 0 and raining == "yes":
    print("Warning: Freezing and wet conditions! Risk of ice.")
elif temp < 0 or temp > 35:
    print("Warning: Extreme temperature!")
else:
    print("Temperature is normal.")
    
    
input("Press Enter to continue")


user = input("Enter username: ")
password = input("Enter password: ")

if user == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")
    
input("Press Enter to continue")

user = input("Enter username: ")
password = input("Enter password: ")

if user == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Wrong password.")
elif user == "student":
    if password == "pass":
        print("Access granted.")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")
    
    
input("Press Enter to continue")

age = int(input("Enter your age: "))
price = 0

if age < 5:
    price = 0
elif age <= 12:
    price = 8
elif age <= 64:
    price = 12
else:
    price = 6

if age >= 13:
    student = input("Are you a student? (yes/no): ").strip().lower()
    if student == "yes":
        price -= 2

price = max(price, 0)

print(f"Ticket price: ${price}")