#from django.shortcuts import render
#
#def home(request):
#    return render(request, 'base.html')

#from django.shortcuts import render
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):

#    return render(request, 'my_app/new_search.html')
#

#from django.shortcuts import render
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    print(search)
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)

import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {'search':search,}
    return render(request, 'my_app/new_search.html', stuff_for_frontend)

