#Python-SQL connector installation required
import mysql.connector as SQL

MyDB=SQL.connect(host='localhost',user='root',password='insertpasswordhere',database='insertDBhere')
MyCursor=MyDB.cursor()

print("Your Connection ID is: ",MyDB.connection_id)

print("***ADDRESS BOOK***")
print("Choose 1 to display all names with details in order of DOB")
print("Choose 2 to search by name")
print("Choose 3 to add a new person with details")
print("Choose 4 to update details of a person, searched by Person's ID")
print("Choose 5 to delete a person by Person's ID")
print("Choose 6 to quit")
choice=0
while choice!=6:
    choice=input("Enter your choice: ")
    if choice=="1":
        print("NAMES WITH DETAILS: ")
        MyCursor.execute("SELECT * FROM PERSONS ORDER BY DOB ASC;")
        myresult = MyCursor.fetchall()
        print("Shown in order: Person ID, Name, Date of birth, Relation, Address, Email, Mobile")
        for i in myresult:
            print(i)
    elif choice=="2":
        sql="SELECT * FROM PERSONS WHERE NAME=%s"
        namer=input("Enter name to be searched: ")
        namey=(namer,)
        MyCursor.execute(sql, namey)
        myresult = MyCursor.fetchall()
        for i in myresult:
            print(i)
    elif choice=="3":
        PID=input("Enter Person's ID: ")
        Name=input("Enter name: ")
        DOB=input("Enter date of birth: ")
        Relation=input("Enter Relation: ")
        Address=input("Enter Address: ")
        Email=input("Enter Email: ")
        Mobile=input("Enter Mobile: ")
        sql="INSERT INTO PERSONS (PID,NAME,DOB,RELATION,ADDRESS,EMAIL,MOBILE) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val=(PID, Name, DOB, Relation, Address, Email, Mobile)
        MyCursor.execute(sql,val)
        MyDB.commit()
        print("Info has been entered.")

    elif choice=="4":
        PID=input("Enter ID whose information has to be updated: ")
        Name=input("Enter name: ")
        DOB=input("Enter date of birth: ")
        Relation=input("Enter Relation: ")
        Address=input("Enter Address: ")
        Email=input("Enter Email: ")
        Mobile=input("Enter Mobile: ")
        sql="UPDATE PERSONS SET NAME=%s,DOB=%s,RELATION=%s,ADDRESS=%s,EMAIL=%s,MOBILE=%s WHERE PID=%s"
        val=(Name, DOB, Relation, Address, Email, Mobile, PID)
        MyCursor.execute(sql,val)
        MyDB.commit()
        print("Info has been updated.")
    elif choice=="5":
        PID=input("Enter ID whose information has to be deleted: ")
        sql = "DELETE FROM PERSONS WHERE PID = %s"
        val=(PID,)
        MyCursor.execute(sql,val)
        MyDB.commit()
        print("Info has been deleted.")
    elif choice=="6":
        print("Thank you for using my program!")
        break

print("Session finished")

