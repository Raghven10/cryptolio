# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.market, name='home'),


    # The Market page
    path('market', views.market, name='market'),

     # The Portfolio page
    path('portfolio', views.portfolio, name='portfolio'),

    path('get_coins/<str:id>', views.get_coins, name='get_coins'),

     # The News page
    path('screener', views.screener, name='screener'),

     # The News page
    path('news', views.news, name='news'),

    # The Market page
    path('market/<str:id>', views.coin, name='coin-info'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
