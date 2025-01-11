import time

def start_message():
    msg_list = ["password manager", "[1] generate password", "[2] list passwords", "[3] delete password"]
    
    for msg in msg_list:
        print(msg)
        time.sleep(0.5)

def main():
    start_message()
    user_option = input("> ")

    match int(user_option):
        case 1:
            """generates a password aswell as gets a name and what not"""
            print("generating password")
        case 2:
            """if passwords exist, list them, if not tell the user to go and generate some"""
            print("listing passwords")
        case 3:
            """lists passwords like prior option and asks whichone to delete based on lines"""
            print("delete a password")
        case _:
            """exits program and tells user how to fix issue"""
            print("not an option, please use the options listed above or use passman -h")

if __name__ == "__main__":
    main()