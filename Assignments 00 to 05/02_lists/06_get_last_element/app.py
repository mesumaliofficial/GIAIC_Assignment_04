def get_last_elem(lst):
    print(lst[-1])

def get_list():
    lst = []
    while True:
        elem = str(input("Please enter an element of the list or press enter to stop."))
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_list()
    get_last_elem(lst)


if __name__ == '__main__':
    main()