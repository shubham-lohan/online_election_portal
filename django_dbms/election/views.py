from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def login(request):
    print("test")
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
    print("f")
    if(request.method == "POST"):
            print(request.POST.dict)

    return render(request, "voter_registration.html")


def register_official(request):
    return render(request, "official_registration.html")
