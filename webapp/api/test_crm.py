"""
MIT License

Copyright (c) 2024 Cécile Hirschauer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from webapp.api.crm import User
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage
import pytest


@pytest.fixture
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture
def user(setup_db):
    u = User(first_name="Alice",
             last_name="Smith",
             address="1 rue du Peuplier 13150 Belleville",
             phone_number="0123456789")

    u.save()
    return u


def test_first_name(user):
    assert user.first_name == "Alice"


def test_last_name(user):
    assert user.last_name == "Smith"


def test_address(user):
    assert user.address == "1 rue du Peuplier 13150 Belleville"


def test_phone_number(user):
    assert user.phone_number == "0123456789"


def test_full_name(user):
    assert user.full_name == "Alice Smith"


def test_exists(user):
    assert user.exists() is True


def test_not_exists(setup_db):
    u = User(first_name="Bob", last_name="Maurane", address="125 avenue de la république 45001 Plopville",
             phone_number="0123456789")
    assert u.exists() is False


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "Alice"
    assert user.db_instance["last_name"] == "Smith"
    assert user.db_instance["address"] == "1 rue du Peuplier 13150 Belleville"
    assert user.db_instance["phone_number"] == "0123456789"


def test_not_db_instance(setup_db):
    u = User(first_name="Bob", last_name="Maurane", address="125 avenue de la république 45001 Plopville",
             phone_number="0123456789")

    assert u.db_instance is None


def test__check_phone_number(setup_db):
    user_good = User(first_name="Patrick", last_name="Martin", phone_number="1230456078",
                     address="9 rue du 8 Mai 88012 Hasard")
    user_bad = User(first_name="Sophie", last_name="Nolan", phone_number="abcd",
                    address="8 place du Marche 55550 Poulain")

    with pytest.raises(ValueError) as err:
        user_bad._check_phone_number()

    assert "Invalid phone number" in str(err.value)

    user_good.save(validate_data=True)
    assert user_good.exists() is True


def test__check_names_empty(setup_db):
    user_bad = User(first_name="", last_name="", phone_number="abcd",
                    address="8 place du Marche 55550 Poulain")

    with pytest.raises(ValueError) as err:
        user_bad._check_names()

    assert "Please enter both first_name and last_name." == str(err.value)


def test__check_names_invalid_characters(setup_db):
    user_bad = User(first_name="!23lop", last_name="To99:::", phone_number="abcd",
                    address="8 place du Marche 55550 Poulain")

    with pytest.raises(ValueError) as err:
        user_bad._check_names()

    assert "Invalid characters" in str(err.value)


def test_delete(setup_db):
    user_test = User(first_name="Patrick", last_name="Martin", phone_number="1230456078",
                     address="9 rue du 8 Mai 88012 Hasard")
    user_test.save()
    first_delete = user_test.delete()
    second_delete = user_test.delete()
    assert len(first_delete) > 0
    assert isinstance(first_delete, list)
    assert len(second_delete) == 0
    assert isinstance(second_delete, list)


def test_save(setup_db):
    user_test = User(first_name="Patrick", last_name="Martin", phone_number="1230456078",
                     address="9 rue du 8 Mai 88012 Hasard")
    user_test_doublon = User(first_name="Patrick", last_name="Martin", phone_number="1230456078",
                             address="9 rue du 8 Mai 88012 Hasard")
    first = user_test.save()
    second = user_test_doublon.save()
    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1
