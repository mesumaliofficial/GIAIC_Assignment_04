def main():
    farenheit: str = str(input("Enter temperature in Fahrenheit: "))
    farenheit = float(farenheit)
    celsius: float = (farenheit - 32) * 5.0 / 9.0  
    print(f"Temperature in Celsius: {celsius:.2f}")  

if __name__ == '__main__':
    main()