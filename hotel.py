from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
import tkinter as tk
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strftime




root=Tk()
root.title("Hotel Management System")
root.geometry("1450x800+0+0")

var_ref=StringVar() 	#heh string use kelay karanki kahi calculations ikde perform karayche nahi aahet
x=random.randint(1000,9999) #ya x variable madhe data store honaar
var_ref.set(str(x))

var_cust_name=StringVar()
var_mother=StringVar()
var_gender=StringVar()
var_post=StringVar()
var_mobile=StringVar()
var_email=StringVar()
var_nationality=StringVar()
var_idproof=StringVar()
var_idnumber=StringVar()
var_address=StringVar()


############## Variables of rooms #############
var_contact=StringVar()
var_checkin=StringVar()
var_checkout=StringVar()
var_roomtype=StringVar()
var_roomavailable=StringVar()
var_meal=StringVar()
var_noofdays=StringVar()
var_paidtax=StringVar()
var_actualtotal=StringVar()
var_total=StringVar()





def f1():
	#root.withdraw()
	cw.deiconify()
def f2():
	rw.deiconify()
def f3():
	dw.deiconify()
def f4():
	rew.deiconify()

def add_data():
	if var_mobile.get()==""or var_mother.get()=="":
		messagebox.showinfo("Error","All fields are required",parent=cw)
	else:
		try:
			conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
			my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
			my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
												var_ref.get(),
												var_cust_name.get(),
												var_mother.get(),
												var_gender.get(),
												var_post.get(),
												var_mobile.get(),
												var_email.get(),
												var_nationality.get(),
												var_idproof.get(),
												var_idnumber.get(),
												var_address.get()
											))
			conn.commit()
			fetch_data()
			conn.close()
			messagebox.showinfo("Success","Customer has been added",parent=cw)
		except Exception as e:
			messagebox.showwarning("Warning",f"Something went Wrong:{str(e)}",parent=cw)		

"""def fetch_data():
	conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
	my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
	my_cursor.execute("select * from customer")
	rows=my_cursor.fetchall()	#hya rows valya variable madhe data sagla fetch honaar
	if len(rows)!=0:
		Cust_Details_Table.delete(*Cust_Details_Table.get_children())	#get children manje colums che childrens
		for i in rows:
			Cust_Details_Table.insert("",END,values=i)
		conn.commit()
	conn.close()
def get_cursor(event=""):
	cursor_row=Cust_Details_Table.focus()
	content=Cust_Details_Table.item(cursor_row)	#joh pan scrollbar valya frame madhe data present aaahe to tithe visible hoyayla paije manjech customer details madhe
	row=content["values"]
		
	var_ref.set(row[0]),
	var_cust_name.set(row[1]),
	var_mother.set(row[2]),
	var_gender.set(row[3]),
	var_post.set(row[4]),
	var_mobile.set(row[5]),
	var_email.set(row[6]),
	var_nationality.set(row[7]),
	var_idproof.set(row[8]),
	var_idnumber.set(row[9]),
	var_address.set(row[10])"""

def update():
	if var_mobile.get()=="":
		messagebox.showerror("Error","Please Enter Mobile Number",parent=cw)
	else:
		conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
		my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
		my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
																				
																				var_cust_name.get(),
																				var_mother.get(),
																				var_gender.get(),
																				var_post.get(),
																				var_mobile.get(),
																				var_email.get(),
																				var_nationality.get(),
																				var_idproof.get(),
																				var_idnumber.get(),
																				var_address.get(),
																				var_ref.get()	#hyala ref la last la lilay karanki tychya through update karaycha aahe																					
																				))
		conn.commit()
		fetch_data()	#update kelya nantar lagech updated data fetch hoyayla paije 
		conn.close()
		messagebox.showinfo("Update","Customer Details are Sucessfully Updated",parent=cw)

def delete():
	delete=messagebox.askyesno("Hotel Management System","Do you really want to delete the customer details",parent=cw)
	if delete>0:
		conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
		my_cursor=conn.cursor()	
		query="delete from customer where Ref = %s"
		value=(var_ref.get(),)
		my_cursor.execute(query,value)
		messagebox.showinfo("Success","Customer details Successfully Deleted",parent=cw)
	else:
		if not delete:
			return
	conn.commit()
	fetch_data()
	conn.close()

def reset():
	#var_ref.set(""),
	var_cust_name.set(""),
	var_mother.set(""),
	#var_gender.set(""),
	var_post.set(""),
	var_mobile.set(""),
	var_email.set(""),
	#var_nationality.set(""),
	#var_idproof.set(""),
	var_idnumber.set(""),
	var_address.set("")
	
	x=random.randint(1000,9999) #ya x variable madhe data store honaar
	var_ref.set(str(x))

def search():
	conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
	my_cursor=conn.cursor()	

	my_cursor.execute("select * from customer where "+str(search_var.get())+" LIKE '%"+str(txt_search.get())+"%'")
	rows=my_cursor.fetchall()	#hya rows valya variable madhe data sagla fetch honaar
	if len(rows)!=0:
		Cust_Details_Table.delete(*Cust_Details_Table.get_children())	#get children manje colums che childrens
		for i in rows:
			Cust_Details_Table.insert("",END,values=i)
		conn.commit()
	conn.close()
	
def fetch_data():
	conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
	my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
	my_cursor.execute("select * from customer")
	rows=my_cursor.fetchall()	#hya rows valya variable madhe data sagla fetch honaar
	if len(rows)!=0:
		Cust_Details_Table.delete(*Cust_Details_Table.get_children())	#get children manje colums che childrens
		for i in rows:
			Cust_Details_Table.insert("",END,values=i)
		conn.commit()
	conn.close()
