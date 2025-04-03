from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter
# import numpy as np
import random
import pymysql
import csv
from datetime import datetime
import csv

Window=tkinter.Tk()
Window.title("Inventory Management System")
Window.geometry("800x600")
my_tree=ttk.Treeview(Window,show="headings",height=20)

# add styling
style=ttk.Style()

placeholderArray=('','','','','')
# genrate database
NUMERIC="1234567890"
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# connecting my MYSQL
def connection():
    conn=pymysql.connect(
        user="root",
        host="localhost",
        password="2004",
        db="inventory"
    )
    return conn
conn=connection()
cursor=conn.cursor()

# function that save data to MYSQL database
def savedata():
    conn = connection()
    if not conn:
        return
    cursor = conn.cursor()
    
    itemID = itemIDEntry.get()
    name = nameIDEntry.get()
    prize = prizeIDEntry.get()
    quantity = quantityIDEntry.get()
    category = categorybombo.get()
    
    if not (itemID and name and prize and quantity and category):
    #message box
        messagebox.showwarning("Input Error", "Fill the Data properly")
        return
    
    try:
        cursor.execute("INSERT INTO inventory (itemID, name, prize, quantity, category) VALUES (%s, %s, %s, %s, %s)",
                       (itemID, name, prize, quantity, category))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted to MYSQL successfully!")
        refreshtable()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert data: {e}")
    finally:
        conn.close()
# 

for i in range(0,5) :
    read=[  ]

def read():
    cursor.connection.ping()
    # sql = "INSERT INTO inventory (itemID, name, price, quantity, category) VALUES (%s, %s, %s, %s, %s)"

    sql = "SELECT * from inventory"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    # conn.close()
    return results


# read = [
#     ["dedwd", "dedwd", "dedwd", "dedwd", "dedwd", "eeeefe"],
#     ["dedwd", "dedwd", "dedwd", "dedwd", "dedwd", "dcd"],
# ]


def refreshtable():   
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent="",index="end",values=array,iid=array,text="",tags="orow")
        my_tree.tag_configure("orow",background="white")
        my_tree.grid()
        

# genrating random ID's
def genraterand():
    itemID="".join(random.choices(NUMERIC,k=4))+"-"+random.choice(alpha)
    itemIDEntry.delete(0,END)
    itemIDEntry.insert(0,itemID)


#  Creating a placeholder variable
    placeholderArray="tkinter.StringVar()"
    
# wroking on select button
def select_data():
    selected=my_tree.focus()
    if not selected:
        messagebox.showwarning("ERROR","Data Is Not Selected")
        return 
    values=my_tree.item(selected,"values")
    if values:
        itemIDEntry.delete(0,END)
        nameIDEntry.delete(0,END)
        prizeIDEntry.delete(0,END)
        quantityIDEntry.delete(0,END)
        categorybombo.set("")
    # incert value in data field
        itemIDEntry.insert(0,values[0])
        nameIDEntry.insert(0,values[1])
        prizeIDEntry.insert(0,values[2])
        quantityIDEntry.insert(0,values[3])
        categorybombo.set(values[4])
        
#working on update button
def update():
    selected=my_tree.focus()
    if not selected:
        messagebox.showerror("Data is not selected") 
        return
    conn=connection()
    cursor=conn.cursor()
    
    cursor.execute("""
        UPDATE inventory SET name=%s, prize=%s, quantity=%s, category=%s 
        WHERE itemID=%s""",
        (nameIDEntry.get(), prizeIDEntry.get(), quantityIDEntry.get(), categorybombo.get(), itemIDEntry.get()))
   
    conn.commit()
    conn.close()
    messagebox.showinfo("success","UPDATED successfully")
    
    refreshtable()

# working on delete button
def delete():
    conn=connection()
    cursor=conn.cursor()
    itemid=itemIDEntry.get()
    sql = "DELETE FROM inventory WHERE itemID=%s"
    cursor.execute(sql,(itemid))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Record Deleted Successfully")
    refreshtable()
    
# clearing data
def clear():
    itemIDEntry.delete(0, END)
    nameIDEntry.delete(0, END)
    prizeIDEntry.delete(0, END)
    quantityIDEntry.delete(0, END)
    categorybombo.set("")
    
    
# Export to csv(EXCEL)
def export_csv():
    with open("inventory_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item ID", "Name", "Price", "Quantity", "Category", "Date"])
        for row in read():
            writer.writerow(row)
    messagebox.showinfo("Success", "Data Exported to inventory_data.csv")
    
    


# main frame
Frame=ttk.Frame(Window)
Frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# button color
btncolor="#196E78"

