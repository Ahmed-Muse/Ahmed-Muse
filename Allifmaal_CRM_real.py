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
main_root=Tk()
main_root.title("CRM WITH TREEVIEW AND SQLITE")
main_root.config(bg="#BC95B4")
main_root.geometry("1000x500")
main_root.iconbitmap('C:\Qoryare/crm_icon.ico')#system icon
tabs = ttk.Notebook(main_root) 
root= ttk.Frame(tabs)
root2=ttk.Frame(tabs)
root3=ttk.Frame(tabs)
root4=ttk.Frame(tabs)
root5=ttk.Frame(tabs)

tabs.add(root, text ='ALLIFMAAL CRM') 
tabs.add(root2, text ='Stock')
tabs.add(root3, text ='customers') 
tabs.add(root4, text ='staff') 
tabs.add(root5, text ='orders') 
tabs.pack(expand = 1, fill ="both")

#create and connect to the database and also create the table.
connec=sqlite3.connect("Allifmaal_CRM.db")
my_cursor=connec.cursor()

#create the table
my_cursor.execute("""CREATE TABLE IF NOT EXISTS Allifmaal_CRM (
                    id integer,
                    org_name text, 
                    project text,
                    project_status text,
                    contacts text,
                    contact_person text,
                    physical_address text
                  
                  )""")

############ start of query function
def query_database_with_primary_key():
    connec=sqlite3.connect("Allifmaal_CRM.db")
    my_cursor=connec.cursor()
    my_cursor.execute("SELECT rowid, * FROM Allifmaal_CRM")
    fetched_data=my_cursor.fetchall()
    print(fetched_data)
    
    #get records from database and display on the tree view
    count=0
    for record in fetched_data:
        if count % 2==0:#if this row is even ...if you divide by two, the remainder is zero
            treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[0],record[2],\
            record[3],record[4],record[5],record[6],record[7]),tags=('evenrow',))
        
        else:
        
            treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[0],record[2],\
            record[3],record[4],record[5],record[6],record[7]),tags=('oddrow',))
        
        count+=1#if you take the count outside the if level, it wouldnot work
    
    
    connec.commit()
    connec.close()

################### end of query function

###########################################################################
treeview_style=ttk.Style()
#pick a theme
treeview_style.theme_use('default')
#configure the treeview colors
treeview_style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
#do a style map which allows records to change color when clicked...ie change the selected color
treeview_style.configure("Treeview.Heading", font=('helvetica',12,'bold'))
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
treeview_crm['columns']=("id","org_name","project","project_status","contacts","contact_person","physical_address")
#format the columns
treeview_crm.column("#0",width=0,stretch=NO)# The fantom auto column
treeview_crm.column("id",anchor=W,width=40)
treeview_crm.column("org_name",anchor=W,width=300)
treeview_crm.column("project",anchor=CENTER,width=100)
treeview_crm.column("project_status",anchor=CENTER,width=200)
treeview_crm.column("contacts",anchor=CENTER,width=200)
treeview_crm.column("contact_person",anchor=CENTER,width=200)
treeview_crm.column("physical_address",anchor=CENTER,width=200)

#create the headings
treeview_crm.heading("#0",text="",anchor=W)
treeview_crm.heading("id",text="S/N",anchor=W)
treeview_crm.heading("org_name",text="NAME",anchor=W)
treeview_crm.heading("project",text="PROJECT",anchor=CENTER)
treeview_crm.heading("project_status",text="STATUS",anchor=CENTER)
treeview_crm.heading("contacts",text="CONTACTS",anchor=CENTER)
treeview_crm.heading("contact_person",text="PERSON",anchor=CENTER)
treeview_crm.heading("physical_address",text="ADDRESS",anchor=CENTER)
#create the striped rows
treeview_crm.tag_configure('oddrow',background="white")
treeview_crm.tag_configure('evenrow',background="lightblue")
#insert data to the screen of the treeview
global count
    # add record entry boxes and labels
data_frame=LabelFrame(root,text="Record",bg="lightblue",font=('helvetica',12,'bold'))
data_frame.pack(fill="x",expand="yes",padx=20)
    
id_label=Label(data_frame,text="ID",font=('helvetica',12,'bold'))
id_label.grid(row=0,column=6,padx=10,pady=10)
id_text_field=Entry(data_frame,width=2,borderwidth=5,font=('helvetica',12,'bold'))
id_text_field.grid(row=0,column=7,padx=10,pady=10)
    
