from tkinter import *
import tkinter.messagebox
import sqlite3
from tkinter import ttk
from tkinter import ttk#the treeview widget is ttk widget
import sys
from PIL import ImageTk, Image
from tkinter.messagebox import askokcancel # get canned std dialog
from tkinter.colorchooser import askcolor
from tkinter.messagebox import *
root=Tk()
root.title("CRM WITH TREEVIEW AND SQLITE")
root.config(bg="#BC95B4")
root.geometry("1000x500")
root.iconbitmap('C:\Qoryare/crm_icon.ico')#system icon

################


tabs = ttk.Notebook(root) 
root1= ttk.Frame(tabs)
root2=ttk.Frame(tabs)


tabs.add(root1, text ='Allifmaal CRM') 
tabs.add(root2, text ='Stock') 
tabs.pack(expand = 1, fill ="both") 

#mylabel=Label(root1,text="Allifmaal CRM")
#mylabel.pack()
#mylabel=Label(root1,text="CRM")
#mylabel.pack()
#mylabel=Label(root2,text="Stock")
#mylabel.pack()
#add some style to the treeview
######################################################################################
################ chnage varisbl
#create and connect to the database and also create the table.
connec=sqlite3.connect("crm_treeview_customer.db")
my_cursor=connec.cursor()

#create the table
my_cursor.execute("""CREATE TABLE IF NOT EXISTS crm_treeview_customer_table_2 (
                    first_name text, 
                  last_name text,
                  id integer,
                  phy_address text,
                  city text,
                  state_1 text,
                  zipcode text
                  
                  )""")




    

################################## END OF FUNCTION TO CLEAR TABLE######################
    


#add dummy data to the database




    

def query_database_with_primary_key():
    connec=sqlite3.connect("crm_treeview_customer.db")
    my_cursor=connec.cursor()
    my_cursor.execute("SELECT rowid, * FROM crm_treeview_customer_table_2")
    fetched_data=my_cursor.fetchall()
    #print(fetched_data)
    
    #get records from database and display on the tree view
    count=0
    for record in fetched_data:
        if count % 2==0:#if this row is even ...if you divide by two, the remainder is zero
            treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[1],record[2],\
            record[0],record[4],record[5],record[6],record[7]),tags=('evenrow',))
        
        else:
        
            treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[1],record[2],\
            record[0],record[4],record[5],record[6],record[7]),tags=('oddrow',))
        
        count+=1#if you take the count outside the if level, it wouldnot work
    
    
    connec.commit()
    connec.close()
    
    

###########################################################################
treeview_style=ttk.Style()
#pick a theme
treeview_style.theme_use('default')
#configure the treeview colors
treeview_style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
#do a style map which allows records to change color when clicked...ie change the selected color
treeview_style.map('Treeview',background=[('selected',"#347083")])
#create frame for the treeview
treeview_frame=Frame(root,bg="green")
treeview_frame.pack(pady=10)
#create scrollbars for the treeview
scrollbar_treeview_y=Scrollbar(treeview_frame,orient=VERTICAL)
scrollbar_treeview_y.pack(side=RIGHT,fill=Y)

scrollbar_treeview_x=Scrollbar(treeview_frame,orient=HORIZONTAL)
scrollbar_treeview_x.pack(side=BOTTOM,fill=X)

title_frame=Frame(treeview_frame,bg="lightblue",bd=10,padx=40,pady=8,relief=RIDGE)#smaller frame inside main frame
title_frame.pack(side=TOP,fill=X)
title_label=Label(title_frame,text="Customer Database Managmenet System",bg="lightblue",font=('arial',50,'normal'))
title_label.grid()

#create the treeview
treeview_crm=ttk.Treeview(treeview_frame,xscrollcommand=scrollbar_treeview_x.set,yscrollcommand=scrollbar_treeview_y.set,selectmode="extended")
treeview_crm.pack()
#configure the scrollbar
scrollbar_treeview_y.config(command=treeview_crm.yview)
scrollbar_treeview_x.config(command=treeview_crm.xview)

#define the columns
treeview_crm['columns']=("First Name","Last Name","ID","phy_address","City","state_1","Zipcode")
#format the columns
treeview_crm.column("#0",width=0,stretch=NO)# The fantom auto column
treeview_crm.column("First Name",anchor=W,width=200)
treeview_crm.column("Last Name",anchor=W,width=200)
treeview_crm.column("ID",anchor=CENTER,width=100)
treeview_crm.column("phy_address",anchor=CENTER,width=200)
treeview_crm.column("City",anchor=CENTER,width=200)
treeview_crm.column("state_1",anchor=CENTER,width=200)
treeview_crm.column("Zipcode",anchor=CENTER,width=200)

