def main():
    c: int = 299792458
    mass_in_kg: float = float(input("Enter mass in kg: "))
    energy: float = mass_in_kg * c**2

    print("e = m * c^2...")
    print("m = ", mass_in_kg, "kg")
    print("c = ", c, "m/s")

    print(f"Energy in joules: {energy}")


if __name__ == '__main__':
    main()