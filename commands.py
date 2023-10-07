from address_book.address_book import AddressBook, Record


def input_error(func):
    def inner(address_book: AddressBook, args):
        try:
            return func(address_book, args)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact is not found."
        except IndexError:
            return "Give me name please."

    return inner


@input_error
def hello_command_handler(*_):
    return "How can I help you?"


@input_error
def add_contact_handler(address_book: AddressBook, args):
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
    name, prev_phone, new_phone = args

    record = address_book.find(name)
    if record:
        record.edit_phone(prev_phone, new_phone)
        return "Contact updated."
    else:
        return "Contact is not found."


@input_error
def show_phones_handler(address_book: AddressBook, args):
    name = args[0]

    record = address_book.find(name)
    if record:
        return str(record)
    else:
        return "Contact is not found."


@input_error
def show_all_handler(address_book: AddressBook, _):
    return str(address_book)


COMMANDS = {
    hello_command_handler: ("hello",),
    add_contact_handler: ("add",),
    change_contact_handler: ("change",),
    show_phones_handler: ("phones",),
    show_all_handler: ("all",),
}
