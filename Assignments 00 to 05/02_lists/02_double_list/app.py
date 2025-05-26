def main():
    number_list: list[int] = [1, 2, 3, 4, 5]

    for i in range(len(number_list)):
        index_of_num = number_list[i]
        number_list[i] = index_of_num * 2
        print(f"{index_of_num} {number_list[i]}")

if __name__ == '__main__':
    main()
