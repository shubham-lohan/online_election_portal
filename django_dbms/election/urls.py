from django.urls import path,re_path
from django.conf.urls import url, include

from .views import home, login, cand_profile, register_candidate, register_party, register_voter, register_official, register, f_voter_view1,f_voter_view2,f_voter_view3

urlpatterns = [
    path('', home, name='home'),
    path(r'login', login, name='login'),
    path('register', register_voter, name='register'),
    path('profile/candidate', cand_profile, name='cand_profile'),
    path('register/candidate', register_candidate, name="reg_cand"),
    path('register/party', register_party, name="register_party"),
    path('register/official', register_official, name="register_official"),
    path('login/voter_view1',f_voter_view1,name="voter_view1"),
    path('login/voter_view2',f_voter_view2,name="voter_view2"),
    path('login/voter_view3',f_voter_view3,name="voter_view3"),
]
