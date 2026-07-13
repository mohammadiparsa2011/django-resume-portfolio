from django.urls import path
from .views import home_view, contact

app_name = 'core'

urlpatterns = [
    path('', home_view, name='index'),
    path('contact/', contact, name='contact'),  # <--- اضافه شد
]