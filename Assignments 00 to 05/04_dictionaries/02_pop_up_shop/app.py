def main():
    fruits = {
        "apple": 10,
        "mango": 20,
        "strawberry": 15,
        "watermelon": 30,
        "delight": 9
    }

    total = 0

    for fruit_name in fruits:
        bought = int(input(f"How many {fruit_name} do you want to buy? "))
        price = fruits[fruit_name]
        total += (price * bought)

    print(f"Your total is ${total}")

if __name__ == '__main__':
    main()
