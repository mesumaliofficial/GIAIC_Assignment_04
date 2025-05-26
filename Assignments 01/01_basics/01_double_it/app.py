def double_it(curr_value):
    while curr_value <= 100:
        curr_value = curr_value * 2
        print(curr_value)




def main():
    curr_value: int = int(input("Enter a number: "))
    double_it(curr_value)


if __name__ == '__main__':
    main()