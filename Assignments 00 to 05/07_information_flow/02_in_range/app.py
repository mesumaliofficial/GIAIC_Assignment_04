def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

def main():
    n: int = int(input("Enter a number for checking in the range: "))
    low: int = int(input("Enter Your Lowest value: "))
    high: int = int(input("Enter your Highest value: ")) 

    print(in_range(n, low, high))


if __name__ == '__main__':
    main()