org_name_label=Label(data_frame,text="Name",font=('helvetica',12,'bold'))
org_name_label.grid(row=0,column=0,padx=10,pady=10)
org_name_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
org_name_text_field.grid(row=0,column=1,padx=10,pady=10)
    
project_label=Label(data_frame,text="Project",font=('helvetica',12,'bold'))
project_label.grid(row=0,column=2,padx=10,pady=10)
project_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
project_text_field.grid(row=0,column=3,padx=10,pady=10)
    
project_status_label=Label(data_frame,text="Status",font=('helvetica',12,'bold'))
project_status_label.grid(row=0,column=4,padx=10,pady=10)
project_status_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
project_status_text_field.grid(row=0,column=5,padx=10,pady=10)
    
contacts_label=Label(data_frame,text="Contacts",font=('helvetica',12,'bold'))
contacts_label.grid(row=1,column=0,padx=10,pady=10)
contacts_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
contacts_text_field.grid(row=1,column=1,padx=10,pady=10)
    
contact_person_label=Label(data_frame,text="Person",font=('helvetica',12,'bold'))
contact_person_label.grid(row=1,column=2,padx=10,pady=10)
contact_person_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
contact_person_text_field.grid(row=1,column=3,padx=10,pady=10)
    
physical_address_label=Label(data_frame,text="Address",font=('helvetica',12,'bold'))
physical_address_label.grid(row=1,column=4,padx=10,pady=10)
physical_address_text_field=Entry(data_frame,width=20,borderwidth=5,font=('helvetica',12,'bold'))
physical_address_text_field.grid(row=1,column=5,padx=10,pady=10)
#################### DELETE TEXT FIELD#################

delete_id_label=Label(data_frame,text="delete id",font=('helvetica',12,'bold'))
#delete_id_label.grid(row=1,column=6,padx=10,pady=10)
delete_id_text_field=Entry(data_frame,width=2,borderwidth=5,font=('helvetica',12,'bold'))
#delete_id_text_field.grid(row=1,column=7,padx=10,pady=10)

######### buttons

#do the functions
def clear_text_fields_func():
    id_text_field.delete(0,END)
    org_name_text_field.delete(0,END)
    project_text_field.delete(0,END)
    project_status_text_field.delete(0,END)
    contacts_text_field.delete(0,END)
    contact_person_text_field.delete(0,END)
    physical_address_text_field.delete(0,END)
    delete_id_text_field.delete(0,END)
    
def select_record_func():
    
    #clear entry boxes first
    clear_text_fields_func()
    
    #grab the selected record number
    selected_record=treeview_crm.focus()# this focus means whatever we clicked is required
    #grab the record values
    record_values=treeview_crm.item(selected_record,'values')#these values are the ones under the for loop 
    #insert the values of the selected record into the entry boxes
    id_text_field.insert(0,record_values[0])
    org_name_text_field.insert(0,record_values[1])
    project_text_field.insert(0,record_values[2])
    project_status_text_field.insert(0,record_values[3])
    contacts_text_field.insert(0,record_values[4])
    contact_person_text_field.insert(0,record_values[5])
    physical_address_text_field.insert(0,record_values[6])
    
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
    treeview_crm.insert(parent='',index='end',text="",values=(id_text_field.get(),\
        org_name_text_field.get(),project_text_field.get(),project_status_text_field.get(),\
        contacts_text_field.get(),contact_person_text_field.get(),physical_address_text_field.get()))
    count+=1

    
    #clear the boxes
    
    clear_text_fields_func()
def delete_all_records_from_table():
    onnec=sqlite3.connect("Allifmaal_CRM.db")
    my_cursor=connec.cursor()
    my_cursor.execute("DELETE FROM Allifmaal_CRM ")
    connec.commit()
    delete_all_records_func()

def update_record_in_database_func():#UPDATES BOTH IN DB AND TREEVIEW SCREEN
    
    #grab the record number of whatever is selected
    
    selected_variable=treeview_crm.focus()
    treeview_crm.item(selected_variable,text="",values=(id_text_field.get(),\
        org_name_text_field.get(),project_text_field.get(),project_status_text_field.get(),\
            contacts_text_field.get(),contact_person_text_field.get(),physical_address_text_field.get(),))
    
    #UPDATE DATABASE
    connec=sqlite3.connect("Allifmaal_CRM.db")
    my_cursor=connec.cursor()
    
    my_cursor.execute(""" UPDATE Allifmaal_CRM SET
                      
                        org_name = :org_name,
                        project = :project,
                        project_status = :project_status,
                        contacts = :contacts,
                        contact_person = :contact_person,
                        physical_address = :physical_address
                    
                        WHERE oid = :id""",
                            {
                            'org_name':org_name_text_field.get(),
                            'project':project_text_field.get(),
                            'project_status':project_status_text_field.get(),
                            'contacts':contacts_text_field.get(),
                            'contact_person':contact_person_text_field.get(),
                            'physical_address':physical_address_text_field.get(),
                            'id':id_text_field.get(),
                            }
                      )
    
    connec.commit()
    connec.close()
    
    clear_text_fields_func()

