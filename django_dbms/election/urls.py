from django.urls import path
from django.conf.urls import url, include

from .views import home, login, cand_profile, register_candidate, register_party, register_voter, register_official, register

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('profile/candidate', cand_profile, name='cand_profile'),
    # path('register', register, name="register"),  # problem in adding this!
    path('regsiter/candidate', register_candidate, name="reg_cand"),
    path('regsiter/party', register_party, name="register_party"),
    path('regsiter/voter', register_voter, name="register_voter"),
    path('regsiter/official', register_official, name="register_official"),

]
