from address_book import AddressBook
from commands import get_command


ADDRESS_BOOK_FILENAME = "address_book.pickle"


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    address_book = AddressBook()
    address_book.load(ADDRESS_BOOK_FILENAME)

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command_name, *args = parse_input(user_input)

        command_object = get_command(command_name)

        if command_object:
            print(f"\n{command_object.execute(address_book, args)}\n")

            if command_object.is_final:
                address_book.save(ADDRESS_BOOK_FILENAME)
                break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
