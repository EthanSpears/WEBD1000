import time
count = 10
while count >= 1:
    print(f"Minutes Reamining:", count)
    time.sleep(1)
    count -= 1

print("Your Cupcakes Are Done!")

count = 1
while count <= 5:
    print(f"Time To Eat 3 Cupcakes:", count)
    time.sleep(1)
    count += 1

print("3 Cupcakes Have Been Eaten!")

input("Press Enter to continue to the next step")

import random

max_guesses = 5

while True:
    secret = random.randint(1, 10)
    guess = 0
    attempts = 0

    while guess != secret and attempts < max_guesses:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < secret:
            print("Too low! 📉")
        elif guess > secret:
            print("Too high! 📈")
        else:
            score = 5 - attempts
            print(f"You got it! 🎉 Your score is {score} points.")

    if guess != secret:
        print(f"Sorry, you've used all {max_guesses} guesses. The number was {secret}, better luck next time!")

    play_again = input("Play again? (Y/N): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye! 👋")
        break


input("Press Enter to continue to the next step")


import random

sips = 5

while sips > 0:
    print("You take a sip... 🧋")
    sips -= 1
    
    event = random.choice(["none", "boba_pearl", "brain_freeze", "none", "none"])
    if event == "boba_pearl":
        print("You chew on a boba pearl! Yum!")
    elif event == "brain_freeze":
        print("🥶 Uh oh! Brain freeze warning! Slow down!")
    
print("Cup empty. Refill time!")