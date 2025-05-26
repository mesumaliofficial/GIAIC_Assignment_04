# Problem => 1
fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
print(len(fruit_list))
fruit_list.append('mango')
print(fruit_list)


# Problem => 2
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'Invalid index'

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return 'Invalid index'
    
def slicing_element(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return 'Invalid index'


def main():
    my_list = ['baraApple', 'chotaApple', 'fatherApple', 'motherApple', 'broApple']
    print(f"Original List: {my_list}")

    while True:
        print("\nChoose an operation: access / modify / slice / exit")
        choice = input("Enter your choice: ").lower()


        if choice == 'access':
            index = int(input("select the index you want to access: "))
            result = access_element(my_list, index)
            print(result)


        elif choice == 'modify':
            index = int(input("select the index you want to modify: "))
            new_value = input("Enter a new value: ")
            result = modify_element(my_list, index, new_value)
            print(result)


        elif choice == 'slice':
            first_index = int(input("Enter a start index: "))
            end_index = int(input("Enter a end index: "))
            result = slicing_element(my_list, first_index, end_index)
            print(result)

        elif choice == 'exit':
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
