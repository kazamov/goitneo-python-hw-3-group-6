from address_book import AddressBook
from commands import COMMANDS_MAP


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    address_book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command_name, *args = parse_input(user_input)

        command_object = None
        for keys, handler in COMMANDS_MAP.items():
            if command_name in keys:
                command_object = handler
                break

        if command_object:
            if not command_object.validate(args):
                continue

            print(f"\n{command_object.execute(address_book, args)}\n")

            if command_object.is_final:
                break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
