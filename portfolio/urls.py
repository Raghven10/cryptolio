from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('market', views.market_view, name='market_view'),
    path('market_news', views.market_news, name='market_news'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('signup', views.register, name='register'),
    path('exchanges', views.exchanges, name='exchanges'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('add_asset/<int:id>', views.add_asset, name='add_asset'),
    path('tech_analysis/<slug:id>', views.tview_ta, name='tview_ta'),
    path('user_profile/<int:id>', views.view_user_profile, name='user_profile'),
]