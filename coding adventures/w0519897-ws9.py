# Step 1: Define the functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # We already check before calling this, but just in case:
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Step 2–4: Main calculator loop
while True:
    # Ask user for input
    num1 = input("Enter the first number (or type 'exit' to quit): ")
    if num1.lower() == "exit":
        print("Goodbye! 👋")
        break

    num2 = input("Enter the second number: ")
    operation = input("Enter operation (+, -, *, /): ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        continue

    # Step 3: Use conditionals to call the correct function
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        if num2 == 0:
            result = "❌ Error: Division by zero is not allowed."
        else:
            result = divide(num1, num2)
    else:
        print("❌ Invalid operation. Please choose +, -, *, or /.")
        continue

    # Step 4: Print result (rounded if it's a number)
    if isinstance(result, (int, float)):
        print("✅ Result:", round(result, 2))
    else:
        print(result)