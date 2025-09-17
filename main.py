

import mysql.connector
import DonorDetails
import ReceiverDetails
import stock
import admin

con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234")
cur=con.cursor()

cur.execute("create database if not exists Blood_Bank_Management;")

con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234" ,database="Blood_Bank_Management")
cur=con.cursor()
cur.execute("use Blood_Bank_Management;")
cur.execute('''create table if not exists DonorDetails(Donor_Id int primary key auto_increment,Donor_Name varchar(50) not null,Gender char(1) not null,
Age char(2) not null,Mobile_No char(10) not null,Address varchar(50) not null,Blood_Group char(3) not null,Quantity char(1) default '1');''')
cur.execute('''create table if not exists ReceiverDetails(Receiver_Id int primary key auto_increment,Receiver_Name varchar(40) not null,Gender char(1) not null,
Age char(2) not null,Mobile_No char(10) not null,Address varchar(50) not null,Blood_Group char(3),Quantity char(2) not null);''')
cur.execute("create table if not exists stock(Blood_Group char(3) not null,Quantity int);")

print("---------------RED CROSS SOCIETY WELCOMES YOU---------------")

while True:
    ch=int(input("Main Menu:\n1.Admin\t2.Donor\t3.Receiver\t4.Exit\nWho are you?\t"))
    print()
    if ch==1:
        admin.menu()
    elif ch==2:
        DonorDetails.menu()
    elif ch==3:
        ReceiverDetails.menu()
    elif ch==4:
        break
    else:
        print("Invalid input!!")

