def count_even():
    lst = []
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":
            break
        num = int(user_input)
        if num % 2 == 0:
            lst.append(user_input)
    print("Even numbers entered:", lst)
    print("Total count of even numbers:", len(lst))


def main():
    count_even()

if __name__ == '__main__':
    main()