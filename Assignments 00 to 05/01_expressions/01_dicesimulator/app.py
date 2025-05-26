import random as rd


num_sides = 6
def roll_dice():
    die1 = rd.randint(1, num_sides)
    die2 = rd.randint(1, num_sides)
    total = die1 + die2
    print("Die 1:", die1)
    print("Die 2:", die2)
    print("Total of two dice:", total)


def main():
    die1: int = 10
    print("die1 in main() start as:", str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() :", str(die1))
if __name__ == '__main__':
    main()