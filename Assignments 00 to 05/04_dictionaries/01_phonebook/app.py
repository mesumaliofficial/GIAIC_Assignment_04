def get_info():
    phonebook = {}

    while True:
        name = input("Name: ").lower()
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook

def print_book(phonebook):
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def find_number(phonebook):
    while True:
        user_input = input("Enter a name for finding number: ")
        if user_input == "":
            break
        if user_input in phonebook:
            print(phonebook[user_input])
        else:
            print(f"{user_input} not in PhoneBook.")


def main():
    phone_book = get_info()
    print_book(phone_book)
    find_number(phone_book)

if __name__ == '__main__':
    main()
