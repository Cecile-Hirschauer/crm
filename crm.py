import re
import string
from typing import List

from tinydb import TinyDB, where, table
from pathlib import Path


class User:
    """
    A class to represent a user.

    Attributes:
    ----------
    first_name : str
        The first name of the user.
    last_name : str
        The last name of the user.
    phone_number : str
        The phone number of the user.
    address : str
        The address of the user.

    Methods:
    -------
    full_name:
        Returns the full name of the user.
    db_instance:
        Returns the database instance of the user.
    exists:
        Checks if the user exists in the database.
    delete:
        Deletes the user from the database.
    save:
        Saves the user to the database.
    """

    # Initialize the TinyDB database
    DB = TinyDB(Path(__file__).parent / 'db.json', indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        """
        Constructs all the necessary attributes for the user object.

        Parameters:
        ----------
        first_name : str
            The first name of the user.
        last_name : str
            The last name of the user.
        phone_number : str, optional
            The phone number of the user (default is "").
        address : str, optional
            The address of the user (default is "").
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        """
        Returns a string representation of the user.
        """
        return f"User({self.first_name}, {self.last_name})"

    def __str__(self):
        """
        Returns a user-readable string representation of the user.
        """
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self):
        """
        Returns the full name of the user.

        Returns:
        -------
        str
            Full name of the user.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        """
        Returns the database instance of the user.

        Returns:
        -------
        tinydb.table.Document
            The database document of the user.
        """
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))

    def _check_phone_number(self):
        """
        Checks if the phone number is valid. Raises a ValueError if invalid.
        """
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Invalid phone number {self.phone_number}.")

    def _check_names(self):
        """
        Checks if the first name and last name are valid. Raises a ValueError if invalid.
        """
        if not self.first_name and not self.last_name:
            raise ValueError("Please enter both first_name and last_name.")

        special_characters = string.punctuation + string.digits

        for char in self.first_name + self.last_name:
            if char in special_characters:
                raise ValueError(f"Invalid characters {self.full_name}.")

    def _checks(self):
        """
        Runs all checks for the user data.
        """
        self._check_names()
        self._check_phone_number()

    def exists(self) -> bool:
        """
        Checks if the user exists in the database.

        Returns:
        -------
        bool
            True if the user exists, False otherwise.
        """
        return bool(self.db_instance)

    def delete(self) -> List[int]:
        """
        Deletes the user from the database.

        Returns:
        -------
        List[int]
            List of document IDs removed.
        """
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

    def save(self, validate_data: bool = False) -> int:
        """
        Saves the user to the database.

        Parameters:
        ----------
        validate_data : bool, optional
            Whether to validate data before saving (default is False).

        Returns:
        -------
        int
            The document ID of the inserted record, or -1 if the user already exists.
        """
        if validate_data:
            self._checks()

        if self.exists():
            return -1
        else:
            return User.DB.insert(self.__dict__)


def get_all_users() -> List[User]:
    """
    Retrieves all users from the database.

    Returns:
    -------
    List[User]
        List of all users.
    """
    return [User(**user) for user in User.DB.all()]


if __name__ == '__main__':
    julie = User("Julie", "Courtois")
    print(julie.delete())
