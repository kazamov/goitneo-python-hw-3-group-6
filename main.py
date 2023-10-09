from address_book import AddressBook
from commands import COMMANDS_MAP, get_command
from pickle import dump, load
from pathlib import Path


ADDRESS_BOOK_FILE = "cache/address_book.pickle"


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def save_address_book(address_book):
    Path("cache").mkdir(exist_ok=True)
    with open(ADDRESS_BOOK_FILE, "wb") as f:
        dump(address_book, f)


def load_address_book():
    try:
        with open(ADDRESS_BOOK_FILE, "rb") as f:
            return load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    address_book = load_address_book()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command_name, *args = parse_input(user_input)

        command_object = get_command(command_name)

        if command_object:
            if not command_object.validate(args):
                continue

            print(f"\n{command_object.execute(address_book, args)}\n")

            if command_object.is_final:
                save_address_book(address_book)
                break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