def add_data_to_database_from_front_end():
    
        
    connec=sqlite3.connect('Allifmaal_CRM.db')
    #create the cursor instance
    cursor_var=connec.cursor()
    
    #insert what is typed into table and use placeholder variables (those under values barakets).that is
    #dumy variables and each starts with colon
    #then create python dictionary that has key value pairs and the keys are those dumies under values and values are whatever in the text boxes
    cursor_var.execute("INSERT INTO Allifmaal_CRM VALUES(:id, :org_name,:project, :project_status, :contacts, :contact_person, :physical_address)",
                       {
                        'id': id_text_field.get(),
                       'org_name': org_name_text_field.get(),
                       'project':project_text_field.get(),
                       
                       'project_status': project_status_text_field.get(),
                       'contacts': contacts_text_field.get(),
                       'contact_person': contact_person_text_field.get(),
                       'physical_address': physical_address_text_field.get()   
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
    
""" def search_record_func():
    connec=sqlite3.connect("Allifmaal_CRM.db")
    my_cursor=connec.cursor()
    #student_list_box.delete(0,END)
    my_cursor.execute("SELECT * FROM Allifmaal_CRM WHERE id=?",org_name_text_field.get())
        
    rows=my_cursor.fetchall()
    print(rows)
    
    
    #student_list_box.insert(rows)
        
    connec.close()
    connec.close()
 """
def search(org_name="", project="",project_status="",contacts="",contact_person="",physical_address=""):  #to search for a given entry in the table given either the value of the title or author name
    my_cursor.execute("SELECT * FROM Allifmaal_CRM WHERE org_name=? OR project=? OR project_status=?OR contacts=? OR contact_person=? OR physical_address=?", (org_name, project,project_status,contacts,contact_person,physical_address))
    rows = my_cursor.fetchall()
    #print(rows)
    treeview_crm.delete(*treeview_crm.get_children())
    
    #print(rows)
    return rows
def search_command():       #to print the row we want based on title or author 
    #list1.delete(0, END)    #empty the list
    count=0
    treeview_crm.delete(*treeview_crm.get_children())
    for record in search(org_name_text_field.get(), project_text_field.get(), project_status_text_field.get(),\
         contacts_text_field.get(), contact_person_text_field.get(), physical_address_text_field.get()): #get the name of the title or the author and pass it to the search function of class DB
        #list1.insert(END, row) #will insert all the rows having the same value of
        print(record)########### it is returns...now print to the tv
        #treeview_crm.insert(values=(record[0],record[2],\
            #record[3],record[4],record[5],record[6],record[7]))
        
        treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[0],\
            record[1],record[2],record[3],record[4],record[5],record[6]))
        
        ''' treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[0],\
            record[1],record[2],record[3],record[4],record[5],record[6])) working without id '''
        
        #orign
        
        #treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[0],record[2],\
           # record[3],record[4],record[5],record[6],record[7]),tags=('evenrow',))
        
        
        
        #below working but not well
        #treeview_crm.insert(parent='',index='end',iid=count,text='',values=(record[1],record[2],\
            #record[3],record[4],record[5],record[6]))
        
        #####################################
        ###############################
        #############################################
        
        


def delete_selected_from_db_func():################# DELETE JUST BY SELECTION###########NOT WORKING
    
    connec=sqlite3.connect('Allifmaal_CRM.db')
    my_cursor=connec.cursor()
    selected_variable=treeview_crm.selection()[0]
    #messageDelete= tkinter.messagebox.askyesno ("","Do you want to permanently delete this record?")
    #if messageDelete > 0:
        #treeview_crm.delete(selected_variable)
    my_cursor.execute("DELETE FROM Allifmaal_CRM WHERE oid="+selected_variable)
    #else:
       # pass
    
    connec.commit()
    connec.close()

####################### END OF DELETE FUNCTION

