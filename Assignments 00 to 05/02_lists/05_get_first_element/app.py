def get_first_elem(lst):
    print(lst[0])

def get_list():
    lst = []
    while True:
        elem: str = input("Please enter an element of the list or press enter to stop. ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_list()
    get_first_elem(lst)


if __name__ == '__main__':
    main()
