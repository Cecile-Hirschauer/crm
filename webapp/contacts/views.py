from django.shortcuts import render, redirect
from api.crm import get_all_users, User


def index(request):
    return render(request, 'contacts/index.html', {'users': get_all_users()})


def add_contact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone_number = request.POST.get('phone_number')
    address = request.POST.get('address')

    new_contact = User(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address)
    new_contact.save()

    return redirect('index')


def delete_contact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    contact_to_delete = User(first_name=first_name, last_name=last_name)
    contact_to_delete.delete()
    return redirect('index')
