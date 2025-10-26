# Завдання 4

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.



# Вимоги до завдання:

# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.


# Рекомендації для виконання:

# В якості прикладу додамо декоратор input_error для обробки помилки ValueError

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Give me name and phone please."

#     return inner



# Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

# @input_error
# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."



# Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.



# Критерії оцінювання:

# Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
# Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
# Кожна функція для обробки команд має декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
# Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.


# Приклад використання:

# При запуску скрипту діалог з ботом повинен бути схожим на цей.

# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356
# Enter a command:

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
