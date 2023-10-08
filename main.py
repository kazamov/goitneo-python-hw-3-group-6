from address_book import AddressBook
from commands import COMMANDS


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    address_book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        command_handler = None
        for handler, keys in COMMANDS.items():
            if command in keys:
                command_handler = handler
                break

        if command_handler:
            print(command_handler(address_book, args))
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
