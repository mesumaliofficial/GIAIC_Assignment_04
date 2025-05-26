def main():
    max_num = 10000
    a = 0
    b = 1

    while a <= max_num:
        print(a, end=" ")
        c = a + b
        a = b
        b = c

if __name__ == '__main__':
    main()