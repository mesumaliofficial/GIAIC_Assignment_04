def main():
    num1: str = str(input("Enter first number: "))
    num2: str = str(input("Enter second number: "))
    num1 = int(num1)
    num2 = int(num2)
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
    return result
main()