# Creating button frame
manageFrame=LabelFrame(Frame,text="Manage",width=5,borderwidth=5)
manageFrame.grid(row=0, column=0, columnspan=8, padx=10, pady=10, sticky="ew")

# creating buttons
saveBtn=Button(manageFrame,text="Save",bg=btncolor,fg="white",width=14,borderwidth=3,command=savedata)
updateBtn=Button(manageFrame,text="Update",bg=btncolor,fg="white",width=14,borderwidth=3,command=update)
deleteBtn=Button(manageFrame,text="Delete",bg="black",fg="red",width=14,borderwidth=3,command=delete)
selectBtn=Button(manageFrame,text="Select",bg=btncolor,fg="white",width=14,borderwidth=3,command=select_data)
# findBtn=Button(manageFrame,text="Find",bg=btncolor,fg="white",width=10,borderwidth=3)
clearBtn=Button(manageFrame,text="Clear",bg=btncolor,fg="white",width=14,borderwidth=3,command=clear)
exportBtn=Button(manageFrame,text="Export to csv",bg="green",fg="white",width=14,borderwidth=3,command=export_csv)


saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn.grid(row=0,column=3,padx=5,pady=5)
selectBtn.grid(row=0,column=4,padx=5,pady=5)
# findBtn.grid(row=0,column=5,padx=5,pady=5)
clearBtn.grid(row=0,column=6,padx=5,pady=5)
exportBtn.grid(row=0,column=7,padx=5,pady=5)

# creating frame for entries
entriesFrame=LabelFrame(Frame,text="form",borderwidth=5)
entriesFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  

# creating entries frame
itemIDLabel=ttk.Label(entriesFrame,text="ITEM ID",anchor="e",width=10)
nameIDLabel=ttk.Label(entriesFrame,text="NAME",anchor="e",width=10)
prizeIDLabel=ttk.Label(entriesFrame,text="PRIZE",anchor="e",width=10)
quantityIDLabel=ttk.Label(entriesFrame,text="QUANTITY",anchor="e",width=10)
categoryIDLabel=ttk.Label(entriesFrame,text="CATEGORY",anchor="e",width=10)

itemIDLabel.grid(row=0, column=0, padx=10, pady=5,sticky="w")
nameIDLabel.grid(row=1, column=0, padx=10, pady=5,sticky="w")
prizeIDLabel.grid(row=2, column=0, padx=10, pady=5,sticky="w")
quantityIDLabel.grid(row=3, column=0, padx=10, pady=5,sticky="w")
categoryIDLabel.grid(row=4, column=0, padx=10, pady=5,sticky="w")

# creating category Array
categoryArray=["Electronics","Clothing & Apparel","Footwear","Home & Kitchen","Furniture","Grocery & Food Items","Beauty & Personal Care","Sports & Fitness"]

# creating entry fields
itemIDEntry=ttk.Entry(entriesFrame,width=65)
nameIDEntry=ttk.Entry(entriesFrame,width=65)
prizeIDEntry=ttk.Entry(entriesFrame,width=65)
quantityIDEntry=ttk.Entry(entriesFrame,width=65)
# select multi category
categorybombo=ttk.Combobox(entriesFrame,width=62,values=categoryArray)

# 
itemIDEntry.grid(row=0,column=1,sticky="e")
nameIDEntry.grid(row=1,column=1,sticky="e")
prizeIDEntry.grid(row=2,column=1,sticky="e")
quantityIDEntry.grid(row=3,column=1,sticky="e")
categorybombo.grid(row=4,column=1,sticky="e")

# cenrate button
gnbtn=Button(entriesFrame,text="GENERATE ID",bg="blue",fg="white",borderwidth=3,command=genraterand)
gnbtn.grid(row=0,column=2,padx=10,pady=5,sticky="w")

# add styling
style.configure(Window)
my_tree["columns"]=("itemID","nameID","prizeID","quantityID","categoryID","dateID")

my_tree.column("itemID",anchor="w",width=90)
my_tree.column("nameID",anchor="w",width=100)
my_tree.column("prizeID",anchor="w",width=120)
my_tree.column("quantityID",anchor="w",width=130)
my_tree.column("categoryID",anchor="w",width=140)
my_tree.column("dateID",anchor="w",width=150)

my_tree.heading("itemID",text="ITEM ID",anchor="w")
my_tree.heading("nameID",text="NAME",anchor="w")
my_tree.heading("prizeID",text="PRIZE",anchor="w")
my_tree.heading("quantityID",text="QUANTITY",anchor="w")
my_tree.heading("categoryID",text="CATEGORY",anchor="w")
my_tree.heading("dateID",text="DATE",anchor="w")

my_tree.tag_configure("oddrow",background="white")
my_tree.grid()

refreshtable()
Window.resizable(False,False)
Window.mainloop()

    