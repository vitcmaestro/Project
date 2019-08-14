import pymysql
import string

conn  = pymysql.connect(host='localhost',user='root',password='meenasekar10',db='Real_Estate',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
print("Connection successful")
cur = conn.cursor()
print("Welcome to SpitiGi")
print("You can buy/sell lands,houses,villa,flats and so on!!!")
custype = input("Do you want to sell or buy ")
custype = custype.lower()
data = []
entry = 0
count = 30005
if(custype == "buy"):
    buyerlog = input("SpitGi wants to know whether you are a new customer or not old/new :")
    if(buyerlog.lower() == "old"):
        userid = input("Enter your userID")
        password = input("Enter your password")
        s1= "Select * from authentication where userID = (%s) AND Password= (%s)"
        acur = conn.cursor()
        acur.execute(s1,(userid,password))
        data = acur.fetchall()
        if(data == None):
            print("password and id mismatching")
        else:
            print(data)
            print("Login successful")
        entry = 1
    elif(buyerlog.lower() == "new"):
        newuser = input("Enter a username")
        newpaswrd = input("Enter a new password")
        i1 = "insert into authentication(userid,password) values((%s),(%s))"
        acur = conn.cursor()
        acur.execute(i1,(newuser,newpaswrd))
        conn.commit()
        a1 = newuser
        b1 = input("Enter your name")
        c1 = input("Enter your e-mail ID")
        d1 = input("Enter your phone number")
        e1 = input("Enter your pincode")
        i2 = "Insert into buyerinfo(userID,user_name,EmailID,phone_num,pincode) values (%s,%s,%s,%s,%s,%s)"
        bcur = conn.cursor()
        bcur.execute(i2,(a1,b1,c1,d1,e1))
        conn.commit()
        a2 = e1
        b2 = input("Enter your address")
        c2 = input("Enter your state")
        d2 = input("Enter your country")
        i3 = "insert into buyerresidence(pincode,address,state,country) values (%s,%s,%s,%s,%s)"
        ccur = conn.cursor()
        ccur.execute(i3,(a2,b2,c2,d2))
        conn.commit()
        print("Registration successful")
    else:
        print("We are sorry sir, SpitiGi could not understand your needs on buyer side, Kindly say it in it's own language")
elif(custype == "sell"):
    sellerlog = input("SpitGi wants to know whether you are a new customer or not old/new :")
    if(sellerlog.lower() == "old"):
        userid = input("Enter your userID")
        password = input("Enter your password")
        s2 = "Select * from authentication where userID = (%s) AND Password= (%s)"
        acur = conn.cursor()
        acur.execute(s2,(userid,password))
        data = acur.fetchall()
        if(data == None):
            print("password and id mismatching")
        else:
            print(data)
            print("Login successful")
        entry = 2
    elif(sellerlog.lower() == "new"):
        newuser = input("Enter a username")
        newpaswrd = input("Enter a new password")
        i4 = "insert into authentication(user_id,password) values((%s),(%s))"
        acur = conn.cursor()
        acur.execute(i4,(newuser,newpaswrd))
        conn.commit()
        a1 = input("Enter your name")
        b1 = input("Enter the type of contact owner/business")
        if(b1.lower() == "business"):
            c1 = input("enter your company name")
        elif(b1.lower() == "owner"):
            c1 = "null"
        else:
            print("Invalid value")
        d1 = input("Enter your phone number")
        e1 = input("Enter residential pincode")
        i5 = "Insert into sellerinfo(userID,seller_name,seller_type,company_name,phone_num,pincode) values (%s,%s,%s,%s,%s,%s)"
        bcur = conn.cursor()
        bcur.execute(i5,(newuser,a1,b1,c1,d1,e1))
        conn.commit()
        a2 = e1
        b2 = input("Enter your address")
        c2 = input("Enter your state")
        d2 = input("Enter your country")
        i3 = "insert into sellerresidence(pincode,address,state,country) values (%s,%s,%s,%s,%s)"
        ccur = conn.cursor()
        ccur.execute(i3,(a2,b2,c2,d2))
        conn.commit()
        print("Registration successful")
    else:
        print("We are sorry sir, SpitiGi could not understand your needs on seller side , Kindly say it in it's own language")
    
else:
    print("We are sorry sir, SpitiGi could not understand your needs, Kindly say it in it's own language")



if(entry == 1):
    print("How do you want to search the property\n")
    print("1.land")
    print("2.house")
    print("3.Flat")
    buychoice = int(input(""))
    print("Select your location")
    print("The available places are.......")
    placestmt = "SELECT location FROM property_detail"
    a2cur = conn.cursor()
    a2cur.execute(placestmt)
    data = a2cur.fetchall()
    print(list(data))
    x = input("Would you like to continue y/n")
    if(x.lower() == 'y'):
        bcstmt =  "Select property_id,property_type,property_status,area_range,location,sale_rate FROM property_detail WHERE property_type = (%s)"
        b2cur = conn.cursor()
        b2cur.execute(bcstmt,buychoice)
        data = b2cur.fetchall()
        for i in data:
            print(data)
    else:
        print("Thank you for using SpitGi")
elif(entry == 2):
    print("do you want to look upon your old property_details or you want to register for a new one old/new")
    sellchoice = input("")
    if(sellchoice.lower() == "old"):
        s4 = "select userID from sellerinfo where userID = %s"
        a3cur = conn.cursor()
        a3cur.execute(s4,userid)
        sid = []
        sid=a3cur.fetchall()
        print(sid)
        s3 = "select prperty_type,property_status,area_range,location from property_detail where seller_id = %s"
        b3cur=conn.cursor()
        b3cur.execute(s3,sid[1])
        data=b3cur.fetchall
        for i in data:
            print(data)
    elif(sellchoice.lower() == "new"):
        ptype = input("Enter the property type land/flat/house")
        pstatus = input("Enter the status on-process/for-sale")
        loc = input("Enter the location")
        salerate = float(input("Enter the sale rate"))
        area = float(input("Enter the total area in square km"))
        s4 = "Insert into property_detail(property_type,property_status,location,sale_rate,area_range) values(%s,%s,%s,%s,%s)"
        a3cur = conn.cursor()
        a3cur.execute(s4,(ptype,pstatus,loc,salerate,area))
        conn.commit()
    else:
        print("Invalid entry")
else:
    print("Thank you")
