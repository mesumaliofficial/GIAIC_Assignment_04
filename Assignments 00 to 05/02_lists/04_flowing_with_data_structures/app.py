def make_threee_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    message: str = str(input("Enter a message to copy:  "))
    my_list: list = []
    print(f"Before List =>>>> {my_list}")
    make_threee_copies(my_list, message)
    print(f"After List =>>>> {my_list}")


if __name__ == '__main__':
    main()