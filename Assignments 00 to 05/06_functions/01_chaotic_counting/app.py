import random

done_likelihood = 0.3

def done():
    return random.random() < done_likelihood


def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i, end=" ")


def main():
        print("\nkI'm going to count until 10 or until I feel like stopping, whichever comes first.")
        chaotic_counting()
        print("\nI'm done")


if __name__ == '__main__':
    main()