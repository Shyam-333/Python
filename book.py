import sqlite3
MyBook=sqlite3.connect('booktest.db')
curbook=MyBook.cursor()
title=input("Enter Title:-- ")
author=input("Enter Author:-- ")
price=input("Enter Price:-- ")
curbook.execute('''INSERT INTO Books(Title,Author,Price) VALUES (?,?,?);''',(title,author,price))
MyBook.commit()
