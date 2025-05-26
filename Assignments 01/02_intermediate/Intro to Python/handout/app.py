
def main():

    earth_weight: float = float(input("Enter your weight on Earth: "))

    planet = input("Enter the planet you want to check your weight on ( Mars, Jupiter): ").capitalize()

    gravity_multipliers = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
    }

    if planet in gravity_multipliers:
        constant_weight = earth_weight * gravity_multipliers[planet]
        print(f"Your weight on {planet} is {round(constant_weight, 2)}")

if __name__ == "__main__":
    main()