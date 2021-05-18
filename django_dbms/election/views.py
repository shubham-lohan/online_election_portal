from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from base64 import b64encode
import mysql.connector
from datetime import date
  
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
            user="A"
            if(user is not None):
                connection=connectit()
                cursor=connection.cursor()
                cursor.execute("""use Election""")
                xxx="Tc8IFClQV0HQvXNnbtAD6PWCVOBI8p9SFXzC5hg0AJbaXArOAp3JaMaFBWeE8qPrSEIdDtflNZC9rxeAp7n1uJRRa7tSwRuI5D66"

                cursor.execute("select ID from person where Token=\""+xxx+"\"")  
                table=cursor.fetchall()
                print("A")
                print(table)
                vid=table[0][0]
                cursor.execute("select id from voter where id="+str(vid))  
                table=cursor.fetchall()
                request.method = "blah"
                cursor.close()
                connection.commit()
                connection.close()
                if(len(table)>0):
                    return render(request, "voter_view2.html") # redirect("login/voter_view2")
                else:
                    return HttpResponse('request view page should be opened');
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
    xxx="Tc8IFClQV0HQvXNnbtAD6PWCVOBI8p9SFXzC5hg0AJbaXArOAp3JaMaFBWeE8qPrSEIdDtflNZC9rxeAp7n1uJRRa7tSwRuI5D66"

    cursor.execute("select * from person where token=\""+xxx+"\"")  
    table=cursor.fetchall()
    id=table[0][0]
    cursor.execute("select * from Voted_for where Election_ID=6 and voter_id="+str(id));
    table=cursor.fetchall()
    print("table")
    print(table)
    
    print(table)
    if len(table)>0:
        cid=str(table[0][1])
        cursor.execute("select FirstName, LastName from person where id="+str(table[0][1]))  
        table=cursor.fetchall()
        
        return HttpResponse("you have voted for "+table[0][0]+" "+table[0][1] +" whose voter id is "+cid)
    else:
        cursor.execute("""select person.FirstName,person.LastName,Political_Party.name,Political_Party.symbol,x.candid from person,Political_Party,Member_Of,
        (select Stands_From.id as candid from Constituency, voter,Stands_From
        where voter.id=1 and Constituency.id=voter.constituency_id and Stands_From.constituency_id=Constituency.id and Stands_From.election_id=5) as x
        where  x.candid=Member_Of.Candidate_id and Member_Of.Party_ID=Political_Party.id and x.candid=person.ID""")
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
        gender = request.POST.get("gender");
        mm = request.POST.get("mm");
        submit=request.POST.get("submit");
        # reset=request.POST.get("reset");
        print("i5")
        print(submit)
        # print("i6")
        # print(reset)
        # if(reset!=None):
        #     return justload(request)

        bod=dict['yyyy']+"-"+mm+"-"+dict['dd']
         
        connection=connectit()
        cursor=connection.cursor()
        cursor.execute("""use Election""")

        cursor.execute("update person set FirstName=\""+dict['firstName']+"\", LastName=\""+dict['lastName']+"\", DOB=Date(\""+ bod+"\"), PhoneNumber=\""+dict['phone']+"\", Gender=\""+gender+"\", Income="+dict['incom']+", education=\""+dict['educs']+"\", religion=\""+dict['relig']+"\" where Token=\""+dict['xxx']+"\"")
        cursor.execute("select ID from person where Token=\"xxx\" ")
        table=cursor.fetchall()
        id=table[0][0]

        # cursor.execute("insert into Unverified_User values("+id+)
        # cursor.execute("delete from voter where Token=\""+dict['xxx']+"\"")
        # cursor.execute("delete from Candidate where id="+id)
        
        cursor.close()
        connection.commit()
        connection.close()
        return HttpResponse("your request is pending")
    return justload(request)

def justload(request):
    connection=connectit()
    cursor=connection.cursor()
    cursor.execute("""use Election""")
    xxx="Tc8IFClQV0HQvXNnbtAD6PWCVOBI8p9SFXzC5hg0AJbaXArOAp3JaMaFBWeE8qPrSEIdDtflNZC9rxeAp7n1uJRRa7tSwRuI5D66"

    cursor.execute("select * from person where token=\""+xxx+"\"")  
    table=cursor.fetchall()
    id=table[0][0]
    print("id")
    print(id)
    cursor.execute("select name from voter,Constituency where voter.id="+str(id)+" and Constituency.id=voter.constituency_id")  
    constituency_name= cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return render(request, "voter_view2.html",{'table': table, 'constituency_name':constituency_name})

def f_voter_view3(request):
    year=date.today().year
    connection=connectit()
    cursor=connection.cursor()
    cursor.execute("""use Election""")

   
    xxx="Tc8IFClQV0HQvXNnbtAD6PWCVOBI8p9SFXzC5hg0AJbaXArOAp3JaMaFBWeE8qPrSEIdDtflNZC9rxeAp7n1uJRRa7tSwRuI5D66"
    cursor.execute("select  ID from   person where Token=\""+xxx+"\"" )
    table=cursor.fetchall()
    print("table1")
    print(table)

    
    p_id= table[0][0]
    cursor.execute("select  Wealth  from BioData where id="+str(p_id)+" and updated_year="+str(year))

    table=cursor.fetchall()
    print("table2")
    print(table)
    wealths=""
    if(len(table)>0):
        wealths=table[0][0]
   
    if(request.method == "POST"):
        dict = request.POST.dict();
        wealths=dict['weal']
        if(wealths==""):
            cursor.execute("insert into BioData values("+str(p_id)+","+str(dict['weal'])+","+str(year)+")")
            
        else:
            cursor.execute("update BioData set Wealth="+str(dict['weal'])+" where id="+str(p_id) +" and updated_year="+str(year)) 
    connection.commit()   
    # print("id")
    # print(id)
    # cursor.execute("select name from voter,Constituency where voter.id="+str(id)+" and Constituency.id=voter.constituency_id")  
    # constituency_name= cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return render(request, "voter_view3.html",{'wealth': wealths ,'year':year})

def party_view(request):
    return render(request,"party_view.html")