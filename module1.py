import pymysql

con=pymysql.connect(host='b9oxiichqfr42xvylzpl-mysql.services.clever-cloud.com',user='u5qyaqclnb8ayqg2',password='2vM1k3YsOaZaymOZs6hT',database='b9oxiichqfr42xvylzpl')
curs=con.cursor()
print('Enter Correct choice...')
nm=int(input('1:View Books  '
             '2:Add Book into the library  '
             '3:Search book  '
             '4:Delete Book '
             '5:Update Info Book '
             '6:Addition New Table '
             '7:Exit :: '))
if nm == 1:
    gen=input("Enter the Genre of the books : ")
    try:
        curs.execute("select * from Books where Genre='%s'"%gen.capitalize())
        data=curs.fetchall()
        #print(data)
        for rec in data:
            print('Bookcode= %d :: Bookname= %s'%(rec[0],rec[1]))
    except Exception as E:
        print(E)

elif nm == 2:
    cd = int(input('Enter Book Code : '))
    nm = input('Enter Book Name : ')
    ath = input('Enter Book Author : ')
    prz = float(input('Enter Book price : '))
    gen = input('Enter Genre of Book : ')

    try:
        curs.execute("insert into Books values(%d,'%s','%s',%.2f,'%s')" % (cd,nm,ath,prz,gen))
        con.commit()
        print('New Book Added Succesfully.....')
    except Exception as E:
        print(E)

elif nm == 3:
    no=int(input("Enter Book Code : "))
    try:
        curs.execute("select * from Books where Bookcode=%d"%no)
        data=curs.fetchone()
        print('Bookcode= %d :: Bookname= %s :: Author=%s :: Price=%.2f'%(data[0],data[1],data[2],data[3]))
    except Exception as E:
        print(E)

elif nm == 4:
    try:
        no=int(input("Enter your Book Code number: "))
        print("delete from Books where Bookcode=%d"%no)
        curs.execute("select * from Books where BookCode=%d"%no)
        data=curs.fetchone()
        if data:
            print(data)
            ch=input(print('Are you surely want to delete ?? _'))
            if ch=='yes':
                curs.execute("delete from Books where Bookcode=%d"%no)
                con.commit()
                print("Book is Deleted.....")
            else:
                print('Book not Deleted...')
        else:
            print("Book not found....")
    except Exception as e:
        print(e)

elif nm == 5:
    try:
        no=int(input('Enter Book Code : '))
        curs.execute("select * from Books where Bookcode=%d"%no)
        data=curs.fetchone()
        if data:
            print(data)
            ch=int(input("Enter Choice for update Prize enter 1 for update Bookcode Enter 2  "))
            if ch == 1:
                pz=float(input("Enter new Price : "))
                curs.execute("update Books set Price=%.2f where Bookcode=%d"%(pz,no))
                con.commit()
                print("Price Update Successfully...")
            elif ch == 2:
                bc=int(input("enter new code : "))
                curs.execute("update Books set Bookcode=%d where Bookcode=%d"%(bc,no))
                con.commit()
                print("Bookcode Update Successfully...")
            else:
                print('You entered Wrong Choice..')
        else:
            print("book not Found...")
    except Exception as e:
        print(e)

elif nm==6:
    try:
        tb=input("Enter the New Table Name : ")
        curs.execute("alter table Books add %s varchar(10)"%tb)
        print("Table Added Successfully...")
    except Exception as e:
        print(e)


elif nm==7:
    print("Thank you for Using this code 😊😊")

else:
    print("You Entered the Wrong Choice...")

con.close()