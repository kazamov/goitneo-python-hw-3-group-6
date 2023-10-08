from address_book import AddressBook, Record
from errors import InvalidCommandError, InvalidValueFieldError


def input_error(func):
    def inner(address_book: AddressBook, args):
        try:
            return func(address_book, args)

        except InvalidCommandError as e:
            return e.message
        except InvalidValueFieldError as e:
            return e.message

    return inner


@input_error
def hello_command_handler(*_):
    return "How can I help you?"


@input_error
def add_contact_handler(address_book: AddressBook, args):
    if len(args) != 2:
        raise InvalidCommandError("add", "Name and phone are required.")

    name, phone = args

    record = address_book.find(name)
    if record:
        record.add_phone(phone)
        return "Contact updated."

    record = Record(name)
    record.add_phone(phone)

    address_book.add_record(record)

    return "Contact added."


@input_error
def change_contact_handler(address_book: AddressBook, args):
    if len(args) != 3:
        raise InvalidCommandError(
            "change", "Name, previous phone and new phone are required."
        )

    name, prev_phone, new_phone = args

    record = address_book.find(name)
    if record:
        record.edit_phone(prev_phone, new_phone)
        return "Contact updated."
    else:
        return "Contact is not found."


@input_error
def delete_contact_handler(address_book: AddressBook, args):
    if len(args) != 2:
        raise InvalidCommandError("delete", "Name and phone are required.")

    name, phone = args

    record = address_book.find(name)
    if record:
        record.delete_phone(phone)
        return "Contact updated."
    else:
        return "Contact is not found."


@input_error
def show_phones_handler(address_book: AddressBook, args):
    if len(args) != 1:
        raise InvalidCommandError("phones", "Name is required.")

    name = args[0]

    record = address_book.find(name)
    if record:
        return str(record)
    else:
        return "Contact is not found."


@input_error
def show_all_handler(address_book: AddressBook, _):
    return str(address_book)


@input_error
def add_birthday_handler(address_book: AddressBook, args):
    if len(args) != 2:
        raise InvalidCommandError("add-birthday", "Name and birthday are required.")

    name, birthday = args

    record = address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact is not found."


@input_error
def show_birthday_handler(address_book: AddressBook, args):
    if len(args) != 1:
        raise InvalidCommandError("show-birthday", "Name is required.")

    name = args[0]

    record = address_book.find(name)
    if record:
        return str(record.birthday)
    else:
        return "Contact is not found."


@input_error
def show_birthdays_handler(address_book: AddressBook, _):
    return address_book.get_birthdays_per_week()


COMMANDS = {
    hello_command_handler: ("hello",),
    add_contact_handler: ("add",),
    change_contact_handler: ("change",),
    delete_contact_handler: ("delete",),
    show_phones_handler: ("phones",),
    show_all_handler: ("all",),
    add_birthday_handler: ("add-birthday",),
    show_birthday_handler: ("show-birthday",),
    show_birthdays_handler: ("birthdays",),
}
