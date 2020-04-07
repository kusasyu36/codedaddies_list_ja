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

#import requests
#from django.shortcuts import render
#from bs4 import BeautifulSoup
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    print(search)
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#

#
#import requests
#from django.shortcuts import render
#from bs4 import BeautifulSoup
#
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    print(search)
#    response = requests.get('https://tokyo.craigslist.org/search/hhh?query=%E7%8C%AB%E3%80%80%E7%8A%AC&sort=rel')
#    data = response.text
#    print(data)
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#



#import requests
#
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from bs4 import BeautifulSoup
#
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    print(search)
#    print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL
#    response = requests.get('https://tokyo.craigslist.org/search/hhh?query=%E7%8C%AB%E3%80%80%E7%8A%AC&sort=rel')
#    data = response.text
#    #print(data)
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#


#import requests
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from bs4 import BeautifulSoup
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    #print(search)
#    #print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
#    print(final_url)
#    response = requests.get('https://tokyo.craigslist.org/search/hhh?query=%E7%8C%AB%E3%80%80%E7%8A%AC&sort=rel')
#    data = response.text
#    #print(data)
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#


#import requests
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from bs4 import BeautifulSoup
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    #print(search)
#    #print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
#    response = requests.get(final_url)
#    data = response.text
#    #print(data)
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#


#import requests
#from bs4 import BeautifulSoup
#
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from . import models
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    models.Search.objects.create(search=search)
#    #print(search)
#    #print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
#    response = requests.get(final_url)
#    data = response.text
#    #print(data)
#    soup = BeautifulSoup(data, features='html.parser')
#    post_titles = soup.find_all('a', {'class': 'result-title'})
##    print(post_titles)
##    print(post_titles[0])
#    print(post_titles[0].get('href'))
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)


#import requests
#from bs4 import BeautifulSoup
#
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from . import models
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    models.Search.objects.create(search=search)
#    #print(search)
#    #print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
#    response = requests.get(final_url)
#    data = response.text
#    #print(data)
#    soup = BeautifulSoup(data, features='html.parser')
#    post_listings = soup.find_all('li', {'class': 'result-row'})
#    
#    post_title = post_listings[0].find(class_='result-title').text
#    
#    post_url = post_listings[0].find('a').get('href')
#    
#    post_price = post_listings[0].find(class_='result-price').text
#    print(post_title)
#    print(post_url)
#    print(post_price)
##    print(post_titles[0])
#    #print(post_titles[0].get('href'))
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)

#
#
#import requests
#from bs4 import BeautifulSoup
#
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from . import models
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    models.Search.objects.create(search=search)
#    #print(search)
#    #print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
#    response = requests.get(final_url)
#    data = response.text
#    #print(data)
#    soup = BeautifulSoup(data, features='html.parser')
#    post_listings = soup.find_all('li', {'class': 'result-row'})
#    
##    post_title = post_listings[0].find(class_='result-title').text
##    
##    post_url = post_listings[0].find('a').get('href')
##    
##    post_price = post_listings[0].find(class_='result-price').text
#    
#    final_postings = []
#    
#    for post in post_listings:
#        post_title = post.find(class_='result-title').text
#        
#        post_url = post.find('a').get('href')
#        
#        post_price = post.find(class_='result-price').text
#        
#        final_postings.append((post_title, post_url, post_price))
#
##        final_postings.append(post_title, post_url, post_price)
#    
#    print(final_postings[0])    
#    
#    stuff_for_frontend = {'search':search,}
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#



#
#import requests
#from bs4 import BeautifulSoup
#
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from . import models
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    models.Search.objects.create(search=search)
#    #print(search)
#    #print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
#    response = requests.get(final_url)
#    data = response.text
#    #print(data)
#    soup = BeautifulSoup(data, features='html.parser')
#    post_listings = soup.find_all('li', {'class': 'result-row'})
#    
#    final_postings = []
#    
#    for post in post_listings:
#        post_title = post.find(class_='result-title').text
#        
#        post_url = post.find('a').get('href')
#        
#        post_price = post.find(class_='result-price').text
#        
#        
#        final_postings.append((post_title, post_url, post_price))
#   
#    
#    stuff_for_frontend = {
#        'search':search,
#        'final_postings':final_postings,
#    
#    }
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#


#import requests
#from bs4 import BeautifulSoup
#
#
#from requests.compat import quote_plus
#from django.shortcuts import render
#from . import models
#
#BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'
#
#def home(request):
#    return render(request, 'base.html')
#
#def new_search(request):
#    search = request.POST.get('search')
#    models.Search.objects.create(search=search)
#    #print(search)
#    #print(quote_plus(search))
#    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
#    response = requests.get(final_url)
#    data = response.text
#    #print(data)
#    soup = BeautifulSoup(data, features='html.parser')
#    post_listings = soup.find_all('li', {'class': 'result-row'})
#    
#    final_postings = []
#    
#    for post in post_listings:
#        post_title = post.find(class_='result-title').text
#        
#        post_url = post.find('a').get('href')
#        
#        if post.find(class_='result-price'):
#            post_price = post.find(class_='result-price').text
#        else:
#            post_price='価格表示なし'
#        
#        
#        final_postings.append((post_title, post_url, post_price))
#   
#    
#    stuff_for_frontend = {
#        'search':search,
#        'final_postings':final_postings,
#    
#    }
#    return render(request, 'my_app/new_search.html', stuff_for_frontend)
#


import requests
from bs4 import BeautifulSoup


from requests.compat import quote_plus
from django.shortcuts import render
from . import models

BASE_CRAIGSLIST_URL='https://tokyo.craigslist.org/search/hhh?query={}'

BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    #print(search)
    #print(quote_plus(search))
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    #print(data)
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    
    final_postings = []
    
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        
        post_url = post.find('a').get('href')
        
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price='価格表示なし'
        
        #イメージ、つまり写真を加える少し複雑。
        #画像で検索
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            
        
        final_postings.append((post_title, post_url, post_price, post_image_url))
   
    
    stuff_for_frontend = {
        'search':search,
        'final_postings':final_postings,
    
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)

