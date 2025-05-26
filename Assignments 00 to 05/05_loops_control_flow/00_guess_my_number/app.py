import random 


def main():
    attempts = 3
    rd_Number = random.randint(1, 10)
    print("I am thinking of a number between 1 to 10")
    print("You have 3 attempts to win the game")

    while attempts > 0:
        guess = int(input("Enter a guess. "))
        if guess == rd_Number:
            print(f"Congratulations! You guessed it right. The number was {rd_Number}.")
            break 
        elif guess > rd_Number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        
        attempts -= 1
        print(f"Attempts {attempts}")
        
        if attempts == 0:
            print(f"you are lost! the right number is {rd_Number}")




if __name__ == '__main__':
    main()