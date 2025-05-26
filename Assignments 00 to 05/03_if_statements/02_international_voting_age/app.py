Peturksbouipo: int = 16
Stanlau: int = 25
Mayengua: int = 45

def main():
    age: int = int(input("Enter your age: "))

    if age >= Peturksbouipo:
        print(f"You are voting on Peturksbouipo where the voting age is {Peturksbouipo}")
    else:
        print("You are not voting on Peturksbouipo")
    
    if age >= Stanlau:
        print(f"You are voting on Stanlau where the voting age is {Stanlau}")
    else:
        print("You are not voting on Stanlau")

    if age >= Mayengua:
        print(f"You are voting on Mayengua where the voting age is {Mayengua}")
    else:
        print("You are not voting on Mayengua")


if __name__ == '__main__':
    main()
