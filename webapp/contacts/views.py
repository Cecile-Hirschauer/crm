from django.shortcuts import render, redirect
from api.crm import get_all_users, User


def index(request):
    """
    View to render the index page with a list of all contacts.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponse: The rendered index page with the list of users.
    """
    # Get all users from the database and pass them to the template
    return render(request, 'contacts/index.html', {'users': get_all_users()})


def add_contact(request):
    """
    View to handle adding a new contact.

    Parameters:
    request (HttpRequest): The request object containing POST data.

    Returns:
    HttpResponse: Redirects to the index page after adding the contact.
    """
    # Extract data from POST request
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone_number = request.POST.get('phone_number')
    address = request.POST.get('address')

    # Create a new user instance
    new_contact = User(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address)
    # Save the new user to the database
    new_contact.save()

    # Redirect to the index page to display the updated list of contacts
    return redirect('index')


def delete_contact(request):
    """
    View to handle deleting a contact.

    Parameters:
    request (HttpRequest): The request object containing POST data.

    Returns:
    HttpResponse: Redirects to the index page after deleting the contact.
    """
    # Extract data from POST request to identify the contact to delete
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    # Create a user instance representing the contact to delete
    contact_to_delete = User(first_name=first_name, last_name=last_name)

    # Delete the user from the database
    contact_to_delete.delete()

    # Redirect to the index page to display the updated list of contacts
    return redirect('index')
