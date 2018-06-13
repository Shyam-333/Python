import sqlite3
MySchool=sqlite3.connect('schooltest.db')

nm=input("Enter name:")

sql="SELECT * from student WHERE name=' "+nm+" ';"
curschool=MySchool.cursor()
curschool.execute(sql)
record = curschool.fetchone()
print(record)
m=float(input("Enter new marks:"))
sql="UPADTE student SET marks=' "+str(m)+" ' WHERE name=' "+nm+" ';"
try:
    curschool.execute(sql)
    MySchool.commit()
    print("record updated successfully")
except:
    print("error in update operation")
    MySchool.rollback()




#mysid= int (input("Enter ID:  "))
#myname= input("Enter name:  ")
#myage= int (input("Enter house:  "))
#mymarks= float (input("Enter marks:  "))

#try block to catch exceptions
#try:
 #   curschool=MySchool.cursor()
  #  curschool.execute("INSERT INTO student (StudentID, name, age, marks) VALUES (?,?,?,?);",(mysid,myname,myage,mymarks))
   # MySchool.commit()
    #print("One record added successfully")

#except block to handle exceptions
#except:
     #   print("Error in operation.")
      #  MySchool.rollback()

#MySchool.close()
