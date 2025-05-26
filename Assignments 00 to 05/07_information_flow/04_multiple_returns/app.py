def get_user_data():
    first_name = input("Enter Your First Name: ") 
    last_name = input("Enter Your Last Name: ")
    email = input("Enter Your Email Address: ").lower()

    return first_name, last_name, email

def main():
    print(f"Received the following user data: {get_user_data()}")


if __name__ == '__main__':
    main() 