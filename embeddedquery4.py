from base64 import b64encode
import mysql.connector
from datetime import datetime
import time

def connectit():
    mydb = mysql.connector.connect(
    host="election.cpawyehotia9.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="ELECTION12"
    )
    return mydb

# https://www.mysqltutorial.org/python-mysql-blob/
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
#xxxxxxxxxxxxxxxxxx

def verification_official():

    connection=connectit()
    cursor=connection.cursor()
    cursor.execute("""use Election""")
    cursor.execute("select * from Unverified_User where V_official_id=20214")
    table=cursor.fetchall()

    allusers=[]
    count=0
    filename="verifdoc"

    if(len(table)==0):
        print("You have no users to verify currently.")
        return
    print("Unverified ID \t\t\t Verification Document Type")
    for i in table:
        write_file(i[2], filename+str(i[0])+".png")
        print(str(i[0])+"\t\t\t\t "+str(i[1]))
        count+=1

    print("Verification Documents can be viewed from current folder.")
    
    print("Enter ID of user to verify.")
    print("Enter 'end' to exit.")
    s=input()
    if(s=="end"):
        return
    else:
        print("Enter 'verify' to confirm verification of user with ID="+s)
        ss=input()
        if ss=="verify":

            cursor.execute("select Constituency_id from Verification_Official where id=20214")
            table=cursor.fetchall()

            contituencyid=0
            for t in table:
                for x in t:
                    constituencyid=x
                    break
                break

            cursor.execute("select * from Unverified_User where Unverified_id="+str(s))
            table=cursor.fetchall()
            x=table[0]

            # x=f"insert into Election.voter (id, constituency_id) VALUES ({x[0]},{constituencyid})"
            query="insert into Election.voter (id, constituency_id) VALUES (%s,%s)"
            inp=(x[0],constituencyid)
            # print(x)
            cursor.execute(query,inp)
            connection.commit()
            
            query = "Update Election.voter set Registration_Date = %s where id = %s"
            current_Date = datetime.now()
            formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
            inp = (formatted_date, x[0])
            cursor.execute(query, inp)
            connection.commit()

            # print(cursor.rowcount, "record inserted in 'voter'.")

            fil="verifdoc"+str(x[0])+".png"
            thedata = open(fil, 'rb').read()
            # print(fil)

            query="update Election.voter set document=%s where id=%s"
            inp=(thedata,x[0])
            cursor.execute(query,inp)
            connection.commit()

            cursor.execute("delete from Election.Unverified_User where Unverified_id= "+str(x[0]))
            # inp=(x[0])
            # cursor.execute(query,inp)
            connection.commit()

            cursor.close()
            connection.close()
            print("User verified.\nUser Data deleted from 'Unverified_User'.\nUser data added to 'Voter'.")

            return

verification_official()