def main():
    feet: float = input("Enter feet to convert inches: ")
    feet = float(feet)
    inches: float = feet * 12
    print(f"{feet} feet is {inches} inches")

if __name__ == '__main__':
    main()