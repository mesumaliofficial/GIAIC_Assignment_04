import random as rd

num_sides:int = int(6)

def roll_dice():
    die1:int = rd.randint(1, num_sides)
    die2:int = rd.randint(1, num_sides)

    total = die1 + die2
    print(f"First Die {die1}")
    print(f"Second Die {die2}")
    print(f"Total of both dice: {total}")

def main():
    
    roll_dice()

if __name__ == '__main__':
    main()