# -*- encoding: utf-8 -*-

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import FormView

from apps.home.forms import OrderForm
 
from .models import Asset

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def heatmap(request):
    context = {'segment': 'heatmap'}

    html_template = loader.get_template('home/heatmap.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def screener(request):
    context = {'segment': 'screener'}

    html_template = loader.get_template('home/market_data.html')
    return HttpResponse(html_template.render(context, request))


# class PortfolioView(FormView):
#     import ccxt
#     exchanges = ccxt.exchanges    
#     form_class = OrderForm
#     template_name = 'home/portfolio.html'
#     success_url = reverse_lazy('portfolio',{'exchanges':exchanges})

@login_required(login_url="/login/")
def portfolio(request):    
    form = OrderForm(request.POST or None)  
    msg = None
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                        
                return HttpResponseRedirect('portfolio')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            msg = 'Error validating the form'
            return HttpResponseRedirect('portfolio')

    else: 
        print('Entering GET method...')  
        import ccxt    
        exchanges = ccxt.exchanges      
          
        orders = Asset.objects.filter(user = request.user.id)
        
        def getLastPrice(o): 
            import ccxt        
            id = o.exchange
            exchange = eval ('ccxt.%s()' %id)
            print(exchange)
            markets = exchange.load_markets() 
            ticker = exchange.fetch_ticker(o.token)
            try:
                lastPrice = ticker['info']['lastPrice']
            except: 
                lastPrice= 0.0
            print(o.token)
            print(lastPrice) 
            return lastPrice
        
        result = map(getLastPrice,orders)
        prices = list(result)
        orders = zip(orders,prices)  
            
    return render(request, "home/portfolio.html", {'segment': 'portfolio','exchanges':exchanges, 'form':form,"msg": msg, 'orders':orders})


@login_required(login_url="/login/")
def delete_asset(request, id):  
    asset = Asset.objects.get(pk=id)
    asset.delete()
    msg = 'Deleted Successfully.'
    return HttpResponseRedirect('../../portfolio')

@login_required(login_url="/login/")
def get_asset(request, id):  
    asset = Asset.objects.get(pk=id) 
    
    return render(request, "home/view_asset.html", {'segment': 'portfolio','asset':asset})

@login_required(login_url="/login/")
def update_asset(request, id):          
    if request.method == "POST":         
        form = OrderForm(request.POST or None)           
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to update Form ..')
                form.save()                        
                return HttpResponseRedirect('portfolio')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            msg = 'Error validating the form'
            return HttpResponseRedirect('portfolio')
    else:
        asset = Asset.objects.get(pk=id)
        form = OrderForm(instance=asset) 

    return render(request, "home/view_asset.html", {'segment': 'portfolio','asset':asset,'form':form})

@login_required(login_url="/login/")
def get_coins(request, id):   
    import ccxt   
    id = id
    exchange = eval ('ccxt.%s()' %id)
    exchange.load_markets()
    data = exchange.symbols    
    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def market(request):
    import requests

    url = "https://coingecko.p.rapidapi.com/coins/markets"

    querystring = {"vs_currency":"usd","page":"1","per_page":"100","order":"market_cap_desc"}

    headers = {
    'x-rapidapi-host': "coingecko.p.rapidapi.com",
    'x-rapidapi-key': "880fd93c19msh4398e1149e010aep102750jsn999e924bb265"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)

    data = response.json()
    #print(data)
    context = {'segment': 'market','data':data}
    html_template = loader.get_template('home/market.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def coin(request, id):
    import requests

    url = "https://coingecko.p.rapidapi.com/coins/{0}".format(id)

    querystring = {"localization":"true","tickers":"true","market_data":"true","community_data":"true","developer_data":"true","sparkline":"false"}

    headers = {
    'x-rapidapi-host': "coingecko.p.rapidapi.com",
    'x-rapidapi-key': "880fd93c19msh4398e1149e010aep102750jsn999e924bb265"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
    data = response.json()
    #print(data)   
  
    context = {'segment': 'market','data':data}
    html_template = loader.get_template('home/coin_info.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def news(request):
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
      
    context = {'segment': 'news','data':data[0]['screen_data']['news']}
    html_template = loader.get_template('home/news.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('errors/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('errors/page-500.html')
        return HttpResponse(html_template.render(context, request))


# default Error pages 
def error_404(request, exception):
        data = {}
        return render(request,'errors/page-404.html', data)

def error_500(request):
        data = {}
        return render(request,'errors/page-500.html', data)

def error_403(request, exception):
        data = {}
        return render(request,'errors/page-403.html', data)

def error_400(request, exception):
        data = {}
        return render(request,'errors/page-400.html', data)