def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if my_list[mid] == target:
            return mid
        elif my_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def main():
    print("=== Binary Search Project ===")
    arr = input("Sorted numbers daalo (space separated): ").strip().split()
    arr = [int(x) for x in arr]
    target = int(input("Search karne wala number daalo: "))
    index = binary_search(arr, target)

    if index != -1:
        print(f"Element {target} list mein index {index + 1} pe mila.")
    else:
        print(f"Element {target} list mein nahi mila.")

if __name__ == "__main__":
    main()