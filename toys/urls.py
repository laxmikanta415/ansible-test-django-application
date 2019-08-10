from django.urls import path
from .views import toy_list, toy_detail
app_name = 'toys'
urlpatterns = [
	path('', toy_list, name='toys_list'),
	path('<id>/', toy_detail, name='toys_detail'),
]