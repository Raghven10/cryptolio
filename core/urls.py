# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this
from apps.home import views

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),          # UI Kits Html files    
]


handler404 = 'apps.home.views.error_404'

handler500 = 'apps.home.views.error_500'

handler403 = 'apps.home.views.error_403'

handler400 = 'apps.home.views.error_400'

