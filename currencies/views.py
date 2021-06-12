from django.shortcuts import render
import requests
import json


def home(request):
    info = requests.get('https://api.coinlore.net/api/tickers/')
    price = json.loads(info.content)
    data = price['data']
    my_string = '-'

    return render(request, 'home.html', {'data': data, 'my_string': my_string})


def search(request):
    if request.method == "POST":
        try:
            info = requests.get(
                'https://api.coinlore.net/api/ticker/?id=' + request.POST['symbol'])
            price = json.loads(info.content)
            mystring = "-"
            return render(request, 'search.html', {'price': price, "mystring" : mystring})
        except:
            return render(request, 'search.html', {'message' : 'Could not find'})

    return render(request, 'search.html', {})
