import mysql.connector
import DonorDetails
import ReceiverDetails
from tabulate import tabulate

con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234",database="Blood_Bank_Management")
cur=con.cursor()

def DisplayDonors():
    cur.execute("select * from donordetails;")
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Donor_ID","Donor_Name","Gender","Age","Mobile_No","Address","Blood_Group","Quantity"],tablefmt="psql"))
        print()
    else:
        print("Table is empty:No record found!")
        print()

def DisplayReceiver():
    cur.execute("select * from Receiverdetails;")
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Receiver_ID","Receiver_Name","Gender","Age","Mobile_No","Address","Blood_Group","Quantity"],tablefmt="psql"))
        print()
    else:
        print("Table is empty:No record found!")
        print()

        
def UpdateDonor():
    donor_id=int(input("Enter Donor's Id whose details are to be edited:"))
    print()
    cur.execute("select * from donordetails where Donor_Id={};".format(donor_id))
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Donor_ID","Donor_Name","Gender","Age","Mobile_No","Address","Blood_Group","Quantity"],tablefmt="psql"))
        print()
        mob_no=input("Enter updated Mobile No:")
        address=input("Enter updated Address:")
        cur.execute("update donordetails set Mobile_No='{}',Address='{}' where Donor_Id={};".format(mob_no,address,donor_id))
        con.commit()
        print()
        print("Details for entered Donor's Id are edited successfully!")
        print()
    else:
        print("Record not found for the entered Donor's Id!")
        print()


def DeleteDonor():
    donor_id=int(input("Enter Donor's Id whose details are to be deleted:"))
    print()
    cur.execute("select * from donordetails where Donor_Id={};".format(donor_id))
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Donor_ID","Donor_Name","Gender","Age","Mobile_No","Address","Blood_Group","Quantity"],tablefmt="psql"))
        print()
        cur.execute("delete from donordetails where Donor_Id={};".format(donor_id))
        con.commit()
        print("Details for the entered Donor's Id are deleted successfully!")
        print()
    else:
        print("Record not found for the entered Donor's Id!")
        print()


def DeleteReceiver():
    receiver_id=int(input("Enter Receiver's Id whose details are to be deleted:"))
    print()
    cur.execute("select * from Receiverdetails where Receiver_Id={};".format(receiver_id))
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["Receiver_ID","Receiver_Name","Gender","Age","Mobile_No","Address","Blood_Group","Quantity"],tablefmt="psql"))
        print()
        cur.execute("delete from Receiverdetails where Receiver_Id={};".format(receiver_id))
        con.commit()
        print("Details for the entered Receiver's Id are deleted successfully!")
        print()
    else:
        print("Record not found for the entered Receiver's Id!")
        print()
   

def DisplayStock():
    l=input("Enter who was last one(donor/receiver):")
    if l.upper()=="DONOR":
        DonorDetails.DisplayStock()
    elif l.upper()=="RECEIVER":
        ReceiverDetails.DisplayStock()


def menu():
    while True:
        print("1.Update Donor Details\n2.Display all Donors Details\n3.Delete Donor Details\n4.Delete Receiver Details\n5.Display all Receiver Details\n6.View Stock Details\n7.Exit")
        print()
        ch=int(input(" Enter your requirement:\t"))
        print()
        if ch==1:
            UpdateDonor()
        elif ch==2:
            DisplayDonors()
        elif ch==3:
            DeleteDonor()
        elif ch==4:
            DeleteReceiver()
        elif ch==5:
            DisplayReceiver()
        elif ch==6:
            DisplayStock()
        elif ch==7:
            break
               
