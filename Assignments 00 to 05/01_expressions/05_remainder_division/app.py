def main():
    num1: int = int(input("Please enter an integer to be divided: "))
    num2: int = int(input("Please enter an integer to divide by: "))

    quotient = num1 // num2
    reminder = num1 % num2
    print(f"The result of this division is {quotient} with a remainder of {reminder}")


if __name__ == '__main__':
    main()