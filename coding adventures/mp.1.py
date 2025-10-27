def calculate_grade():
    print("Welcome to the Grading Calculator!\n")

    # Get user input
    total_marks = float(input("Enter total possible marks: "))
    obtained_marks = float(input("Enter marks obtained: "))

    # Validate input
    if total_marks <= 0:
        print("\nError: Total marks must be greater than 0!")
        return
    elif obtained_marks < 0:
        print("\nError: Obtained marks cannot be negative!")
        return
    elif obtained_marks > total_marks:
        print("\nError: Obtained marks cannot exceed total possible marks!")
        return

    # Calculate percentage
    percentage = (obtained_marks / total_marks) * 100

    # Determine letter grade
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Determine pass/fail and special perfect score message
    if obtained_marks == total_marks:
        status = "🎉 Perfect Score! Outstanding performance! 🎉"
    elif grade == 'F':
        status = "You failed. Better luck next time!"
    else:
        status = "Congratulations! You passed!"

    # Show results
    print("\n--- Results ---")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(status)

# Run the calculator
calculate_grade()