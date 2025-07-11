# 🎯 Number Guessing Game

A simple Python-based number guessing game where the computer randomly selects a number between 0 and 100, and the user tries to guess it.

## 🧠 How It Works

- The computer generates a **random number between 0 and 100**.
- You, the user, will guess the number.
- After each guess, the program will give you a hint:
  - `"Lower Number Please"` if your guess is too high.
  - `"Higher Number Please"` if your guess is too low.
- The game continues until you guess the correct number.
- It will then tell you **how many attempts** you took to guess it.

## 📋 Sample Output

```bash
Guess a number between (0 - 100): 50
Lower Number Please
Guess a number between (0 - 100): 25
Higher Number Please
Guess a number between (0 - 100): 32
You have guessed the number 32 correctly in 3 attempts
