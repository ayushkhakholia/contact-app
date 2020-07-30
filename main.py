import contacthub as dab
import sqlite3


db=sqlite3.connect('contactapp.db')
db.cursor().execute('create table if not exists' + ' contactapp(name text, phone text) ')

def printfunc():
    print("Enter 1 for add")
    print("Enter 2 for viewcontact")
    print("Enter 3 for updatecontactusingname")
    print("Enter 4 for updatecontactusingnumber")
    print("Enter 5 for deleteecontactusingnumber")
    print("Enter 6 for deleteecontactusingname")
    print("Enter 7 or any other key to exit")

i=2
while i!= 7:

    printfunc()
    try:
         i=int(input("Enter the task you would like to do"))
    except:
        print("Please enter a valid input")
        continue
    if i == 1:
        name = input("Enter the name you would like to add")
        number = input("Enter the number")

        dab.addcontact(db,name,number)

    elif i == 2:

        dab.viewcontact(db)

    elif i == 3:

         name = input("Enter the name for which you would like to update the phone number")
         number = input("Enter the updated phone no.")
         dab.updatecontactusingname(db,name,number)

    elif i == 4:

         number= input("Enter the number for which you would like to update the name")
         name=input("Enter the updated name")
         dab.updatecontactusingnumber(db,name,number)

    elif i==5:

         number = input("Enter the contact numner you would like to delete")
         dab.deletecontactusingnumber(db, number)

    elif i==6:
        name = input("Enter the contact name you would like to delete")
        dab.deletecontactusingname(db, name)

    elif i==7:
        exit()
    else:
        print("Please enter a valid number")
        continue

db.commit()
db.close()

