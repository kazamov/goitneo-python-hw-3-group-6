from collections import UserDict, defaultdict
from datetime import datetime, timedelta

from fields import Name, Phone, Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = None
        self.phones: list[Phone] = []

    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

        if self.birthday:
            result += f", birthday: {self.birthday.value}"

        return result

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

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)


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

    def get_birthdays_per_week(self):
        user_records = self.data.values()

        if len(user_records) == 0:
            return "No users found."

        birthdays_list = defaultdict(list)
        current_date = datetime.now().date()

        for record in user_records:
            name = record.name.value
            birthday = record.birthday.value

            if not birthday:
                continue

            birthday_this_year = birthday.replace(year=current_date.year)

            if birthday_this_year < current_date:
                birthday_this_year = birthday_this_year.replace(
                    year=current_date.year + 1
                )

            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            delta_days = (birthday_this_year - current_date).days
            if delta_days > 0 and delta_days <= 7:
                birthdays_list[birthday_this_year].append(name)

        if len(birthdays_list) == 0:
            return "No birthdays near 7 days."

        sorted_birthdays_list = sorted(birthdays_list.keys())

        result = ""
        for day in sorted_birthdays_list:
            result += f"{day.strftime('%A')}: {', '.join(birthdays_list[day])}\n"

        return result
