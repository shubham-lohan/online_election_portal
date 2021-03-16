from django.urls import path
from django.conf.urls import url,include

from .views import home,login;

urlpatterns = [
	path('',home,name='home'),
	path('',login,name='login'),
]
