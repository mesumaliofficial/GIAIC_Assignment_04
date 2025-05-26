def is_odd():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")



def main():
    is_odd()


if __name__ == '__main__':
    main()