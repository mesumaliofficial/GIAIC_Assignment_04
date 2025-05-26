def print_ones_digit(num):
    print(num % 10)



def main():
    num: int = int(input("Enter a number: "))

    print_ones_digit(num)


if __name__ == '__main__':
    main()