def print_multiple(message, repeats):
    for i in range(1, repeats + 1):
        print(f"{i}) {message}")

def main():
    message: str = str(input("Please type a message: "))
    repeats: int = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)


if __name__ == '__main__':
    main()