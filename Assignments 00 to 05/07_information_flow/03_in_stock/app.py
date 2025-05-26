def num_in_stock(fruit):

    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        return 0

def main():
    fruit = input("Enter a Fruit: ").lower()
    print(num_in_stock(fruit))


if __name__ == '__main__':
    main()