import math

def main():
    ab: float = float(input("Enter the value of AB: "))
    ac: float = float(input("Enter the value of AC: "))

    bc = math.sqrt(ab**2 + ac**2)
    print(f"The value of BC is: {bc}")


if __name__ == '__main__':
    main()