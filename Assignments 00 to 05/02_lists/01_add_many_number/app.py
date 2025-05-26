def list_of_numbers()-> int:

    number_list = [1, 2, 3, 4, 5]
    total = 0
    for number in number_list:
        total += number
    return total

def main():
    print("total of numbers is: ", list_of_numbers())


if __name__ == '__main__':
    main()