from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    customer = User.objects.create_user('jodasdsaddddhn', 'lennon@thebeatles.com', 'johnpassword',first_name='John',last_name='Lenon')
    print (customer.first_name,customer.last_name,customer.email)

    return HttpResponse("Test API")
