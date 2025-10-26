contacts = {}
# Decorator to handle input errors
def input_error(func):
    def inner(args, contacts):
        # No command entered
        if args is None:
            return "Please enter a command."
        # check for specific command errors some require one argument, some two
        if func.__name__ in ("add_contact", "change_contact"):
            if len(args) == 0:
                return "Please provide both name and phone number."
            elif len(args) == 1:
                return "Please provide a phone number."
        elif func.__name__ == "show_phone":
            if len(args) == 0:
                return "Please provide a contact name."
        # Handle exceptions from the command functions
        try:
            return func(args, contacts)
        except ValueError:
            return "Invalid input format."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner
# Parses user input into command and arguments
def parse_input(user_input):
    cmd, *args = user_input.split() if user_input.strip() else (None, [])
    if not cmd:
        return None, []
    cmd = cmd.strip().lower()
    return cmd, *args
# Adds a new contact
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

# Changes an existing contact's phone number
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name.lower()] = phone
        return "Contact updated."
    else:
        return "Contact not found."
# Shows a contact's phone number
@input_error
def show_phone(args, contacts):
    name = args[0].lower()
    return contacts.get(name, "Contact not found.")

# Shows all contacts
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name.capitalize()}: {phone}")
    return "\n".join(result)
# Main function to run the assistant bot
def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
