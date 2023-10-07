from collections import UserDict
from fields import Name, Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone_str: str):
        phone = self.find_phone(phone_str)
        if phone:
            self.phones.remove(phone)

    def edit_phone(self, prev_phone: str, next_phone: str):
        phone = self.find_phone(prev_phone)
        if phone:
            phone.value = next_phone

    def find_phone(self, phone_str: str) -> Phone:
        phone = None
        for p in self.phones:
            if p.value == phone_str:
                phone = p
                break
        return phone


class AddressBook(UserDict):
    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.data.values())

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name] if name in self.data else None

    def delete(self, name: str):
        if name in self.data:
            self.data.pop(name)
