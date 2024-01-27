import mysql.connector as a
#password = str(input("Enter Your Database Password:- "))
con = a.connect(host="localhost", user="root", passwd= "",port=3306)

#Database Selection

sqlquery = con.cursor()
sqlquery.execute("show databases")
d1 = sqlquery.fetchall()
d2 = []
for i in d1:
    d2.append(i[0])
if 'bshop' in d2:
    msql ="use bshop"
    sqlquery.execute(msql)
else:                                       #Create Database If Dose not exist
    sql1 ="create database bshop"
    sqlquery.execute(sql1)
    sql2 = "use bshop"
    sqlquery.execute(sql2)
    sql3 = """create table book (Name varchar(50),Author varchar(50),CostPrice integer,SellPrice integer,Date varchar(20))"""
    sqlquery.execute(sql3)
    sql4 = """create table customer (Name varchar(20), Book varchar(25), Payment varchar(25), Date varchar(25), Phone varchar(11))"""
    sqlquery.execute(sql4)
    sql5 = """create table bill (Details varchar(20), Cost integer, Date varchar(25))"""
    sqlquery.execute(sql5)
    sql6 = """create table worker (Name varchar(100), Work varchar(20), Salary varchar(20))"""
    sqlquery.execute(sql6)
    con.commit()

#System Login Password
def signin():
    print("\n")
    print("------------->>>>>>>>>>>>>Welcome To Book Shop Bangladesh<<<<<<<<<<<<<-------------")
    print("\n")
    p = input("Enter you System password:- ")
    if p =="Uzzal":
        options()
    else:
        signin()

#Project Work Options
def options():
    print("""
                                    FIFOTech Book Shop
          --------------------------------------------------------------------
          1. Add Book                               5. Display Books
          2. Sell Book                              6. Display Payments
          3. Add Bill                               7. Display Bills
          4. Add Workers                            8. Display Workers
          --------------------------------------------------------------------
        """)
    choice = input("Select Options:- ")
    while True:
        if (choice == '1'):
            AddBook()
        elif (choice == '2'):
            SellBook()
        elif (choice == '3'):
            AddBill()
        elif (choice == '4'):
            AddWorkers()
        elif (choice == '5'):
            DisplayBooks()
        elif (choice == '6'):
            DisplayPayments()
        elif (choice == '7'):
            DisplayBills()
        elif (choice == '8'):
            DisplayWorkers()
        else:
            print("Enter Again.........")
            options()
    

#Add Options 
            
def AddBook():
    n = input("Name:- ")
    a = input("Autho:- ")
    c = input("Cost Price:- ")
    s = input("Salling Price:- ")
    d = input("Date:- ")
    data = (n,a,c,s,d)
    sql = 'insert into book values(%s,%s,%s,%s,%s)'
    sqlquery.execute(sql,data)
    con.commit()
    print("Data Insert Successfully")
    options()

def SellBook():
    n = input("Name:- ")
    s = input("Book Name:- ")
    Py = input("Payments:- ")
    d = input("Date:- ")
    p = input("Phone Number:- ")
    data = (n,s,Py,d,p)
    sql = 'insert into customer values(%s,%s,%s,%s,%s)'
    sqlquery.execute(sql,data)
    con.commit()
    print("Data Insert Successfully")
    options()

def AddBill():
    dt = input("Details:- ")
    c = input("Cost:- ")
    d = input("Date:- ")
    data = (dt,c,d)
    sql = 'insert into bill values(%s,%s,%s)'
    sqlquery.execute(sql,data)
    con.commit()
    print("Data Insert Successfully")
    options()

def AddWorkers():
    n = input("Worker Name:- ")
    w = input("Works:- ")
    s = input("Salary:- ")
    data = (n,w,s)
    sql = 'insert into worker values(%s,%s,%s)'
    sqlquery.execute(sql,data)
    con.commit()
    print("Data Insert Successfully")
    options()

#Display Option
def DisplayBooks():
    DispDate = input("Date:- ")
    displaysql = 'select * from book'
    c = con.cursor()
    sqlquery.execute(displaysql)
    d = sqlquery.fetchall()
    for i in d:
        if i[4]==DispDate:
            print("Name:- ",i[0],"Author:-",i[1],"Cost:-",i[2],"Buy:-",i[3],"Date:-",i[4],)
            print("-------------------------------------------------------------")
    options()
    

def DisplayPayments():
    DispDate = input("Date:- ")
    displaysql = 'select * from customer'
    c = con.cursor()
    sqlquery.execute(displaysql)
    d = sqlquery.fetchall()
    for i in d:
        if i[3]==DispDate:
            print("Name:- ",i[0],"Book:-",i[1],"Payments:-",i[2],"Date:-",i[3],"Phone Number:-",i[4],)
            print("-------------------------------------------------------------")
    options()

def DisplayBills():
    DispDate = input("Date:- ")
    displaysql = 'select * from bill'
    c = con.cursor()
    sqlquery.execute(displaysql)
    d = sqlquery.fetchall()
    for i in d:
        if i[2]==DispDate:
            print("Details:- ",i[0],"Cost:-",i[1],"Date:-",i[2])
            print("-------------------------------------------------------------")
    options()

def DisplayWorkers():
    displaysql = 'select * from worker'
    c = con.cursor()
    sqlquery.execute(displaysql)
    d = sqlquery.fetchall()
    for i in d:
        print("Name:- ",i[0],"Work:-",i[1],"Salary:-",i[2])
        print("-----------------------------------------------------------------")
    options()


signin()