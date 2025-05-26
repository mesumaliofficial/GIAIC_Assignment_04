def print_divisor(num):
    for i in range(1, num + 1):
        if num % 2 == 0:
            print(i)

def main():
    num: int = int(input("Enter a number "))
    print_divisor(num)


if __name__ == '__main__':
    main()