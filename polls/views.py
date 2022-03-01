

from urllib import response

from django.shortcuts import render

from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required





def index():

    return HttpResponse("Hello, world. You're at the polls index.")
'''
@login_required(login_url='login')
def users(request):

    response = requests.get('https://jsonplaceholder.typicode.com/todos/')

    todos = response.json()
    print(todos)

    return render(request, "main_app/home.html", {"todos": todos})

def login(request):

    return render(request, "main_app/login.html")
'''


