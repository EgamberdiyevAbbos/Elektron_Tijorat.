from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', index, name='home'),
    path('category', category, name='category'),
    path('buy', buy, name='buy'),
    path('customer', customer, name='customer'),
    path('product', product, name='product'),
    path('search', search, name='search'),
    path('signup', signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)