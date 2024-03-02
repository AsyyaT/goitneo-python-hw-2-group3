def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner


def key_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter valid username."

    return inner


def index_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter username."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact added."


def show_all_contacts(contacts):
    formatted_contacts = []
    for name, phone in contacts.items():
        formatted_contacts.append(f'{name}: {phone}')

    return '\n'.join(formatted_contacts)


@key_error
@index_error
def show_phone(contacts, args):
    username = args[0]
    return contacts[username]


@input_error
def update_phone(contacts, args):
    name, phone = args

    contacts[name] = phone
    return "Contact updated."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command == "phone":
            print(show_phone(contacts, args))
        elif command == "change":
            print(update_phone(contacts, args))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
