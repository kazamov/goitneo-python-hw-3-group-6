from address_book import AddressBook, Record
from errors import InvalidCommandError, InvalidValueFieldError


def input_error(func):
    def inner(self, address_book: AddressBook, args):
        try:
            return func(self, address_book, args)

        except InvalidCommandError as e:
            return e.message
        except InvalidValueFieldError as e:
            return e.message

    return inner


class Command:
    def __init__(
        self, name: str, description: str, alias: str = None, is_final: bool = False
    ):
        self.name = name
        self.description = description
        self.alias = alias
        self.is_final = is_final

    def __str__(self):
        return f"{self.name} - {self.description}"

    def validate(self, args):
        return True

    def execute(self, address_book: AddressBook, args):
        pass


class HelloCommand(Command):
    def __init__(self):
        super().__init__("hello", "Show greeting message.")

    def execute(self, *_):
        return "How can I help you?"


class AddContactCommand(Command):
    def __init__(self):
        super().__init__(
            "add",
            "Add a new contact. Format: add <name> <phone>",
        )

    def validate(self, args):
        if len(args) != 2:
            raise InvalidCommandError(self.name, "Name and phone are required.")

        return True

    @input_error
    def execute(self, address_book: AddressBook, args):
        name, phone = args

        record = address_book.find(name)
        if record:
            record.add_phone(phone)
            return "Contact updated."

        record = Record(name)
        record.add_phone(phone)

        address_book.add_record(record)

        return "Contact added."


class ChangeContactCommand(Command):
    def __init__(self):
        super().__init__(
            "change",
            "Change a phone number of a contact. Format: change <name> <prev_phone> <new_phone>",
        )

    def validate(self, args):
        if len(args) != 3:
            raise InvalidCommandError(
                self.name, "Name, previous phone and new phone are required."
            )

        return True

    @input_error
    def execute(self, address_book: AddressBook, args):
        name, prev_phone, new_phone = args

        record = address_book.find(name)
        if record:
            record.edit_phone(prev_phone, new_phone)
            return "Contact updated."
        else:
            return "Contact is not found."


class DeleteContactCommand(Command):
    def __init__(self):
        super().__init__(
            "delete",
            "Delete a phone number of a contact. Format: delete <name> <phone>",
        )

    def validate(self, args):
        if len(args) != 2:
            raise InvalidCommandError(self.name, "Name and phone are required.")

        return True

    @input_error
    def execute(self, address_book: AddressBook, args):
        name, phone = args

        record = address_book.find(name)
        if record:
            record.delete_phone(phone)
            return "Contact updated."
        else:
            return "Contact is not found."


class ShowPhonesCommand(Command):
    def __init__(self):
        super().__init__(
            "phones",
            "Show all phones of a contact. Format: phones <name>",
        )

    def validate(self, args):
        if len(args) != 1:
            raise InvalidCommandError(self.name, "Name is required.")

        return True

    @input_error
    def execute(self, address_book: AddressBook, args):
        name = args[0]

        record = address_book.find(name)
        if record:
            return str(record)
        else:
            return "Contact is not found."


class ShowAllContactsCommand(Command):
    def __init__(self):
        super().__init__("all", "Show all contacts.")

    def execute(self, address_book: AddressBook, _):
        return str(address_book)


class AddBirthdayCommand(Command):
    def __init__(self):
        super().__init__(
            "add-birthday",
            "Add a birthday to a contact. Format: add-birthday <name> <birthday>",
        )

    def validate(self, args):
        if len(args) != 2:
            raise InvalidCommandError(self.name, "Name and birthday are required.")

        return True

    @input_error
    def execute(self, address_book: AddressBook, args):
        name, birthday = args

        record = address_book.find(name)
        if record:
            record.add_birthday(birthday)
            return "Birthday added."
        else:
            return "Contact is not found."


class ShowBirthdayCommand(Command):
    def __init__(self):
        super().__init__(
            "show-birthday",
            "Show a birthday of a contact. Format: show-birthday <name>",
        )

    def validate(self, args):
        if len(args) != 1:
            raise InvalidCommandError(self.name, "Name is required.")

        return True

    @input_error
    def execute(self, address_book: AddressBook, args):
        name = args[0]

        record = address_book.find(name)
        if record:
            return str(record.birthday)
        else:
            return "Contact is not found."


class ShowBirthdaysCommand(Command):
    def __init__(self):
        super().__init__("birthdays", "Show all birthdays per week.")

    def execute(self, address_book: AddressBook, _):
        return address_book.get_birthdays_per_week()


class ExitCommand(Command):
    def __init__(self):
        super().__init__("exit", "Exit the program.", alias="close", is_final=True)

    def execute(self, *_):
        return "Good bye!"


class HelpCommand(Command):
    def __init__(self):
        super().__init__("help", "Show all available commands.")

    def execute(self, *_):
        return "\n".join(str(c) for c in COMMANDS)


COMMANDS = [
    HelloCommand(),
    AddContactCommand(),
    ChangeContactCommand(),
    DeleteContactCommand(),
    ShowPhonesCommand(),
    ShowAllContactsCommand(),
    AddBirthdayCommand(),
    ShowBirthdayCommand(),
    ShowBirthdaysCommand(),
    ExitCommand(),
    HelpCommand(),
]

COMMANDS_MAP = {(c.name, c.alias): c for c in COMMANDS}
