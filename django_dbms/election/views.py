from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from base64 import b64encode
import mysql.connector


# Create your views here.
def connectit():
    mydb = mysql.connector.connect(
    host="election.cpawyehotia9.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="ELECTION12"
    )
    return mydb
 

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
    if(request.method == "POST"):
            dict = request.POST.dict();

            print("i4")

            print(dict)
            connection=connectit()
            cursor=connection.cursor()
            cursor.execute("""use Election""")

            cursor.execute("select * from Voted_for where Election_ID=6 and voter_id=1");
            table=cursor.fetchall()
            print("i3")
            print(table)
            if len(table)>0:
                return HttpResponse("you have voted for candidate with voter id:"+str(table[0][1]))
            else:

                cursor.execute("insert into Voted_for values (1,"+dict['hopping']+",6)");

                cursor.close()
                connection.commit()
                connection.close()
                return render(request, "voter_view2.html")
             
            

            
    print("i1")
    connection=connectit()
    cursor=connection.cursor()
    # print("blahblahblahblahblah")
    # print(cursor)
    cursor.execute("use Election")
    cursor.execute("select * from Voted_for where Election_ID=6 and voter_id=1");
    table=cursor.fetchall()
    print(table)
    if len(table)>0:
        return HttpResponse("you have voted for candidate with voter id:"+str(table[0][1]))
    else:
        cursor.execute("""select person.FirstName,person.LastName,Political_Party.name,Political_Party.symbol,x.candid from person,Political_Party,Member_Of,
        (select Stands_From.id as candid from Constituency, voter,Stands_From
        where voter.id=1 and Constituency.id=voter.constituency_id and Stands_From.constituency_id=Constituency.id and Stands_From.election_id=5) as x
        where  x.candid=Member_Of.Candidate_id and Member_Of.Party_ID=Political_Party.id and x.candid=person.id""")
        table=cursor.fetchall()
        # print(table)
        print("i2")
        imgs=[]
        for i in table:
            imgs.append( (i[0],i[1],i[2],b64encode(i[3]).decode() ,i[4]))
        cursor.close()
        connection.close()
        # print("b2")
        # print(imgs)
        return render(request, "voter_view1.html",{  'imgs':imgs, 'n':range(len(table))})

def f_voter_view2(request):
    if(request.method == "POST"):
        dict = request.POST.dict();
        dict2 = request.POST.get("gender");

        print("i5")

        print(dict)
        print("i6")

        print(dict2)
        # connection=connectit()
        # cursor=connection.cursor()
        # cursor.execute("""use Election""")

        # cursor.execute("update person set FirstName=\""+dict['firstname']+"\", LastName=\""+dict['lastName']+"\", DOB=Date(\"2017-06-15\"), PhoneNumber=\""+dict['phone']+"\", Gender=\""+dict[]+"\", Income="+dict['incom']+", education=\""+dict['educs']+"\", religion=\""+dict['relig']+"\" where Token=\""+dict['csrfmiddlewaretoken']+"\"")
        # cursor.execute("insert into person values("0","Raj","kumar",DATE("2017-06-15"),123456789,"Male",10000,"10th pass","xxx","hinduism");");
        # table=cursor.fetchall()
        # print("i3")
        # print(table)
        # if len(table)>0:
        #     return HttpResponse("you have voted for candidate with voter id:"+str(table[0][1]))
        # else:

        #     cursor.execute("insert into Voted_for values (1,"+dict['hopping']+",6)");

        #     cursor.close()
        #     connection.commit()
        #     connection.close()
        #     return render(request, "voter_view2.html")
    return render(request, "voter_view2.html")

def f_voter_view3(request):
    return render(request, "voter_view3.html")
