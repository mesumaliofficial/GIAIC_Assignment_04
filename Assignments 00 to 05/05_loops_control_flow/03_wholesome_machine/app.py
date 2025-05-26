def main():
    Affirmation = "I am capable of doing anything I put my mind to.".lower()
    print(f"Please type the following affirmation {Affirmation}")
    
    user_input = input("").lower()
    while user_input != Affirmation:
        user_input = input("").lower()
        if user_input == Affirmation:
            print("That's right!")
            break
        else:
            print("That was not the affirmation.")
            print(f"Please type the following affirmation {Affirmation}")

if __name__ == '__main__':
    main()