from datetime import datetime

class User:
    def __init__(self, name=None, phone=None, email=None):
        self.__id = datetime.now().timestamp()
        self.__name = name
        self.__phone = phone
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"ID: {self.get_id()}, Name: {self.get_name()}, Phone: {self.get_phone()}, Email: {self.get_email()}"

dbase = []

def new_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    user = User(name, phone, email)
    dbase.append(user)
    print(f"User  {name} added with ID {user.get_id()}")

def user_id():
    user_id = float(input("Enter user ID: "))
    for user in dbase:
        if user.get_id() == user_id:
            print(user)
            return
    print("User  not found.")

def all_users():
    if not dbase:
        print("No users found.")
        return
    for user in sorted(dbase, key=lambda x: x.get_name()):
        print(user)

def del_user():
    user_id = float(input("Enter user ID to delete: "))
    global dbase
    dbase = [user for user in dbase if user.get_id() != user_id]
    print(f"User  with ID {user_id} deleted.")

def run():
    while True:
        command = input("Enter command (new_user, user_id, all, del_user, exit): ").strip()
        if command == "new_user":
            new_user()
        elif command == "user_id":
            user_id()
        elif command == "all":
            all_users()
        elif command == "del_user":
            del_user()
        elif command == "exit":
            print("Exiting program.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    run()