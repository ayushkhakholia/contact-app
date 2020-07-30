
def addcontact(db, name, number):
    cur1=db.cursor()
    cur1.execute('select *from contactapp where phone=?',(number,))
    display1 = cur1.fetchall()
    cur2= db.cursor()
    cur2.execute('select *from contactapp where name=?', (name,))
    display2 = cur2.fetchall()

    if  display1!=[]:
        print("Number already exists")
    elif display2!=[]:
        print("Name  already exists")
    else:
            cur1.execute('insert into contactapp values(?,?)', (name,number))
            db.commit()
def viewcontact(db):
    cur=db.cursor()
    cur.execute('select *from contactapp')
    display=cur.fetchall()
    print('contacts:',display)
    db.commit()
def deletecontactusingnumber(db,number):
    cur = db.cursor()
    cur.execute('select *from contactapp where phone=?',(number,))
    display = cur.fetchall()
    if  display==[]:
         print("Contact cannot be deleted as no such number  exists")
    else:
         cur.execute('delete from contactapp where phone=?',(number,))
    db.commit()
def updatecontactusingname(db,name,number):
    cur = db.cursor()
    cur.execute('select *from contactapp where name=?', (name,))
    display = cur.fetchall()
    if display == []:
        print("Contact cannot be updated as No such name exists")
    else:
         cur.execute('update contactapp set phone=? where name=?',(number,name))
         db.commit()
def updatecontactusingnumber(db,name,number):
    cur = db.cursor()
    cur.execute('select *from contactapp where phone=?', (number,))
    display = cur.fetchall()
    if display == []:
        print("Contact cannot be updated as No such number exists")
    else:
        cur.execute('update contactapp set name=? where phone=?',(name,number))
        db.commit()

def deletecontactusingname(db,name):
    cur = db.cursor()
    cur.execute('select *from contactapp where name=?',(name,))
    display = cur.fetchall()
    if  display==[]:
         print("Contact cannot be deleted as no such name  exists")
    else:
         cur.execute('delete from contactapp where name=?',(name,))
    db.commit()

