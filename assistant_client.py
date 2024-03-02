from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def is_valid(self):
        if len(self.value) == 10 and str(self.value).isdigit():
            return True
        return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        p = Phone(phone)
        if p.is_valid():
            self.phones.append(p)

    def remove_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                self.phones.remove(el)

    def edit_phone(self, old_number, new_number):
        phones = [p.value for p in self.phones]
        if old_number in phones:
            self.remove_phone(old_number)
            self.add_phone(new_number)

    def find_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            return phone
        return "Number not found"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, value):
        return self.data.get(value, "Contact not found")

    def delete(self, value):
        self.data.pop(value, None)