#create the headings
treeview_crm.heading("#0",text="",anchor=W)
treeview_crm.heading("First Name",text="First Name",anchor=W)
treeview_crm.heading("Last Name",text="Last Name",anchor=W)
treeview_crm.heading("ID",text="ID",anchor=CENTER)
treeview_crm.heading("phy_address",text="phy_address",anchor=CENTER)
treeview_crm.heading("City",text="City",anchor=CENTER)
treeview_crm.heading("state_1",text="state_1",anchor=CENTER)
treeview_crm.heading("Zipcode",text="Zipcode",anchor=CENTER)



#create the striped rows
treeview_crm.tag_configure('oddrow',background="white")
treeview_crm.tag_configure('evenrow',background="lightblue")
#


#insert data to the screen of the treeview
global count


    
    # add record entry boxes and labels
data_frame=LabelFrame(root,text="Record",bg="lightblue")
data_frame.pack(fill="x",expand="yes",padx=20)
    
first_name_label=Label(data_frame,text="First Name")
first_name_label.grid(row=0,column=0,padx=10,pady=10)
first_name_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
first_name_text_field.grid(row=0,column=1,padx=10,pady=10)
    
last_name_label=Label(data_frame,text="Last Name")
last_name_label.grid(row=0,column=2,padx=10,pady=10)
last_name_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
last_name_text_field.grid(row=0,column=3,padx=10,pady=10)
    
id_label=Label(data_frame,text="ID")
id_label.grid(row=0,column=4,padx=10,pady=10)
id_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
id_text_field.grid(row=0,column=5,padx=10,pady=10)
    
phy_address_label=Label(data_frame,text="phy_address")
phy_address_label.grid(row=1,column=0,padx=10,pady=10)
phy_address_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
phy_address_text_field.grid(row=1,column=1,padx=10,pady=10)
    
city_label=Label(data_frame,text="City")
city_label.grid(row=1,column=2,padx=10,pady=10)
city_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
city_text_field.grid(row=1,column=3,padx=10,pady=10)
    
state_1_label=Label(data_frame,text="state_1")
state_1_label.grid(row=1,column=4,padx=10,pady=10)
state_1_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
state_1_text_field.grid(row=1,column=5,padx=10,pady=10)
    
zipcode_label=Label(data_frame,text="Zipcode")
zipcode_label.grid(row=1,column=6,padx=10,pady=10)
zipcode_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
zipcode_text_field.grid(row=1,column=7,padx=10,pady=10)
#################### DELETE TEXT FIELD#################
delete_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
delete_text_field.grid(row=1,column=8,padx=10,pady=10)

#do the functions
def clear_text_fields_func():
    first_name_text_field.delete(0,END)
    last_name_text_field.delete(0,END)
    id_text_field.delete(0,END)
    phy_address_text_field.delete(0,END)
    city_text_field.delete(0,END)
    state_1_text_field.delete(0,END)
    zipcode_text_field.delete(0,END)
    
    
    
#do the select record so that when you click its button, the values are auto-inserted into the text fields
def select_record_func():
    
    #clear entry boxes first
    clear_text_fields_func()
    
    #grab the selected record number
    selected_record=treeview_crm.focus()# this focus means whatever we clicked is required
    #grab the record values
    record_values=treeview_crm.item(selected_record,'values')#these values are the ones under the for loop 
    #insert the values of the selected record into the entry boxes
    first_name_text_field.insert(0,record_values[0])
    last_name_text_field.insert(0,record_values[1])
    id_text_field.insert(0,record_values[2])
    phy_address_text_field.insert(0,record_values[3])
    city_text_field.insert(0,record_values[4])
    state_1_text_field.insert(0,record_values[5])
    zipcode_text_field.insert(0,record_values[6])  
    
    #
#move a row up function
def move_row_up_func():
    rows=treeview_crm.selection()
    for row in rows:
        treeview_crm.move(row,treeview_crm.parent(row),treeview_crm.index(row)-1)
def move_row_down_func():
    rows=treeview_crm.selection()
    for row in reversed(rows):
        treeview_crm.move(row,treeview_crm.parent(row),treeview_crm.index(row)+1)

#remove one selected record---this removes only from the screen since no db connected yet
def delete_one_selected_record_func():
    delete_one_selected_variable=treeview_crm.selection()[0]
    treeview_crm.delete(delete_one_selected_variable)

#delete many records selected
def delete_many_selected_records_func():
    delete_many_selected_variable=treeview_crm.selection()#since you are deleting many, no need to specify zero
    for records in delete_many_selected_variable:
        treeview_crm.delete(records)
#remove all records
def delete_all_records_func():
    for records in treeview_crm.get_children():
        treeview_crm.delete(records)
        
