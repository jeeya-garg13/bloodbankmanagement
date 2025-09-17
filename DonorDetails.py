import mysql.connector
from tabulate import tabulate

con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234",database="Blood_Bank_Management")
cur=con.cursor()

def AddDonor():
    while True:
        donor_name=input("Enter Donor's Name:")
        gender=input("Enter Donor's Gender(M/F):")
        age=int(input("Enter Donor's Age:"))
        mob_no=input("Enter Donor's Mobile No:")
        address=input("Enter Donor's Address:")
        blood_grp=input("Enter Donor's Blood Group:")
        print()
        if age>=18:
            cur.execute("insert into DonorDetails (Donor_Name,Gender,Age,Mobile_No,Address,Blood_Group) values('{}','{}','{}','{}','{}','{}');".format(donor_name,gender,age,mob_no,address,blood_grp))
            con.commit()
            cur.execute("update stock set Quantity=Quantity+1 where Blood_Group='{}';".format(blood_grp))
            con.commit()
            print("Donor's Details added successfully!")
            print()
        else:
            print("Donor is not eligible to donate blood!")
            print()
        status=input("Enter more records(y/n):")
        print()
        if status in ['n','N']:
            break
    

        
def SearchDonor():
    donor_id=int(input("Enter Donor's Id whose details are to be searched:"))
    print()
    cur.execute("select * from donordetails where Donor_Id={};".format(donor_id))
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Donor_ID","Donor_Name","Gender","Age","Mobile_No","Address","Blood_Group","Quantity"],tablefmt="psql"))
        print()
    else:
        print("Record not found for the entered Donor's Id!")
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
        print("1.Add Your Details\n2.Search Your Details\n3.Exit")
        print()
        ch=int(input("Enter your requirement:\t"))
        print()
        if ch==1:
            AddDonor()
        elif ch==2:
            SearchDonor()
        else:
            break
