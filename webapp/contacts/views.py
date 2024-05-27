from django.shortcuts import render
from api.crm import get_all_users


def index(request):
    return render(request, 'contacts/index.html', {'users': get_all_users()})
