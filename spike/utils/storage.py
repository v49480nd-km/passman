import os

def find_pwd(pwd_name: str): # NOT TESTED
    """returns whether a line number exists or not with the password name"""
    if os.path.exists("storage.txt"):
        with open("storage.txt", "r") as file:
            line_number = 0
            current_name = ""

            for line in file:
                current_name = line[0:4]

                if current_name == pwd_name[0:4]:
                    return line_number
                else:
                    return -1
    else:
        print("cannot delete passwords cause they dont exist, go generate them")

def delete_pwd(line_number: int): # NOT TESTED
    """create a copy of the file and copy all except the one line and then rename the files and delete the old one"""
    
    pass

def store_pwd(pwd_name: str, pwd: str): # TESTED AND WORKS
    """store a given password in a certain format obviously"""
    if os.path.exists("storage.txt"):
        with open("storage.txt", "a") as file:
            file.write(f"{pwd_name[0:4]} - {pwd}")
            
    else:
        with open("storage.txt", "w") as file:
            file.write(f"{pwd_name} - {pwd}")

def list_pwds(): # NOT TESTED
    """list passwords and check if file exists before doing so"""
    if os.path.exists("storage.txt"):
        with open("storage.txt", "r") as file:
            print(file.read())
    else:
        print("You have no generated any passwords therefore their is nothing to list. go make a password for this functionality")
