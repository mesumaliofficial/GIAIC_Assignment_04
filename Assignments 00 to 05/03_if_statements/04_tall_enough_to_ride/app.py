minimum_height:int = 50

def main():
    while True:
        height = input("How tall are you ? ")

        if height == "":
            break

        height = int(height)
        
        if height >= minimum_height:
            print("You're tall enough to ride!")
        else:
            print("ou're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()