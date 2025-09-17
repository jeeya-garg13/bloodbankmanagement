import mysql.connector
from tabulate import tabulate

con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234",database="blood_bank_management")
cur=con.cursor()
cur.execute("use Blood_Bank_Management;")


def load():
    cur.execute("select * from stock;")
    rec=cur.fetchall()
    if rec:
        pass
    else:
        cur.execute("insert into stock(Blood_Group,Quantity) values('A+',5);")
        cur.execute("insert into stock(Blood_Group,Quantity) values('A-',5);")
        cur.execute("insert into stock(Blood_Group,Quantity) values('B+',5);")
        cur.execute("insert into stock(Blood_Group,Quantity) values('B-',5);")
        cur.execute("insert into stock(Blood_Group,Quantity) values('AB+',5);")
        cur.execute("insert into stock(Blood_Group,Quantity) values('AB-',5);")
        cur.execute("insert into stock(Blood_Group,Quantity) values('O+',5);")
        cur.execute("insert into stock(Blood_Group,Quantity) values('O-',5);")
        con.commit()
        print()
load()
