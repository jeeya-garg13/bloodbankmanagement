import mysql.connector
from tabulate import tabulate


con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234" ,database="Blood_Bank_Management")
cur=con.cursor()


def AddReceiver():
    while True:
        receiver_name=input("Enter Receiver's Name:")
        gender=input("Enter Receiver's Gender(M/F):")
        age=int(input("Enter Receiver's Age:"))
        mob_no=input("Enter Receiver's Mobile No:")
        address=input("Enter Receiver's Address:")
        blood_grp=input("Enter Receiver's Blood Group:")
        Quantity=int(input("Enter Receiver's Blood Requirement:"))
        print()
        cur.execute("insert into ReceiverDetails(Receiver_Name,Gender,Age,Mobile_No,Address,Blood_Group,Quantity) values('{}','{}','{}','{}','{}','{}','{}');".format(receiver_name,gender,age,mob_no,address,blood_grp,Quantity))
        con.commit()
        cur.execute("update stock set Quantity=Quantity-{} where Blood_Group='{}';".format(Quantity,blood_grp))
        con.commit()
        status=input("enter more records(y/n):")
        print()
        if status in ['n','N']:
            print("Receiver's Details added successfully!")
            print()
            break



def SearchReceiver():
    receiver_id=int(input("Enter Receiver's Id whose details are to be searched:"))
    print()
    cur.execute("select * from receiverdetails where Receiver_Id={};".format(receiver_id))
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Receiver_ID","Receiver_Name","Gender","Age","Mobile_No","Address","Blood_Group","Quantity"],tablefmt="psql"))
        print()
    else:
        print("Record not found for the entered Receiver's Id!")
        print()


def DisplayStock():
    cur.execute("select * from stock;")
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Blood_Group","Quantity"],tablefmt="psql"))
        print()
    else:
        print("Table is empty:No record found!")
        print()
            

            
def menu():
    while True:
        print("1.Add your Details\n2.Search your Details\n3.View Stock Details\n4.Exit")
        print()
        ch=int(input("Enter your requirement:\t"))
        print()
        if ch==1:
            AddReceiver()
        elif ch==2:
            SearchReceiver()
        elif ch==3:
            DisplayStock()
        else:
            break

    