#update record
def update_record_out_database_func():#UPDATES ONLY IN TREEVIEW SCREEN
    
     #grab the record number of whatever is selected
    ''' selected_variable=treeview_crm.focus()
    treeview_crm.item(selected_variable,text="",values=(first_name_text_field.get(),\
        last_name_text_field.get(),id_text_field.get(),phy_address_text_field.get(),\
            city_text_field.get(),state_1_text_field.get(),zipcode_text_field.get(),)) '''
    
    global count
    count=0
    treeview_crm.insert(parent='',index='end',text="",values=(first_name_text_field.get(),\
        last_name_text_field.get(),id_text_field.get(),phy_address_text_field.get(),\
        city_text_field.get(),state_1_text_field.get(),zipcode_text_field.get()))
    count+=1

    
    #clear the boxes
    
    clear_text_fields_func() 
    
################################## START OF UPDATE RECORDS FUNCTION IN THE DATABASE
def update_record_in_database_func():#UPDATES BOTH IN DB AND TREEVIEW SCREEN
    
    #grab the record number of whatever is selected
    
    selected_variable=treeview_crm.focus()
    treeview_crm.item(selected_variable,text="",values=(first_name_text_field.get(),\
        last_name_text_field.get(),id_text_field.get(),phy_address_text_field.get(),\
            city_text_field.get(),state_1_text_field.get(),zipcode_text_field.get(),))
    
    #UPDATE DATABASE
    connec=sqlite3.connect("crm_treeview_customer.db")
    my_cursor=connec.cursor()
    
    my_cursor.execute(""" UPDATE crm_treeview_customer_table_2 SET
                      
                        first_name = :first_name,
                        last_name = :last_name,
                        phy_address = :phy_address,
                        city = :city,
                        state_1 = :state_1,
                        zipcode = :zipcode
                    
                        WHERE oid = :id""",
                            {
                            'first_name':first_name_text_field.get(),
                            'last_name':last_name_text_field.get(),
                            'phy_address':phy_address_text_field.get(),
                            'city':city_text_field.get(),
                            'state_1':state_1_text_field.get(),
                            'zipcode':zipcode_text_field.get(),
                            'id':id_text_field.get(),
                            }
                      )
    
    connec.commit()
    connec.close()
    
    clear_text_fields_func()


################################## END OF UPDATE RECORDS FUNCTION IN THE DATABASE

######################### Adding data to the database##############3MINE

def add_data_to_database_from_front_end():

        
    connec=sqlite3.connect('crm_treeview_customer.db')
    #create the cursor instance
    cursor_var=connec.cursor()
    
    #insert what is typed into table and use placeholder variables (those under values barakets).that is
    #dumy variables and each starts with colon
    #then create python dictionary that has key value pairs and the keys are those dumies under values and values are whatever in the text boxes
    cursor_var.execute("INSERT INTO crm_treeview_customer_table_2 VALUES(:first_name, :last_name,:id, :phy_address, :city, :state_1, :zipcode)",
                       {
                       'first_name': first_name_text_field.get(),
                       'last_name': last_name_text_field.get(),
                       'id':id_text_field.get(),
                       'phy_address': phy_address_text_field.get(),
                       'city': city_text_field.get(),
                       'state_1': state_1_text_field.get(),
                       'zipcode': zipcode_text_field.get()   
                       })
    
    #commit changes to the db
    connec.commit()
    #close connection
    connec.close()

    
    clear_text_fields_func()
    #then, clear the text boxes when the submit button is clicked
    #clear the treeview table and
    treeview_crm.delete(*treeview_crm.get_children())#clears the treeview so that all the records and be inserted again
    
    query_database_with_primary_key()#inserts all values into treeview again


################################### END MINE#########################

############# START OF DELETE FUNCTION######################
def delete_selected_from_db_func():################# DELETE JUST BY SELECTION###########NOT WORKING
    #selected_variable=treeview_crm.selection()[0]#DELETES ONE
    
    #WHERE id=?", (id,))

    connec=sqlite3.connect('crm_treeview_customer.db')
    my_cursor=connec.cursor()
    selected_variable=treeview_crm.selection()[0]
    #messageDelete= tkinter.messagebox.askyesno ("","Do you want to permanently delete this record?")
    #if messageDelete > 0:
        #treeview_crm.delete(selected_variable)
    my_cursor.execute("DELETE FROM crm_treeview_customer_table WHERE oid="+selected_variable)
    #else:
       # pass
    
    connec.commit()
    connec.close()

####################### END OF DELETE FUNCTION

