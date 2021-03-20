from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "home.html")


def login(request):
    if(request.method == "POST"):
            dict = request.POST.dict();
            print(dict);
            user = authenticate(request, username=['username'], password=dict['password'])
            if(user is not None):
                return HttpResponse(f'logged in as {user.first_name} {user.last_name}');
            else:
                return HttpResponse('invalid username or password');
 
    return render(request, "login.html")


def register(request):
    print("f")
    return render(request, "register.html")



def cand_profile(request):
    return render(request, "cand_profile.html")


def register_candidate(request):
    return render(request, "candidate_registration.html")


def register_party(request):
    return render(request, "party_registration.html")


def register_voter(request):
    if(request.method == "POST"):
            dict = request.POST.dict()
            if(not(User.objects.filter(username=dict['Username']).exists())):
                user = User.objects.create_user(dict['Username'],dict['firstName']+"@gmail.com",dict['password']);

                user.first_name,user.last_name = dict['firstName'],dict['lastName']
                user.save();
                return HttpResponse('new user created');
            else:
                return HttpResponse('user already exists');
    return render(request, "voter_registration.html")


def register_official(request):
    return render(request, "official_registration.html")