def get_cursor(event=""):
	cursor_row=Cust_Details_Table.focus()
	content=Cust_Details_Table.item(cursor_row)	#joh pan scrollbar valya frame madhe data present aaahe to tithe visible hoyayla paije manjech customer details madhe
	row=content["values"]
		
	var_ref.set(row[0]),
	var_cust_name.set(row[1]),
	var_mother.set(row[2]),
	var_gender.set(row[3]),
	var_post.set(row[4]),
	var_mobile.set(row[5]),
	var_email.set(row[6]),
	var_nationality.set(row[7]),
	var_idproof.set(row[8]),
	var_idnumber.set(row[9]),
	var_address.set(row[10])

#################################### Add room data########################
def add_datarw():
	if var_contact.get()==""or var_checkin.get()=="":
		messagebox.showinfo("Error","All fields are required",parent=rw)
	else:
		try:
			conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
			my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
			my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
											var_contact.get(),
											var_checkin.get(),
											var_checkout.get(),
											var_roomtype.get(),
											var_roomavailable.get(),
											var_meal.get(),
											var_noofdays.get()
										))
			conn.commit()
			fetch_datarw()
			conn.close()
			messagebox.showinfo("Success","Room Details has been added",parent=rw)
		except Exception as e:
			messagebox.showwarning("Warning",f"Something went Wrong:{str(e)}",parent=rw)
######################Update room details #####################
def update1():
	if var_contact.get()=="":
		messagebox.showerror("Error","Please Enter valid room number",parent=rw)
	else:
		conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
		my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
		my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
															
															var_checkin.get(),
															var_checkout.get(),
															var_roomtype.get(),
															var_roomavailable.get(),
															var_meal.get(),
															var_noofdays.get(),																		
															var_contact.get()	#hyala contact la last la lilay karanki tychya through update karaycha aahe				
														))
																				
																				
		conn.commit()
		fetch_datarw()	#update kelya nantar lagech updated data fetch hoyayla paije 
		conn.close()
		messagebox.showinfo("Update","Room Details are Sucessfully Updated",parent=rw)

		
def deleter():
	if var_contact.get()=="":
			messagebox.showinfo("error","please enter mobile number",parent=rw)
	else:
		
		delete=messagebox.askyesno("Hotel Management System","Do you really want to delete the customer room details",parent=rw)
	
	if delete>0:
		conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
		my_cursor=conn.cursor()	
		query="delete from room where contact = %s"
		value=(var_contact.get(),)
		my_cursor.execute(query,value)
		messagebox.showinfo("Success","Customer room details Successfully Deleted",parent=rw)
	else:
		if not delete:
			return
	
	conn.commit()
	fetch_datarw()
	conn.close()


def resetr():
	#var_ref.set(""),
	var_contact.set(""),
	var_checkin.set(""),
	#var_gender.set(""),
	var_checkout.set(""),
	var_roomtype.set(""),
	var_roomavailable.set(""),
	#var_nationality.set(""),
	#var_idproof.set(""),
	var_meal.set(""),
	var_noofdays.set("")
	var_paidtax.set("")
	var_actualtotal.set("")
	var_total.set("")
	
	
	x=random.randint(1000,9999) #ya x variable madhe data store honaar
	var_ref.set(str(x))