############################ START OF  DELETE BY ID SELECTION##############
def delete_record_by_id_text_field_func():
    connec=sqlite3.connect('Allifmaal_CRM.db')
    my_cursor=connec.cursor()
    
    #clear entry boxes first
    clear_text_fields_func()
    
    #grab the selected record number
    selected_record=treeview_crm.focus()# this focus means whatever we clicked is required
    #grab the record values
    record_values=treeview_crm.item(selected_record,'values')#these values are the ones under the for loop 
    #insert the values of the selected record into the entry boxes
    #delete_all_records_func()
    
    id_text_field.insert(0,record_values[0])
    my_cursor.execute("DELETE from Allifmaal_CRM WHERE oid=" + id_text_field.get())
    id_text_field.delete(0, END)#clear the text field after deleteion
    #treeview_crm.delete(*treeview_crm.get_children())#clear the treeview after deletion
    #delete_all_records_func()
    delete_one_selected_variable=treeview_crm.selection()[0]
    treeview_crm.delete(delete_one_selected_variable)
    
    #query_database_with_primary_key()#inserts all values into treeview again
    connec.commit()
    connec.close()
    

def update_record_by_id_text_field_func():
    connec=sqlite3.connect('Allifmaal_CRM.db')
    my_cursor=connec.cursor()
    
    #clear entry boxes first
    clear_text_fields_func()
    
    #grab the selected record number
    selected_record=treeview_crm.focus()# this focus means whatever we clicked is required
    #grab the record values
    record_values=treeview_crm.item(selected_record,'values')#these values are the ones under the for loop 
    #insert the values of the selected record into the entry boxes
    #delete_all_records_func()
    
    delete_id_text_field.insert(0,record_values[2])
    my_cursor.execute("DELETE from Allifmaal_CRM WHERE oid=" + delete_id_text_field.get())
    
    delete_id_text_field.delete(0, END)#clear the text field after deleteion
    #treeview_crm.delete(*treeview_crm.get_children())#clear the treeview after deletion
    #delete_all_records_func()
    delete_one_selected_variable=treeview_crm.selection()[0]
    treeview_crm.delete(delete_one_selected_variable)
    
    #query_database_with_primary_key()#inserts all values into treeview again
    connec.commit()
    connec.close()

textfont=('helvetica',12,'bold')# this applies to all texts so long as they are referenced.
#height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE

buttons_frame=LabelFrame(root,text="Actions",bg="lightblue",font=('helvetica',12,'bold'))
buttons_frame.pack(fill="x",expand="yes",padx=20)

update_out_database_button=Button(buttons_frame,text="Update Treeview Record",command=update_record_out_database_func)
#update_out_database_button.grid(row=0,column=0,padx=10,pady=10)
update_in_database_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,text="Update",bg="green",command=update_record_in_database_func)
update_in_database_button.grid(row=0,column=1,padx=10,pady=10)

add_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="green",text="Add",command=add_data_to_database_from_front_end)
add_button.grid(row=0,column=0,padx=10,pady=10)
remove_all_button=Button(buttons_frame,bg="green",text="Remove All Records from TV",command=delete_all_records_func)
#remove_all_button.grid(row=0,column=2,padx=10,pady=10)
remove_one_button=Button(buttons_frame,bg="green",text="Remove one selected Record from TV",command=delete_one_selected_record_func)
#remove_one_button.grid(row=0,column=3,padx=10,pady=10)
remove_many_button=Button(buttons_frame,bg="green",text="Remove Many Selected Records from TV",command=delete_many_selected_records_func)
#remove_many_button.grid(row=0,column=4,padx=10,pady=10)
move_up_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="green",text="Move Up",command=move_row_up_func)
move_up_button.grid(row=0,column=5,padx=10,pady=10)
move_down_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="green",text="Move Down",command=move_row_down_func)
move_down_button.grid(row=0,column=6,padx=10,pady=10)
select_record_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="green",text="Select",command=select_record_func)
select_record_button.grid(row=0,column=2,padx=10,pady=10)
clear_text_field_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="green",text="Clear Fields",command=clear_text_fields_func)
clear_text_field_button.grid(row=0,column=6,padx=10,pady=10)

show_all_records_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="green",text="Show All",command=query_database_with_primary_key)
show_all_records_button.grid(row=0,column=5,padx=10,pady=10)

delete_selected_from_db_button=Button(buttons_frame,text="Delete selected from DB",command=delete_selected_from_db_func)
#delete_selected_from_db_button.grid(row=1,column=5,padx=10,pady=10)
delete_all_db_records_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="red",text="Delete All",command=delete_all_records_from_table)
delete_all_db_records_button.grid(row=0,column=7,padx=10,pady=10)
search_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,text="Search",command=search_command)
search_button.grid(row=0,column=4,padx=10,pady=10)


