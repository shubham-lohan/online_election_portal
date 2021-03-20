from django.urls import path,re_path
from django.conf.urls import url, include

from .views import home, login, cand_profile, register_candidate, register_party, register_voter, register_official, register

urlpatterns = [
    path('', home, name='home'),
    path(r'login', login, name='login'),
    path('profile/candidate', cand_profile, name='cand_profile'),
    path(r'register', register, name="register"),  # problem in adding this!
    path('register/candidate', register_candidate, name="reg_cand"),
    path('register/party', register_party, name="register_party"),
    path('register/voter', register_voter, name="register_voter"),
    path('register/official', register_official, name="register_official"),

]
