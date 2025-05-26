def get_number():
    user_numbers = []

    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break

        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_num(numbers):
    user_dict = {}

    for num in numbers:
        if num in user_dict:
            user_dict[num] += 1
        else:
            user_dict[num] = 1
    return user_dict

def main():
    numbers = get_number()
    result = count_num(numbers)
    
    for num, count in result.items():
        print(f"{num} appears {count} times.")

if __name__ == '__main__':
    main()
