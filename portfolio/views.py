import json

from django.core import serializers
from django.shortcuts import render, redirect
import ccxt
import http.client

from .forms import AddNewAsset, AddNewUser
from .models import Asset, User


def index(request):
    return render(request,'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')


def market_view(request):
    return render(request,'portfolio/market.html')

def market_news(request):
    import requests

    url = "https://investing-cryptocurrency-markets.p.rapidapi.com/coins/get-news"

    querystring = {"pair_ID": "1057391", "page": "1", "time_utc_offset": "28800", "lang_ID": "1"}

    headers = {
        'x-rapidapi-host': "investing-cryptocurrency-markets.p.rapidapi.com",
        'x-rapidapi-key': "fdac14d600mshc374a3fc825cf75p1b1f3djsn48b05e8b6305"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.json()['data'])
    data = response.json()['data']

    #All News API data
    url_all = "https://crypto-news-live.p.rapidapi.com/news"

    headers = {
        'x-rapidapi-host': "crypto-news-live.p.rapidapi.com",
        'x-rapidapi-key': "880fd93c19msh4398e1149e010aep102750jsn999e924bb265"
    }

    response_all = requests.request("GET", url_all, headers=headers)
    data_all = response_all.json()
    print(data_all)

    context = {"items":data[0]['screen_data']['news'], "items_all":data_all}
    return render(request,'portfolio/market_news.html', context)


def dashboard(request):
    return render(request,'portfolio/dashboard.html')

def exchanges(request, enableRateLimit=None):

    # print(dir(ccxt))
    binance =  ccxt.binance()
    markets =  binance.load_markets()

    # async def tick(exchange):
    #     for market in markets:
    #         response = await exchange.fetchOrderBook(market)
    #
    #     for market in markets:
    #         # print(binance.fetch_ticker(market)['info'])
    #         lastPrice = binance.fetch_ticker(market)['info']['lastPrice']
    #         open = binance.fetch_ticker(market)['info']['openPrice']
    #         high = binance.fetch_ticker(market)['info']['highPrice']
    #         low = binance.fetch_ticker(market)['info']['lowPrice']
    #         volume = binance.fetch_ticker(market)['info']['volume']
    #     return response

    # exchange = ccxt.binance()
    # while (True):
    #     result = await tick (exchange)
    #


    tickers = binance.fetch_tickers()
    print(tickers)
    for ticker in tickers:
        print(tickers[ticker])


    context = {'markets': markets,
               'tickers':tickers,
               'binance':binance
               }
    return render(request,'portfolio/exchanges.html',context)


def register(request):
    return render(request,'portfolio/user_registration.html')


def portfolio(request):
    assets = Asset.objects.all()
    context= {'assets':assets}
    return render(request,'portfolio/portfolio.html',context)


def add_asset(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = AddNewAsset()
        else:
            asset = Asset.objects.get(pk=id)
            form = AddNewAsset(instance=asset)
        return render(request, 'portfolio/add_asset.html', {'form': form})
    else:
        if id == 0:
            form = AddNewAsset(request.POST)
            if form.is_valid():
                form.save()
        else:
            asset = Asset.objects.get(pk=id)
            form = AddNewAsset(request.POST, instance=asset)
            if form.is_valid():
                form.save()

        return redirect('../../portfolio/portfolio')


def view_user_profile(request,id=0):

    #View pages to create new or edit existing user
    if request.method == 'GET':
        # create new user profile form page
        if id == 0:
            form = AddNewUser()

        # view existing user profile to edit
        else:
            user = User.objects.get(pk=id)
            form = AddNewUser(instance=user)

        return render(request, 'portfolio/add_user_profile.html', {'form': form})

    # Post : Save method for new or edit existing user
    else:
        # save new user
        if id == 0:
            form = AddNewUser(request.POST)
            if form.is_valid():
                form.save()

        # update existing user
        else:
            user = User.objects.get(pk=id)
            form = AddNewUser(request.POST, instance=user)
            if form.is_valid():
                form.save()

        return redirect('../../portfolio/dashboard')

def tview_ta(request, id):
    from tradingview_ta import TA_Handler, Interval, Exchange

    ta = TA_Handler(
        symbol=id,
        screener="crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_DAY
    )
    print(ta.get_analysis().summary)
    context= {'id':id}
    return render(request,'portfolio/technical_analysis.html', context)


def login(request):
    return render(request,'portfolio/login.html')