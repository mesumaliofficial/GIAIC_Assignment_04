import random

NUM_ROUNDS = 5
score = 0
current_round = 0

def main():
    global score
    global current_round    
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    for i in range(NUM_ROUNDS):

        comp_num = random.randint(1, 100)
        your_num = random.randint(1, 100)

        current_round += 1 
        print(f"\nRound => {current_round}")
        print(f"Your num is {your_num}")    

        while True:
            check = input("Do you think your number is higher or lower than the computer's?\n").lower()

            if check == 'lower' or check == 'higher':
                if check == 'higher' and your_num > comp_num:
                    print(f"You were right! The computer's number was {comp_num}")
                    score += 1
                    print(f"Your Score is now {score}")
                    break
                    
                elif check == 'lower' and your_num < comp_num:
                    print(f"You were right! The computer's number was {comp_num}")
                    score += 1
                    print(f"Your Score is now {score}")
                    break
                
                else:
                    print(f"Aww, that's incorrect. The computer's number was {comp_num}")
                    print(f"Your Score is now {score}")
                    break
            else:
                print("Invalid Input! please enter 'higher' and 'lower' ")

    print("\n\nFinal Result of your 5 round!")
    print(f"Your score is {score}")
    if score == 5:
        print("Wow! You played perfectly!")
    elif score == 3:
        print("Good job, you played really well!")
    else:
        print("better luck next time!")


if __name__ == "__main__":

    main()
