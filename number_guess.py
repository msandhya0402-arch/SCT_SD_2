import random

print("🎮 Number Guessing Game 🎮")

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("🎉 Correct! You guessed the number.")
elif guess < number:
    print("📉 Too low! The number was", number)
else:
    print("📈 Too high! The number was", number)
