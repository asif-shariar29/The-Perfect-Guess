import random

n = random.randint(0,100)
a = -1
guesses = 1

while (a != n):
    a = int(input("Guess a number between (0 - 100): "))
    if (a > n):
        print("Lower Number Please")
        guesses += 1
    elif (a < n):
        print("Higher Number Please")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")