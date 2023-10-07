class InvalidFieldType(Exception):
    pass


class InvalidNameError(Exception):
    pass


class InvalidPhoneLengthError(Exception):
    pass


class InvalidPhoneFormatError(Exception):
    pass


class Field:
    _value = None

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value


class Name(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        if type(value) != str:
            raise InvalidFieldType("name")
        elif len(value) == 0:
            raise InvalidNameError
        self._value = value


class Phone(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        if type(value) != str:
            raise InvalidFieldType("phone")
        elif len(value) < 0:
            raise InvalidPhoneLengthError
        elif not value.isdigit():
            raise InvalidPhoneFormatError

        self._value = value


class Birthday(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        if type(value) != str:
            raise InvalidFieldType("birthday")

        self._value = value
