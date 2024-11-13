#Validate username
#1) No more than 12 letters, 2)Must not contain spaces, 3)Must not contain digits

def main():
    while True:
        username = input("Key in your username here: ")

        username_length = len(username)
        username_space = username.count(" ")
        username_letters = username.isalpha()

        if username_length > 12:
            print("Username is invalid. Must have less than 12 characters.")

        elif username_space >=1:
            print("Username is invalid. Must not have any spaces.")

        elif username_letters == False:
            print("Username is invalid. Must not have any digits.") 

        else:
            print(f"Your username is {username}!")


main()

    
