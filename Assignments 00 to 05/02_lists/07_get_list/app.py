def main():
    lst = []
    while True:
        value = input("Enter a Value. ")
        if value == "":
            break
        lst.append(value)
    print(f"Here's the list {lst}")

if __name__ == '__main__':
    main()