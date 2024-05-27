# CRM Project

## Overview

This project is a basic Customer Relationship Management (CRM) system that allows users to store and manage contact information such as names, addresses, and phone numbers. It serves as an address book and is designed to demonstrate the fundamental aspects of a professional Python project.

## Features

- **User Management**: Add, delete, and query user details.
- **Validation**: Ensure the correctness of user data (e.g., valid phone numbers, proper names).
- **Database**: Store user data using TinyDB.
- **Web Application**: Interactive web interface using Django.
- **Bootstrap**: Responsive design with Bootstrap.


## Getting Started

### Prerequisites

- Python 3.10
- Django 5.0.6
- Faker
- TinyDB
- pytest
- Virtual Environment (optional but recommended)

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/Cecile-Hirschauer/crm.git
    cd crm
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

To run the project, use Django's development server:

```sh
python manage.py runserver
```

## Usage
The project includes several functionalities, such as adding a user, deleting a user, and fetching user details. Here are some examples:

### Add a User:

- Fill out the form on the homepage and click "Ajouter".
Delete a User:

- Click the "Supprimer" button on the respective user card.

### List All Users:
- All users are displayed on the homepage.

## Code Documentation
### User Class
The User class handles all operations related to user management.

**Attributes:**

- `first_name (str)`: The first name of the user.
- `last_name (str)`: The last name of the user.
- `phone_number (str)`: The phone number of the user.
- `address (str):` The address of the user.

**Methods:**

- `full_name`: Returns the full name of the user.
- `db_instance`: Returns the database instance of the user.
- `exists`: Checks if the user exists in the database.
- `delete`: Deletes the user from the database.
- `save`: Saves the user to the database.

### Views
**Index View (index)**:
* Renders the index page with a list of all contacts.
* Uses the `get_all_users` function to retrieve user data and passes it to the template.

**Add Contact View (add_contact):**

* Handles the submission of the form to add a new contact.
* Extracts the first name, last name, phone number, and address from the POST request.
* Creates and saves a new User instance with the provided data.
* Redirects to the index page after successfully adding the contact.

**Delete Contact View (delete_contact):**
* Handles the submission of the form to delete a contact.
* Extracts the first name and last name from the POST request to identify the contact to delete.
* Creates a User instance representing the contact and deletes it from the database.
* Redirects to the index page after successfully deleting the contact.

### Templates
**Index Template (index.html):**

- Displays a list of users and their details using Bootstrap cards.
- Includes a form to add a new contact.
- Each user card has a delete button to remove the contact.