delete_record_by_id_text_field_from_db_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="red",text="Delete",command=delete_record_by_id_text_field_func)
delete_record_by_id_text_field_from_db_button.grid(row=0,column=3,padx=10,pady=10)
################################################################################################################


#
query_database_with_primary_key()#calling this function ensures that the data is on the treeview


connec.commit()

def calc():
    editor=Tk()
    editor.mainloop
    #the below system does a simple calculator
    editor.title("Allifmaal")
    editor.geometry("210x400")
    textfont=('verdana','15','bold')# this applies to all texts so long as they are referenced.

    #create the input field
    input_field=Entry(editor,width=30,borderwidth=5)
    input_field.grid(padx=10,pady=10,columnspan=3)

    #define button click funciton
    def button_click(number):
        current_num=input_field.get()
        input_field.delete(0,END)
        input_field.insert(0,str(current_num)+str(number))
    
    def add_func():
        first_num=input_field.get()
        global math
        global f_num
        math="addition"
        f_num=float(first_num)
        input_field.delete(0,END)
        
    def button_equal():
        second_num=input_field.get()
        input_field.delete(0,END)
        if math=="addition":
            input_field.insert(0,f_num+float(second_num))
        if math=="subtraction":
            input_field.insert(0,f_num-float(second_num))
        if math=="multiplication":
            input_field.insert(0,f_num*float(second_num))
        if math=="division":
            input_field.insert(0,f_num/float(second_num))
            
    def button_subtract():
        first_num=input_field.get()
        global math
        global f_num
        math="subtraction"
        f_num=float(first_num)
        input_field.delete(0,END)
        
    def button_multiply():
        first_num=input_field.get()
        global math
        global f_num
        math="multiplication"
        f_num=float(first_num)
        input_field.delete(0,END)
        
    def button_divide():
        first_num=input_field.get()
        global math
        global f_num
        math="division"
        f_num=float(first_num)
        input_field.delete(0,END)
        
    def button_clear():
        input_field.delete(0,END)
        
    #crete the buttons
    button_1 = Button(editor, text="1",command=lambda:button_click(1) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_1.grid(row=1,column=0)
    button_2 = Button(editor, text="2",command=lambda:button_click(2) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_2.grid(row=1,column=1)
    button_3 = Button(editor, text="3",command=lambda:button_click(3) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_3.grid(row=1,column=2)
    button_4 = Button(editor, text="4",command=lambda:button_click(4) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_4.grid(row=2,column=0)
    button_5 = Button(editor, text="5",command=lambda:button_click(5) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_5.grid(row=2,column=1)
    button_6 = Button(editor, text="6",command=lambda:button_click(6) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_6.grid(row=2,column=2)
    button_7 = Button(editor, text="7",command=lambda:button_click(7) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_7.grid(row=3,column=0)
    button_8 = Button(editor, text="8",command=lambda:button_click(8) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_8.grid(row=3,column=1)
    button_9 = Button(editor, text="9",command=lambda:button_click(9) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_9.grid(row=3,column=2)
    button_0 = Button(editor, text="0",command=lambda:button_click(0) ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_0.grid(row=4,column=0)
    button_clear = Button(editor, text="C",command=button_clear ,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_clear.grid(row=4,column=1)
    button_add = Button(editor, text="+",command=add_func,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_add.grid(row=4,column=2)
    button_subtract = Button(editor, text="-",command=button_subtract,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_subtract.grid(row=5,column=0)
    button_multiply = Button(editor, text="*",command=button_multiply,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_multiply.grid(row=5,column=1)
    button_divide = Button(editor, text="÷",command=button_divide,height=1, width=2, font=textfont,padx=5, pady=1, bg="#20378f", fg="white", bd=8, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_divide.grid(row=5,column=2)
    button_equal = Button(editor, text="=",command=button_equal,height=1, width=2, font=textfont,padx=80, pady=5, bg="#20378f", fg="white", bd=4, relief=GROOVE)  # FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
    button_equal.grid(row=6,column=0,columnspan=3)

    editor.mainloop()

calculator_button=Button(buttons_frame,bd=5,font=textfont ,relief=RAISED,padx=5, pady=1,height=2, width=10,bg="green",text="Calc",command=calc)
calculator_button.grid(row=0,column=8,padx=10,pady=10)

calculator_button=Button(buttons_frame,bg="green",text="Calculator",command=calc)
#calculator_button.grid(row=2,column=0,padx=10,pady=10)

            

root.mainloop()

############################ other tabs here.
""" mylabel=Label(root2,text="Stock")
mylabel.pack() """
root.mainloop()
main_root.mainloop()