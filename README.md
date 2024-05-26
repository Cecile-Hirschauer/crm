# CRM Project

## Overview

This project is a basic Customer Relationship Management (CRM) system that allows users to store and manage contact information such as names, addresses, and phone numbers. It serves as an address book and is designed to demonstrate the fundamental aspects of a professional Python project.

## Features

- **User Management**: Add, delete, and query user details.
- **Validation**: Ensure the correctness of user data (e.g., valid phone numbers, proper names).
- **Database**: Store user data using TinyDB.
- **Command-Line Interface**: Interact with the application via a CLI built with Typer.
- **Object-Oriented Design**: Transition from procedural to object-oriented programming.
- **Web Application**: Expand functionality with a web interface using Django.

## Project Structure

(TODO: Describe the project structure here)

## Getting Started

### Prerequisites

- Python 3.10
- Virtual Environment (optional but recommended)

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/crm_project.git
    cd crm_project
    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Project

To run the project, you can use the CLI commands provided by Typer. For example, to add a new user:

```sh
python -m crm.user add --first-name John --last-name Doe --phone-number 1234567890 --address "123 Elm Street"
```

### Running Tests

Tests are written using `pytest`. To run the tests, execute:

```sh
pytest
```

## Usage

The project includes several functionalities, such as adding a user, deleting a user, and fetching user details. Here are some examples:

- **Add a User**:

    ```sh
    python -m crm.user add --first-name John --last-name Doe --phone-number 1234567890 --address "123 Elm Street"
    ```

- **Delete a User**:

    ```sh
    python -m crm.user delete --first-name John --last-name Doe
    ```

- **List All Users**:

    ```sh
    python -m crm.user list
    ```

## Code Documentation

### User Class

The `User` class handles all operations related to user management.

- **Attributes**:
    - `first_name` (str): The first name of the user.
    - `last_name` (str): The last name of the user.
    - `phone_number` (str): The phone number of the user.
    - `address` (str): The address of the user.

- **Methods**:
    - `full_name`: Returns the full name of the user.
    - `db_instance`: Returns the database instance of the user.
    - `exists`: Checks if the user exists in the database.
    - `delete`: Deletes the user from the database.
    - `save`: Saves the user to the database.

### Example

Here's an example of how to create a user and save it to the database:

```python
from crm import User

# Create a user instance
john = User(first_name="John", last_name="Doe", phone_number="1234567890", address="123 Elm Street")

# Save the user to the database
john.save(validate_data=True)

# Check if the user exists
print(john.exists())

# Get the full name of the user
print(john.full_name)

# Delete the user
john.delete()
```