def total():
	inDate=var_checkin.get()
	outDate=var_checkout.get()
	inDate=datetime.strptime(inDate,"%d/%m/%Y")	#date cha format
	outDate=datetime.strptime(outDate,"%d/%m/%Y")
	var_noofdays.set(abs(outDate-inDate).days)
	
	if(var_meal.get()=="Breakfast" and var_roomtype.get()=="Single"):
		q1=float(2000)
		q2=float(5000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	elif(var_meal.get()=="Breakfast" and var_roomtype.get()=="Luxury"):
		q1=float(2000)
		q2=float(10000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	elif(var_meal.get()=="Breakfast" and var_roomtype.get()=="Double"):
		q1=float(2000)
		q2=float(7000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	elif(var_meal.get()=="Lunch" and var_roomtype.get()=="Single"):
		q1=float(3500)
		q2=float(5000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	elif(var_meal.get()=="Lunch" and var_roomtype.get()=="Double"):
		q1=float(3500)
		q2=float(7000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	elif(var_meal.get()=="Lunch" and var_roomtype.get()=="Luxury"):
		q1=float(3500)
		q2=float(10000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	elif(var_meal.get()=="Dinner" and var_roomtype.get()=="Single"):
		q1=float(3600)
		q2=float(5000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	elif(var_meal.get()=="Dinner" and var_roomtype.get()=="Double"):
		q1=float(3600)
		q2=float(7000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)

	else:
		var_meal.get()=="Dinner" and var_roomtype.get()=="Luxury"
		q1=float(3600)
		q2=float(10000)
		q3=float(var_noofdays.get())
		q4=float(q1+q2)
		q5=float(q3+q4)
		Tax="Rs"+str("%.2f"%((q5)*0.09))	#formula aahe
		ST="Rs"+str("%.2f"%((q5)))		#formula aahe
		TT="Rs"+str("%.2f"%(q5+((q5)*0.09)))	#formula aahe
		var_paidtax.set(Tax)
		var_actualtotal.set(ST)
		var_total.set(TT)









#################### Table Frame for room ####################
"""table_frame1=LabelFrame(rw,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
table_frame1.place(x=400,y=275,width=679,height=240)


lblsearch=Label(table_frame1,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
lblsearch.grid(row=0,column=0,sticky=W,padx=2)"""


















	
















def fetch_contact():
	if var_contact.get()=="":
		messagebox.showerror("Error","Please Enter Contact Number",parent=rw)
	else:
		conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
		my_cursor=conn.cursor()
		query=("select Name from customer where Mobile=%s")
		value=(var_contact.get(),)
		my_cursor.execute(query,value)
		row=my_cursor.fetchone()

		if row==None:
			messagebox.showerror("Error","This Number Not Found",parent=rw)	
		else:			
			conn.commit()
			conn.close()
			
			showDataframe=Frame(rw,bd=4,relief=RIDGE,padx=2)
			showDataframe.place(x=400,y=55,width=280,height=200)
		
			lblName=Label(showDataframe,text="Name",font=("arial",5,"bold"))	
			lblName.grid(row=0,column=0)

			lbl=Label(showDataframe,text=row,font=("arial",10,"bold"))
			lbl.grid(row=0,column=1)
######################################################### Gender #############################
			conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
			my_cursor=conn.cursor()
			query=("select Gender from customer where Mobile=%s")
			value=(var_contact.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()
			
			lblGender=Label(showDataframe,text="Gender",font=("arial",5,"bold"))	
			lblGender.grid(row=1,column=0)

			lbl=Label(showDataframe,text=row,font=("arial",10,"bold"))
			lbl.grid(row=1,column=1)
############################################# Email ###################
			conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
			my_cursor=conn.cursor()
			query=("select Email from customer where Mobile=%s")
			value=(var_contact.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone() #hyat query cha data fetch houn yenaar
			
			lblemail=Label(showDataframe,text="Email",font=("arial",5,"bold"))	
			lblemail.grid(row=2,column=0)

			lbl=Label(showDataframe,text=row,font=("arial",8,"bold"))
			lbl.grid(row=2,column=1)
############################################ Nationality ###########################

			conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
			my_cursor=conn.cursor()
			query=("select Nationality from customer where Mobile=%s")
			value=(var_contact.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone() #hyat query cha data fetch houn yenaar
			
			lblnat=Label(showDataframe,text="Nationality",font=("arial",5,"bold"))	
			lblnat.grid(row=3,column=0)

			lbl=Label(showDataframe,text=row,font=("arial",10,"bold"))
			lbl.grid(row=3,column=1)

############################################### Address ###################################

			conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
			my_cursor=conn.cursor()
			query=("select Address from customer where Mobile=%s")
			value=(var_contact.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone() #hyat query cha data fetch houn yenaar
			
			lbladd=Label(showDataframe,text="Address",font=("arial",5,"bold"))	
			lbladd.grid(row=4,column=0)

			lbl=Label(showDataframe,text=row,font=("arial",8,"bold"))
			lbl.grid(row=4,column=1)
############################# Close Window(logout) ######################

def close_root():
	result = messagebox.askyesno("Confirmation", "Are you sure you want to close the window?")
	if result == YES:
		root.quit() 
	


###############################DETAILS ######################
dw=Toplevel(root)
dw.title("Hotel Management System")
dw.geometry("1082x550+188+200")
#cw.resizable(False,False)

def add_datadw():
	if var_floor.get()==""or var_roomno.get()=="":
		messagebox.showinfo("Error","All fields are required",parent=dw)
	else:
		try:
			conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
			my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
			my_cursor.execute("insert into details values(%s,%s,%s)",(
									var_floor.get(),
									var_roomno.get(),
									var_roomType.get()
											
								))
			conn.commit()
			fetch_datadw()
			conn.close()
			messagebox.showinfo("Success","New Room has been added",parent=dw)
		except Exception as e:
			messagebox.showwarning("Warning",f"Something went Wrong:{str(e)}",parent=dw)

######################Update room details #####################
def updatedw():
	if var_floor.get()=="":
		messagebox.showerror("Error","Please Enter valid floor number",parent=dw)
	else:
		conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
		my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
		my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
															
											var_floor.get(),
											var_roomType.get(),
											var_roomno.get()
											
											))
																				
																				
		conn.commit()
		fetch_datadw()	#update kelya nantar lagech updated data fetch hoyayla paije 
		conn.close()
		messagebox.showinfo("Update","New Room Details are Sucessfully Updated",parent=dw)




def deletedw():
	if var_floor.get()=="":
			messagebox.showinfo("error","please enter floor number",parent=dw)
	else:
		
		delete=messagebox.askyesno("Hotel Management System","Do you really want to delete the new room details",parent=dw)
	
	if delete>0:
		conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
		my_cursor=conn.cursor()	
		query="delete from details where Floor = %s"
		value=(var_floor.get(),)
		my_cursor.execute(query,value)
		messagebox.showinfo("Success","New room details Successfully Deleted",parent=dw)
	else:
		if not delete:
			return
	
	conn.commit()
	fetch_datadw()
	conn.close()










table_frame=LabelFrame(dw,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
table_frame.place(x=500,y=50,width=579,height=300)

scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

room_Details_Tabledw=ttk.Treeview(table_frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=room_Details_Tabledw.xview)
scroll_y.config(command=room_Details_Tabledw.yview)




def fetch_datadw():
	conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
	my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
	my_cursor.execute("select * from details")
	rows=my_cursor.fetchall()	#hya rows valya variable madhe data sagla fetch honaar
	if len(rows)!=0:
		room_Details_Tabledw.delete(*room_Details_Tabledw.get_children())	#get children manje colums che childrens
		for i in rows:
			room_Details_Tabledw.insert("",END,values=i)
		conn.commit()
	conn.close()


####################### Detail data  for rw ###########################





def get_cursordw(event=""):
	cursor_row=room_Details_Tabledw.focus()
	content=room_Details_Tabledw.item(cursor_row)	#joh pan scrollbar valya frame madhe data present aaahe to tithe visible hoyayla paije manjech customer details madhe
	row=content["values"]
	var_floor.set(row[0]),
	var_roomno.set(row[1]),
	var_roomType.set(row[2])


room_Details_Tabledw.heading("floor",text="Floor no")
room_Details_Tabledw.heading("roomno",text="Room No")
room_Details_Tabledw.heading("roomType",text="Room Type")


room_Details_Tabledw["show"]="headings"

room_Details_Tabledw.column("floor",width=100)
room_Details_Tabledw.column("roomno",width=100)
room_Details_Tabledw.column("roomType",width=100)



room_Details_Tabledw.pack(fill=BOTH,expand=1) # heh na columns chya arrangement mule vaparlay
room_Details_Tabledw.bind("<ButtonRelease-1>",get_cursordw)	#ha  get_cursor chya funcion la data la customer details madhe anayla madat karto
fetch_datadw()

def resetdw():
	
	var_floor.set(""),
	var_roomno.set(""),
	var_roomType.set("")
	



########################## Logo RW
imgdw=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\logohotel.png")
imgdw=imgdw.resize((230,40),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimgdw=ImageTk.PhotoImage(imgdw)

lbldw=Label(dw,image=photoimgdw,bd=0,relief=RIDGE)
lbldw.place(x=5,y=2,width=230,height=40)



################# Title of DETAILS ###############
lbl_title=Label(dw,text="DETAILS",font=("times ne roman",18,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
lbl_title.place(x=0,y=0,width=1082,height=50)

labelframeleft=LabelFrame(dw,bd=2,relief=RIDGE,text="Rooms to Add",font=("times new roman",12,"bold"),padx=2)
labelframeleft.place(x=5,y=50,width=500,height=300)


################ labels and entrys for details #####################
#floor
var_floor=StringVar()
lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
lbl_floor.grid(row=0,column=0,sticky=W)

enty_floor=ttk.Entry(labelframeleft,textvariable=var_floor,font=("arial",12,"bold"),width=25)
enty_floor.grid(row=0,column=1)

#room no
var_roomno=StringVar()
croomno=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
croomno.grid(row=1,column=0,sticky=W)

txtroomno=ttk.Entry(labelframeleft,textvariable=var_roomno,font=("arial",12,"bold"),width=25)
txtroomno.grid(row=1,column=1)

#room type
var_roomType=StringVar()
roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
roomtype.grid(row=2,column=0,sticky=W)

txtroomtype=ttk.Entry(labelframeleft,textvariable=var_roomType,font=("arial",12,"bold"),width=25)
txtroomtype.grid(row=2,column=1)


########################## dowm Button Frames DETAILS ################################
btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
btn_frame.place(x=0,y=195,width=375,height=35)

#add
btn_add=Button(btn_frame,text="Add",command=add_datadw,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_add.grid(row=0,column=0,padx=1)

#update
btn_update=Button(btn_frame,text="Update",command=updatedw,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_update.grid(row=0,column=1,padx=1)

#delete
btn_delete=Button(btn_frame,text="Delete",command=deletedw,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_delete.grid(row=0,column=2,padx=1)

#reset
btn_res=Button(btn_frame,text="Reset",command=resetdw,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_res.grid(row=0,column=3,padx=1)

################################# Table Frame ###########





"""table_frame=LabelFrame(dw,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
table_frame.place(x=500,y=50,width=579,height=300)

scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

room_Details_Tabledw=ttk.Treeview(table_frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=room_Details_Tabledw.xview)
scroll_y.config(command=room_Details_Tabledw.yview)




def fetch_datadw():
	conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
	my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
	my_cursor.execute("select * from details")
	rows=my_cursor.fetchall()	#hya rows valya variable madhe data sagla fetch honaar
	if len(rows)!=0:
		room_Details_Tabledw.delete(*room_Details_Tabledw.get_children())	#get children manje colums che childrens
		for i in rows:
			room_Details_Tabledw.insert("",END,values=i)
		conn.commit()
	conn.close()


####################### Detail data  for rw ###########################





def get_cursordw(event=""):
	cursor_row=room_Details_Tabledw.focus()
	content=room_Details_Tabledw.item(cursor_row)	#joh pan scrollbar valya frame madhe data present aaahe to tithe visible hoyayla paije manjech customer details madhe
	row=content["values"]
	var_floor.set(row[0]),
	var_roomno.set(row[1]),
	var_roomType.set(row[2])


room_Details_Tabledw.heading("floor",text="Floor no")
room_Details_Tabledw.heading("roomno",text="Room No")
room_Details_Tabledw.heading("roomType",text="Room Type")


room_Details_Tabledw["show"]="headings"

room_Details_Tabledw.column("floor",width=100)
room_Details_Tabledw.column("roomno",width=100)
room_Details_Tabledw.column("roomType",width=100)



room_Details_Tabledw.pack(fill=BOTH,expand=1) # heh na columns chya arrangement mule vaparlay
room_Details_Tabledw.bind("<ButtonRelease-1>",get_cursordw)	#ha  get_cursor chya funcion la data la customer details madhe anayla madat karto
fetch_datadw()"""





dw.withdraw()







############################### 1st img#####################################
img1=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\hotel1.png")
img1=img1.resize((1450,250),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg1=ImageTk.PhotoImage(img1)

lblimg=Label(root,image=photoimg1,bd=4,relief=RIDGE)
lblimg.place(x=0,y=0,width=1450,height=140)

#####################LOGO#########################
img2=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\logohotel.png")
img2=img2.resize((230,140),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg2=ImageTk.PhotoImage(img2)

lblimg=Label(root,image=photoimg2,bd=4,relief=RIDGE)
lblimg.place(x=0,y=0,width=230,height=140)


lbl_title=Label(root,text="HOTEL MANAGEMENT SYSTEM",font=("times ne roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
lbl_title.place(x=0,y=140,width=1350,height=40)

############################### Main Frame ##########################################
main_frame=Frame(root,bd=2,relief=RIDGE)
main_frame.place(x=0,y=180,width=1350,height=620)

####################MEnu $$$$$$$$$$$$$$$$$


lbl_menu=Label(main_frame,text="MENU",font=("times ne roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
lbl_menu.place(x=0,y=0,width=190)

####################### button frame#############################

btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
btn_frame.place(x=0,y=35,width=190,height=180)

cust_btn=Button(btn_frame,text="CUSTOMER",width=18,font=("times ne roman",12,"bold"),bg="black",fg="gold",bd=2,cursor="hand1",relief=RIDGE,command=f1)
cust_btn.grid(row=0,column=0,pady=1)

room_btn=Button(btn_frame,text="ROOM",command=f2,width=18,font=("times ne roman",12,"bold"),bg="black",fg="gold",bd=2,cursor="hand1",relief=RIDGE)
room_btn.grid(row=1,column=0,pady=1)

detail_btn=Button(btn_frame,text="DETAILS",width=18,command=f3,font=("times ne roman",12,"bold"),bg="black",fg="gold",bd=2,cursor="hand1",relief=RIDGE)
detail_btn.grid(row=2,column=0,pady=1)

report_btn=Button(btn_frame,text="REPORT",width=18,command=f4,font=("times ne roman",12,"bold"),bg="black",fg="gold",bd=2,cursor="hand1",relief=RIDGE)
report_btn.grid(row=3,column=0,pady=1)

logout_btn=Button(btn_frame,text="LOGOUT",width=18,command=close_root,font=("times ne roman",12,"bold"),bg="black",fg="gold",bd=2,cursor="hand1",relief=RIDGE)
logout_btn.grid(row=4,column=0,pady=1)


############################### right side image###########################

img3=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\taj.jpg")
img3=img3.resize((1350,590),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg3=ImageTk.PhotoImage(img3)

lblimg=Label(main_frame,image=photoimg3,bd=4,relief=RIDGE)
lblimg.place(x=190,y=0,width=1350,height=590)

############################ down image ###########################


img4=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\myh.jpg")
img4=img4.resize((230,210),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg4=ImageTk.PhotoImage(img4)

lblimg=Label(main_frame,image=photoimg4,bd=3,relief=RIDGE)
lblimg.place(x=0,y=205,width=190,height=190)



img5=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\khana.jpg")
img5=img5.resize((230,210),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg5=ImageTk.PhotoImage(img5)

lblimg=Label(main_frame,image=photoimg5,bd=0,relief=RIDGE)
lblimg.place(x=0,y=395,width=190,height=155)




cw=Toplevel(root)
cw.title("Hotel Management System")
cw.geometry("1082x550+188+200")
#cw.resizable(False,False)

lbl_title=Label(cw,text="ADD CUSTOMER DETAILS",font=("times ne roman",18,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
lbl_title.place(x=0,y=0,width=1082,height=50)

################### Logo ####################
img6=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\logohotel.png")
img6=img6.resize((230,40),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg6=ImageTk.PhotoImage(img6)

lblimg=Label(cw,image=photoimg2,bd=0,relief=RIDGE)
lblimg.place(x=5,y=2,width=230,height=40)

##################### Label Frame #######################
labelframeleft=LabelFrame(cw,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
labelframeleft.place(x=0,y=50,width=400,height=465)


################ labels and entrys #####################
#custref
lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
lbl_cust_ref.grid(row=0,column=0,sticky=W)

enty_ref=ttk.Entry(labelframeleft,textvariable=var_ref,state="readonly",font=("arial",12,"bold"),width=25)
enty_ref.grid(row=0,column=1)

#cust name
cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
cname.grid(row=1,column=0,sticky=W)

txtcname=ttk.Entry(labelframeleft,textvariable=var_cust_name,font=("arial",12,"bold"),width=25)
txtcname.grid(row=1,column=1)

#mother name
mname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
mname.grid(row=2,column=0,sticky=W)

txtmname=ttk.Entry(labelframeleft,textvariable=var_mother,font=("arial",12,"bold"),width=25)
txtmname.grid(row=2,column=1)

#gender name
gname=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
gname.grid(row=3,column=0,sticky=W)

combo_gender=ttk.Combobox(labelframeleft,textvariable=var_gender,font=("arial",12,"bold"),state="readonly")
combo_gender["value"]=("Male","Female","Other")
combo_gender.current(0)
combo_gender.grid(row=3,column=1,sticky=W)


"""txtgname=ttk.Entry(labelframeleft,font=("arial",12,"bold"),width=25)
txtgname.grid(row=3,column=1)"""


#postcode
lblpostcode=Label(labelframeleft,text="PostCode",font=("arial",12,"bold"),padx=2,pady=6)
lblpostcode.grid(row=4,column=0,sticky=W)

txtpostcode=ttk.Entry(labelframeleft,textvariable=var_post,font=("arial",12,"bold"),width=25)
txtpostcode.grid(row=4,column=1)

#mobile
lblmobo=Label(labelframeleft,text="Mobile No",font=("arial",12,"bold"),padx=2,pady=6)
lblmobo.grid(row=5,column=0,sticky=W)

txtmobo=ttk.Entry(labelframeleft,textvariable=var_mobile,font=("arial",12,"bold"),width=25)
txtmobo.grid(row=5,column=1)

#email
lblemail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
lblemail.grid(row=6,column=0,sticky=W)

txtemail=ttk.Entry(labelframeleft,textvariable=var_email,font=("arial",12,"bold"),width=25)
txtemail.grid(row=6,column=1)

#nationality

lblnat=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
lblnat.grid(row=7,column=0,sticky=W)

combo_nat=ttk.Combobox(labelframeleft,textvariable=var_nationality,font=("arial",12,"bold"),state="readonly")
combo_nat["value"]=("India","England","Austraila","USA","New Zealand","Pakistan","South Africa","Germany","Dubai","Singapore","France","Others")
combo_nat.current(0)
combo_nat.grid(row=7,column=1,sticky=W)

"""txtnat=ttk.Entry(labelframeleft,font=("arial",12,"bold"),width=25)
txtnat.grid(row=7,column=1)"""

#id proof type comboboX

lblidproof=Label(labelframeleft,text="Id Proof Type ",font=("arial",12,"bold"),padx=2,pady=6)
lblidproof.grid(row=8,column=0,sticky=W)

combo_idproof=ttk.Combobox(labelframeleft,textvariable=var_idproof,font=("arial",12,"bold"),state="readonly")
combo_idproof["value"]=("Aadhar card","Pan Card","Driving License","Ration Card","Others")
combo_idproof.current(0)
combo_idproof.grid(row=8,column=1,sticky=W)



#id number
lblid=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
lblid.grid(row=9,column=0,sticky=W)

txtid=ttk.Entry(labelframeleft,textvariable=var_idnumber,font=("arial",12,"bold"),width=25)
txtid.grid(row=9,column=1)

#address

lbladd=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
lbladd.grid(row=10,column=0,sticky=W)

txtid=ttk.Entry(labelframeleft,textvariable=var_address,font=("arial",12,"bold"),width=25)
txtid.grid(row=10,column=1)

########################## dowm Button Frames ################################
btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
btn_frame.place(x=0,y=395,width=375,height=35)

#add
btn_add=Button(btn_frame,text="Add",command=add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_add.grid(row=0,column=0,padx=1)

#update
btn_update=Button(btn_frame,text="Update",command=update,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_update.grid(row=0,column=1,padx=1)

#delete
btn_delete=Button(btn_frame,text="Delete",command=delete,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_delete.grid(row=0,column=2,padx=1)

#reset
btn_res=Button(btn_frame,text="Reset",command=reset,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_res.grid(row=0,column=3,padx=1)

#################### Table Frame ####################
table_frame=LabelFrame(cw,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
table_frame.place(x=400,y=50,width=679,height=465)

lblsearch=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
lblsearch.grid(row=0,column=0,sticky=W,padx=2)

search_var=StringVar()
combo_search=ttk.Combobox(table_frame,textvariable=search_var,font=("arial",12,"bold"),state="readonly",width=15)
combo_search["value"]=("Mobile No","Ref")
combo_search.current(0)
combo_search.grid(row=0,column=1,sticky=W,padx=2)

txt_search=StringVar()
txtsearch=ttk.Entry(table_frame,textvariable=txt_search,font=("arial",12,"bold"),width=22)
txtsearch.grid(row=0,column=2,padx=2)

btn_search=Button(table_frame,text="Search",command=search,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
btn_search.grid(row=0,column=3,padx=2)

btn_show=Button(table_frame,text="Show All",command=fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
btn_show.grid(row=0,column=4,padx=2)



####################### Detail data ###########################
detail_table=Frame(table_frame,bd=2,relief=RIDGE)
detail_table.place(x=0,y=50,width=673,height=392)

scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

Cust_Details_Table=ttk.Treeview(detail_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=Cust_Details_Table.xview)
scroll_y.config(command=Cust_Details_Table.yview)


Cust_Details_Table.heading("ref",text="Refer no")
Cust_Details_Table.heading("name",text="Name")
Cust_Details_Table.heading("mother",text="Mother Name")
Cust_Details_Table.heading("gender",text="Gender")
Cust_Details_Table.heading("post",text="Postcode")
Cust_Details_Table.heading("mobile",text="Mobile")
Cust_Details_Table.heading("email",text="Email")
Cust_Details_Table.heading("nationality",text="Nationality")
Cust_Details_Table.heading("idproof",text="Id proof")
Cust_Details_Table.heading("idnumber",text="Id Number")
Cust_Details_Table.heading("address",text="Address")

Cust_Details_Table["show"]="headings"

Cust_Details_Table.column("ref",width=100)
Cust_Details_Table.column("name",width=100)
Cust_Details_Table.column("mother",width=100)
Cust_Details_Table.column("gender",width=100)
Cust_Details_Table.column("post",width=100)
Cust_Details_Table.column("mobile",width=100)
Cust_Details_Table.column("email",width=100)
Cust_Details_Table.column("nationality",width=100)
Cust_Details_Table.column("idproof",width=100)
Cust_Details_Table.column("idnumber",width=100)
Cust_Details_Table.column("address",width=100)
Cust_Details_Table.pack(fill=BOTH,expand=1) # heh na columns chya arrangement mule vaparlay
Cust_Details_Table.bind("<ButtonRelease-1>",get_cursor)	#ha  get_cursor chya funcion la data la customer details madhe anayla madat karto
fetch_data()




cw.withdraw()

############################### Room ######################

rw=Toplevel(root)
rw.title("Hotel Management System")
rw.geometry("1082x550+188+200")
#cw.resizable(False,False)
########################## Logo RW
"""imgrw=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\logohotel.png")
imgrw=imgrw.resize((230,40),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimgrw=ImageTk.PhotoImage(imgrw)

lblrw=Label(rw,image=photoimgrw,bd=0,relief=RIDGE)
lblrw.place(x=5,y=2,width=230,height=40)"""



################# Title ###############
lbl_title=Label(rw,text="ROOM BOOKING DETAILS",font=("times ne roman",18,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
lbl_title.place(x=0,y=0,width=1082,height=50)

labelframeleft=LabelFrame(rw,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),padx=2)
labelframeleft.place(x=0,y=50,width=400,height=465)

################ Room labels and entrys #####################
#cust contact
lbl_cust_ref=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
lbl_cust_ref.grid(row=0,column=0,sticky=W)

enty_cust=ttk.Entry(labelframeleft,textvariable=var_contact,font=("arial",12,"bold"),width=18)
enty_cust.grid(row=0,column=1,sticky=W)	#sticky w manje stick on west side

#Fetch Data
btn_fetch=Button(labelframeleft,text="Fetch Data",command=fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=9)
btn_fetch.place(x=320,y=4)

#check in date
check_in_date=Label(labelframeleft,text="Check_in Date",font=("arial",12,"bold"),padx=2,pady=6)
check_in_date.grid(row=1,column=0,sticky=W)

txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=var_checkin,font=("arial",12,"bold"),width=25)
txtcheck_in_date.grid(row=1,column=1)

#check_out_date
lbl_Check_out=Label(labelframeleft,text="Check_Out Date",font=("arial",12,"bold"),padx=2,pady=6)
lbl_Check_out.grid(row=2,column=0,sticky=W)

txt_check_out=ttk.Entry(labelframeleft,textvariable=var_checkout,font=("arial",12,"bold"),width=25)
txt_check_out.grid(row=2,column=1)

#Room Type
roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
roomtype.grid(row=3,column=0,sticky=W)

conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
my_cursor.execute("select RoomType from details")
ide=my_cursor.fetchall()

combo_roomtype=ttk.Combobox(labelframeleft,textvariable=var_roomtype,font=("arial",12,"bold"),state="readonly")
combo_roomtype["value"]=ide
combo_roomtype.current(0)
combo_roomtype.grid(row=3,column=1,sticky=W)


"""txtgname=ttk.Entry(labelframeleft,font=("arial",12,"bold"),width=25)
txtgname.grid(row=3,column=1)"""


#Available room
availableroom=Label(labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
availableroom.grid(row=4,column=0,sticky=W)

#txtavailable=ttk.Entry(labelframeleft,textvariable=var_roomavailable,font=("arial",12,"bold"),width=25)
#txtavailable.grid(row=4,column=1)

conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
my_cursor.execute("select RoomNo from details")
rows=my_cursor.fetchall()

combo_roomav=ttk.Combobox(labelframeleft,textvariable=var_roomavailable,font=("arial",12,"bold"),state="readonly")
combo_roomav["value"]=rows
combo_roomav.current(0)
combo_roomav.grid(row=4,column=1,sticky=W)


#meal
lblmeal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
lblmeal.grid(row=5,column=0,sticky=W)

txtmeal=ttk.Entry(labelframeleft,textvariable=var_meal,font=("arial",12,"bold"),width=25)
txtmeal.grid(row=5,column=1)

#no of days
lblnoofdays=Label(labelframeleft,text="No of Days",font=("arial",12,"bold"),padx=2,pady=6)
lblnoofdays.grid(row=6,column=0,sticky=W)

txtnoofdays=ttk.Entry(labelframeleft,textvariable=var_noofdays,font=("arial",12,"bold"),width=25)
txtnoofdays.grid(row=6,column=1)

#paid tax

lblpaid=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
lblpaid.grid(row=7,column=0,sticky=W)

"""combo_paid=ttk.Combobox(labelframeleft,textvariable=var_paidtax,font=("arial",12,"bold"),state="readonly")
combo_paid["value"]=("India","England","Austraila","USA","New Zealand","Pakistan","South Africa","Germany","Dubai","Singapore","France","Others")
combo_paid.current(0)
combo_nat.grid(row=7,column=1,sticky=W)"""

txtpaid=ttk.Entry(labelframeleft,textvariable=var_paidtax,font=("arial",12,"bold"),width=25)
txtpaid.grid(row=7,column=1)

#Sub Total

lblsub=Label(labelframeleft,text="Sub Total ",font=("arial",12,"bold"),padx=2,pady=6)
lblsub.grid(row=8,column=0,sticky=W)

txtsub=ttk.Entry(labelframeleft,textvariable=var_actualtotal,font=("arial",12,"bold"),width=25)
txtsub.grid(row=8,column=1)

"""combo_idproof=ttk.Combobox(labelframeleft,textvariable=var_idproof,font=("arial",12,"bold"),state="readonly")
combo_idproof["value"]=("Aadhar card","Pan Card","Driving License","Ration Card","Others")
combo_idproof.current(0)
combo_idproof.grid(row=8,column=1,sticky=W)"""



#Total Cost
lbltotal=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
lbltotal.grid(row=9,column=0,sticky=W)

txttotal=ttk.Entry(labelframeleft,textvariable=var_total,font=("arial",12,"bold"),width=25)
txttotal.grid(row=9,column=1)

#address

"""lbladd=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
lbladd.grid(row=10,column=0,sticky=W)

txtid=ttk.Entry(labelframeleft,textvariable=var_address,font=("arial",12,"bold"),width=25)
txtid.grid(row=10,column=1)"""
#################### Bill
btn_bill=Button(labelframeleft,text="Bill",command=total,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_bill.grid(row=11,column=0,padx=1,sticky=W)


########################## dowm Button Frames for rooms ################################
btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
btn_frame.place(x=0,y=395,width=375,height=35)

#add
btn_add=Button(btn_frame,text="Add",command=add_datarw,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_add.grid(row=0,column=0,padx=1)

#update
btn_update=Button(btn_frame,text="Update",command=update1,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_update.grid(row=0,column=1,padx=1)

#delete
btn_delete=Button(btn_frame,text="Delete",command=deleter,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_delete.grid(row=0,column=2,padx=1)

#reset
btn_res=Button(btn_frame,text="Reset",command=resetr,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
btn_res.grid(row=0,column=3,padx=1)

#################### Right side image RW ###############

img10=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\bed.jpg")
img10=img10.resize((400,300),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg10=ImageTk.PhotoImage(img10)

lblimg=Label(rw,image=photoimg10,bd=4,relief=RIDGE)
lblimg.place(x=680,y=55,width=400,height=300)


#################### Table Frame for room ####################
table_frame=LabelFrame(rw,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
table_frame.place(x=400,y=275,width=679,height=240)

lblsearch=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
lblsearch.grid(row=0,column=0,sticky=W,padx=2)


detail_table=Frame(table_frame,bd=2,relief=RIDGE)
detail_table.place(x=0,y=50,width=673,height=175)

scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

room_Details_Table=ttk.Treeview(detail_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=room_Details_Table.xview)
scroll_y.config(command=room_Details_Table.yview)


def searchrw():
	conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
	my_cursor=conn.cursor()	

	my_cursor.execute("select * from room where "+str(search_varrw.get())+" LIKE '%"+str(txt_searchrw.get())+"%'")
	rows=my_cursor.fetchall()	#hya rows valya variable madhe data sagla fetch honaar
	if len(rows)!=0:
		room_Details_Table.delete(*room_Details_Table.get_children())	#get children manje colums che childrens
		for i in rows:
			room_Details_Table.insert("",END,values=i)
		conn.commit()
	conn.close()

def fetch_datarw():
	conn=mysql.connector.connect(host="localhost",username="root",password="Oneness13",database="hotel")
	my_cursor=conn.cursor()			#heh cursor mysql chya query execute karnya sathi use kelya aahet
	my_cursor.execute("select * from room")
	rows=my_cursor.fetchall()	#hya rows valya variable madhe data sagla fetch honaar
	if len(rows)!=0:
		room_Details_Table.delete(*room_Details_Table.get_children())	#get children manje colums che childrens
		for i in rows:
			room_Details_Table.insert("",END,values=i)
		conn.commit()
	conn.close()


####################### Detail data  for rw ###########################





def get_cursorrw(event=""):
	cursor_row=room_Details_Table.focus()
	content=room_Details_Table.item(cursor_row)	#joh pan scrollbar valya frame madhe data present aaahe to tithe visible hoyayla paije manjech customer details madhe
	row=content["values"]


	var_contact.set(row[0]),
	var_checkin.set(row[1]),
	var_checkout.set(row[2]),
	var_roomtype.set(row[3]),
	var_roomavailable.set(row[4]),
	var_meal.set(row[5]),
	var_noofdays.set(row[6])



room_Details_Table.heading("contact",text="Contact no")
room_Details_Table.heading("checkin",text="Check in")
room_Details_Table.heading("checkout",text="Check out")
room_Details_Table.heading("roomtype",text="Room Type")
room_Details_Table.heading("roomavailable",text="Room Available")
room_Details_Table.heading("meal",text="Meal")
room_Details_Table.heading("noofdays",text="No of Days")


room_Details_Table["show"]="headings"

room_Details_Table.column("contact",width=100)
room_Details_Table.column("checkin",width=100)
room_Details_Table.column("checkout",width=100)
room_Details_Table.column("roomtype",width=100)
room_Details_Table.column("roomavailable",width=100)
room_Details_Table.column("meal",width=100)
room_Details_Table.column("noofdays",width=100)

room_Details_Table.pack(fill=BOTH,expand=1) # heh na columns chya arrangement mule vaparlay
room_Details_Table.bind("<ButtonRelease-1>",get_cursorrw)	#ha  get_cursor chya funcion la data la customer details madhe anayla madat karto
fetch_datarw()








search_varrw=StringVar()
combo_searchr=ttk.Combobox(table_frame,textvariable=search_varrw,font=("arial",12,"bold"),state="readonly",width=15)
combo_searchr["value"]=("Contact No","Room")
combo_searchr.current(0)
combo_searchr.grid(row=0,column=1,sticky=W,padx=2)

txt_searchrw=StringVar()
txt_searchrw=ttk.Entry(table_frame,textvariable=txt_searchrw,font=("arial",12,"bold"),width=22)
txt_searchrw.grid(row=0,column=2,padx=2)

btn_searchrw=Button(table_frame,text="Search",command=searchrw,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
btn_searchrw.grid(row=0,column=3,padx=2)

btn_showrw=Button(table_frame,text="Show All",command=fetch_datarw,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
btn_showrw.grid(row=0,column=4,padx=2)





"""table_frame=LabelFrame(rw,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
table_frame.place(x=400,y=50,width=679,height=465)"""





rw.withdraw()



root.mainloop()

"""img13=Image.open(r"C:\Python Program's Practice\Hotel Management System\images\hotel images\taj.jpg")
img13=img13.resize((1450,800),Image.ANTIALIAS) #ANTIALIAS high quality image la low quality madhe convert karto
photoimg13=ImageTk.PhotoImage(img13)

lblimg=Label(rew_frame,image=photoimg13,bd=4,relief=RIDGE)
lblimg.place(x=0,y=0,width=1450,height=800)"""











#rew.withdraw()

root.mainloop()