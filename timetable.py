from tkinter import *
from tkinter import ttk, messagebox
from tkinter.constants import LEFT, BOTTOM, END

top = Tk()
top.title("Time Management Maker")

schedule = []

#Section for Time:
L1 = Label(top, text="Enter Time: ", font = ("Calibri", "11","bold"))
L1.pack()
E1 = Entry(top, bd=3, bg='light yellow')
E1.pack()
E1.insert(END, '(To be changed) 5:30')

#Section for Work:
L2 = Label(top, text="Enter Work: ", font = ("Calibri", "11","bold"))
L2.pack()
E2 = Entry(top, bd=3, bg='light yellow')
E2.pack()
E2.insert(END, '(To be changed) Feeding corgi')

#Section for Note:
L3 = Label(top,text="Additional Note: ", font = ("Calibri", "11","bold"))
L3.pack()
E3 = Entry(top, bd=1, bg='light yellow')
E3.pack()
E3.insert(END, '(To be changed) Use Pedigree')

#Add to the Time Table:
def add_schedule():
    schedule.append([E1.get(),E2.get(), E3.get()])
    welcome()

#Delete from the Time Table:
def delete_schedule():
    n=len(schedule)
    for i in range (0,n):
        if (E1.get()==schedule[i][0]):
            del schedule[i]
            break
    welcome()

#New Window for Time Table result:
def welcome():
    root = Tk()
    root.title("Time Management Maker (Treeview)")

    #General form for the tree:
    tree = ttk.Treeview(root)
    tree['columns'] = ("one","two","three")
    tree.column("one", width=200)
    tree.column("two", width=200)

    #Choose what and how to print on the tree:  
    n=len(schedule)
    for i in range (0,n):
        tree.insert("", i, text=schedule[i][0], values=(schedule[i][1], schedule[i][2]))
    tree.pack()
    tree.bind('<<TreeviewSelect>>')
    
#Button to generate the tree:
    #Add:
b1 = Button(top, text="Add to table", font= ("Calibri", "10"), bg='coral', command = add_schedule)
b1.pack()
    #Delete:
b2 = Button(top, text="Remove from table", font= ("Calibri", "10"), command = delete_schedule)
b2.pack()

#Main window:
top.geometry("300x300")
top.mainloop()