max_length: int = 3

def shorten(lst):
    while len(lst) > max_length:
        last_elem = lst.pop()
        print(f"last removing elements: {last_elem}")

def get_list():
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop. ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_list()
    shorten(lst)

if __name__ == '__main__':
    main()