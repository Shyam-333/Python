import sqlite3
MyBook=sqlite3.connect('booktest.db')

str=input("Book Title:-- ")
sql="SELECT * from Books WHERE Title='"+str+"';"

curbook=MyBook.cursor()
curbook.execute(sql)
record=curbook.fetchone()
print(record)

sql="SELECT Price from Books WHERE Title='"+str+"';"
curbook=MyBook.cursor()
curbook.execute(sql)
record1=int()
record1=curbook.fetchone()


cost=float()
cost1=float()
c=int(input("No of copies:-- "))
d=input("Add more books? Y/N ")
if d=='N':
    cost=c*record1
    print('Total Cost:--')
    print(cost)
else:
    e=input("More copies--")
    cost1=record1*(c+e)
    print('Total Cost:--'+cost1)

    
