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
            user = authenticate(request, username=dict['username'], password=dict['password'])
            if(user is not None):

                return HttpResponse(f'logged in as {user.first_name} {user.last_name}');
            else:
                return HttpResponse('invalid username or password');

    return render(request, "login.html")
    # return render(request, "voter_view1.html")

def ec_official_profile(request):
    if(request.method == "POST"):
        election_date = request.POST.dict()
        print(election_date)
        start_date = election_date['start_date']
        end_date = election_date['end_date']
        if(start_date >= end_date):
            return HttpResponse('Invalid Dates entered')
        else:
            return HttpResponse(f'New Election set from {start_date} to {end_date}');
    return render(request, "ec_official_profile.html")

def admin_official_profile(request):
    if(request.method == "POST"):
        candidate_details = request.POST.dict()
        print(candidate_details)
        candidate_id = candidate_details['candidate_id']
        wealth = candidate_details['wealth']
        updated_year = candidate_details['updated_year']
        criminal_cases = candidate_details['criminal_cases']
        return HttpResponse(f'Candidate {candidate_id} details for the year {updated_year} have been entered');
    return render(request, "admin_official_profile.html")

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

def f_voter_view1(request):
    return render(request, "voter_view1.html")

def f_voter_view2(request):
    return render(request, "voter_view2.html")

def f_voter_view3(request):
    return render(request, "voter_view3.html")

def party_view(request):
    return render(request,"party_view.html")