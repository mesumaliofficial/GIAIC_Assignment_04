def main():
    side_1 = float(input("Enter the length of side 1: "))
    side_2 = float(input("Enter the length of side 2: "))
    side_3 = float(input("Enter the length of side 3: "))
    
    perimeter = side_1 + side_2 + side_3
    print(f"The perimeter of the triangle is: {perimeter}")
    

if __name__ == '__main__':
    main()