############################ START OF  DELETE BY ID SELECTION##############
def delete_record_by_id_text_field_func():
    connec=sqlite3.connect('crm_treeview_customer.db')
    my_cursor=connec.cursor()
    
    #clear entry boxes first
    clear_text_fields_func()
    
    #grab the selected record number
    selected_record=treeview_crm.focus()# this focus means whatever we clicked is required
    #grab the record values
    record_values=treeview_crm.item(selected_record,'values')#these values are the ones under the for loop 
    #insert the values of the selected record into the entry boxes
    #delete_all_records_func()
    
    delete_text_field.insert(0,record_values[2])
    my_cursor.execute("DELETE from crm_treeview_customer_table_2 WHERE oid=" + delete_text_field.get())
    delete_text_field.delete(0, END)#clear the text field after deleteion
    #treeview_crm.delete(*treeview_crm.get_children())#clear the treeview after deletion
    #delete_all_records_func()
    delete_one_selected_variable=treeview_crm.selection()[0]
    treeview_crm.delete(delete_one_selected_variable)
    
    #query_database_with_primary_key()#inserts all values into treeview again
    connec.commit()
    connec.close()
    

def update_record_by_id_text_field_func():
    connec=sqlite3.connect('crm_treeview_customer.db')
    my_cursor=connec.cursor()
    
    #clear entry boxes first
    clear_text_fields_func()
    
    #grab the selected record number
    selected_record=treeview_crm.focus()# this focus means whatever we clicked is required
    #grab the record values
    record_values=treeview_crm.item(selected_record,'values')#these values are the ones under the for loop 
    #insert the values of the selected record into the entry boxes
    #delete_all_records_func()
    
    delete_text_field.insert(0,record_values[2])
    my_cursor.execute("DELETE from crm_treeview_customer_table_2 WHERE oid=" + delete_text_field.get())
    
    delete_text_field.delete(0, END)#clear the text field after deleteion
    #treeview_crm.delete(*treeview_crm.get_children())#clear the treeview after deletion
    #delete_all_records_func()
    delete_one_selected_variable=treeview_crm.selection()[0]
    treeview_crm.delete(delete_one_selected_variable)
    
    #query_database_with_primary_key()#inserts all values into treeview again
    connec.commit()
    connec.close()


buttons_frame=LabelFrame(root,text="Buttons",bg="lightblue")
buttons_frame.pack(fill="x",expand="yes",padx=20)

update_out_database_button=Button(buttons_frame,text="Update Treeview Record",command=update_record_out_database_func)
update_out_database_button.grid(row=0,column=0,padx=10,pady=10)
update_in_database_button=Button(buttons_frame,text="Update in DB Record",command=update_record_in_database_func)
update_in_database_button.grid(row=1,column=0,padx=10,pady=10)

add_button=Button(buttons_frame,bg="green",text="Add Record to DB",command=add_data_to_database_from_front_end)
add_button.grid(row=0,column=1,padx=10,pady=10)
remove_all_button=Button(buttons_frame,bg="green",text="Remove All Records from TV",command=delete_all_records_func)
remove_all_button.grid(row=0,column=2,padx=10,pady=10)
remove_one_button=Button(buttons_frame,bg="green",text="Remove one selected Record from TV",command=delete_one_selected_record_func)
remove_one_button.grid(row=0,column=3,padx=10,pady=10)
remove_many_button=Button(buttons_frame,bg="green",text="Remove Many Selected Records from TV",command=delete_many_selected_records_func)
remove_many_button.grid(row=0,column=4,padx=10,pady=10)
move_up_button=Button(buttons_frame,bg="green",text="Move Up",command=move_row_up_func)
move_up_button.grid(row=0,column=5,padx=10,pady=10)
move_down_button=Button(buttons_frame,bg="green",text="Move Down",command=move_row_down_func)
move_down_button.grid(row=0,column=6,padx=10,pady=10)
select_record_button=Button(buttons_frame,bg="green",text="Select Record",command=select_record_func)
select_record_button.grid(row=1,column=1,padx=10,pady=10)
clear_text_field_button=Button(buttons_frame,bg="green",text="Clear Text Fields",command=clear_text_fields_func)
clear_text_field_button.grid(row=1,column=4,padx=10,pady=10)

show_all_records_button=Button(buttons_frame,bg="green",text="Show All DB records",command=query_database_with_primary_key)
show_all_records_button.grid(row=1,column=2,padx=10,pady=10)

delete_selected_from_db_button=Button(buttons_frame,text="Delete selected from DB",command=delete_selected_from_db_func)
delete_selected_from_db_button.grid(row=1,column=5,padx=10,pady=10)


delete_record_by_id_text_field_from_db_button=Button(buttons_frame,bg="green",text="Delete by id text field from DB",command=delete_record_by_id_text_field_func)
delete_record_by_id_text_field_from_db_button.grid(row=1,column=6,padx=10,pady=10)
################################################################################################################


#
query_database_with_primary_key()


connec.commit()

            

root.mainloop()
###################
#######################################

########################################################
#######################3 only update not working.###########################