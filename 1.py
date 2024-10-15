class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.next_id = 1

    def new_user(self, name, phone, email):
        self.contacts[self.next_id] = {'name': name.strip(), 'phone': phone, 'email': email.strip()}
        print(f"User added with ID: {self.next_id}")
        self.next_id += 1

    def user_id(self, user_id):
        try:
            user_id = int(user_id)
            if user_id in self.contacts:
                contact = self.contacts[user_id]
                print(f"ID: {user_id}, Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print(f"No user with ID: {user_id}")
        except ValueError:
            print("Invalid ID. Please enter a valid number.")

    def user_name(self, name):
        name = name.strip().lower()
        users = [(id, info) for id, info in self.contacts.items() if info['name'].lower() == name]
        if users:
            for id, info in sorted(users, key=lambda x: x[1]['name']):
                print(f"ID: {id}, Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print(f"No user with name: {name}")

    def all_users(self):
        if self.contacts:
            for id, info in sorted(self.contacts.items(), key=lambda x: x[1]['name']):
                print(f"ID: {id}, Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print("No contacts available.")

    def del_user(self, ids):
        deleted = []
        not_found = []

        try:
            if '-' in ids:
                start, end = map(int, ids.split('-'))
                for id in range(start, end + 1):
                    if id in self.contacts:
                        del self.contacts[id]
                        deleted.append(id)
                    else:
                        not_found.append(id)
            elif ',' in ids:
                ids_list = map(int, ids.split(','))
                for id in ids_list:
                    if id in self.contacts:
                        del self.contacts[id]
                        deleted.append(id)
                    else:
                        not_found.append(id)
            else:
                id = int(ids)
                if id in self.contacts:
                    del self.contacts[id]
                    deleted.append(id)
                else:
                    not_found.append(id)

            print(f"Deleted IDs: {deleted}" if deleted else "No users deleted.")
            if not_found:
                print(f"IDs not found: {not_found}")
        except ValueError:
            print("Invalid input. Please provide valid IDs or ranges.")

    def exit_program(self):
        print("Exiting the program.")
        raise SystemExit

def main():
    contact_book = ContactBook()
    while True:
        command = input("Enter command: ").strip().lower()
        if command == 'new_user':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.new_user(name, phone, email)
        elif command.startswith('user '):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                contact_book.user_id(parts[1])
            else:
                print("Invalid command. Usage: user <ID>")
        elif command.startswith('user_name '):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                contact_book.user_name(parts[1])
            else:
                print("Invalid command. Usage: user_name <name>")
        elif command == 'all':
            contact_book.all_users()
        elif command.startswith('del_user '):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                contact_book.del_user(parts[1])
            else:
                print("Invalid command. Usage: del_user <ID(s)>")
        elif command == 'exit':
            contact_book.exit_program()
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
