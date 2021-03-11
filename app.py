
#how do you get the right value from DB?


import tkinter as tk
#import main
from tkinter import *
import sqlite3
root = tk.Tk()
root.title('GPA calculator')
root.configure(bg="black")
connect = sqlite3.connect('classes.db')
c= connect.cursor()
#how to create a table
# c.execute("DROP TABLE clases")
# c.execute(""" CREATE TABLE clases   
#  (        	id INTEGER,
#   			VALUE INTEGER,
#  			GPA INTEGER
 			


 			
#  			)
#   			""" )
# connect.commit()
# 
label =Label(root,text='GPA calculator',bg='black',fg='blue')
label.grid(row=0, columnspan=6)
label1=Label(root, text='enter a grade value',bg='black',fg='blue')
label1.grid(row=1, column=0)
enter=Entry(root)
enter.grid(row=1,column=1)


#add values to the data base
def ADDING():
	#define gpa and value and storage in data base, # only called a single time 
	Id=0
	gpa =0
	value=0

	while value!=100:
		value+=1
		Id+=1
		# c.execute(" INSERT INTO clases VALUES (:value :gpa,)",{'value': value, 'gpa':gpa } )
		# connect.commit()
		# connect.close()
		if value<=64:
			gpa=0
		elif value >64 and value<67:
			gpa=1
		elif value >66 and value<70:
			gpa=1.3
		elif value >71 and value<73:
			gpa=1.7
		elif value >74 and value<77:
			gpa=2
		
		elif value >78 and value<80:
			gpa=2.3
		elif value >81 and value<83:
			gpa=2.7
		elif value >84 and value<87:
			gpa=3
		elif value >88 and value<90:
			gpa=3.3
		elif value >91 and value<93:
			gpa=3.7
		elif value >94 and value<97:
			gpa=4
		
		c.execute(" INSERT INTO clases VALUES (:id,:value, :gpa)",{'id':Id, 'value': value, 'gpa':gpa } )
		connect.commit()
		#connect.close()

#function to acces data base based on user input
def convert():
	var=enter.get()

	enter.delete(0,END)
	c.execute(" SELECT * FROM clases WHERE id=? AND value=?",(var,var) ) 
	db = c.fetchone()
	enter.insert(0,db[2])
	
	connect.commit()


#print out values from data base

def returning():
	c.execute("SELECT * FROM clases")
	db=c.fetchall()
	for i in db:

		print(i)
# returning()

button =Button(root, text='convert to GPA', highlightbackground="green",command=convert)
button.grid(row=1,column=3)

root.mainloop()
connect.close()