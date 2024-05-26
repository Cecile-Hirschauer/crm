import re
import string


class User:
    """
    Class that generates new instances of users
    """
    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        """
        __init__ method that helps us define properties for our objects.
        :param first_name: str
        :param last_name: str
        :param phone_number: str or None
        :param address: str or None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"

    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Invalid phone number {self.phone_number}.")

    def _check_names(self):
        if not self.first_name and not self.last_name:
            raise ValueError("Please enter both first_name and last_name.")

        special_characters = string.punctuation + string.digits

        for char in self.first_name + self.last_name:
            if char in special_characters:
                raise ValueError(f"Invalid character {self.full_name}.")

    def _checks(self):
        self._check_names()
        self._check_phone_number()


if __name__ == '__main__':
    from  faker import Faker
    fake = Faker(locale="fr_FR")
    user = User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        phone_number=Faker().phone_number(),
        address=fake.address(),
    )
    print(user)
    print("-" * 10)
