def main():
    year: int = int(input("Enter year for checking is leap year or not :"))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} That's a leap year.")
            else: 
                print(f"{year} That's not a leap year.")
        else:
            print(f"{year} That's a leap year.")
    else:
        print(f"{year} That's not a leap year.")

if __name__ == '__main__':
    main()