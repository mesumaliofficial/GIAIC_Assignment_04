import random

def main():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("I am thinking of a number between 1 and 10...")
    print("You have 3 chances")

    while attempts > 0:
        guess = int(input("Enter a guess: "))

        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print("🎉 Congratulations! You win 🥂!")
            return 

        attempts -= 1
        print(f"Remaining chances: {attempts}")

    print(f"❌ Game Over! The correct number was {secret_number}")

if __name__ == '__main__':
    main()
