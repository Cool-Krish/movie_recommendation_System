import tkinter as tk
import pymysql
from tkinter import *
from tkinter import messagebox, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import getpass
import PIL


db = pymysql.Connect(host="localhost",user="root",password="",db="movies")

cursor = db.cursor()

def submitact():
    user = Username.get()
    passw = password.get()

    print(f"""The name entered by you is {user}""")

    logintodb(user)
    openHome()

def openHome():
     canvas = tk.Tk()
     canvas.title("Home Page")
     canvas.geometry('500x400')
     canvas.configure(bg='peachpuff')

     ttk.Label(canvas, text="Movie Recommendation system",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=0, column=1)


     ttk.Label(canvas, text="Please choose the movie you like",
              background='blue', foreground="white",
              font=("Times New Roman", 12)).grid(row=10, column=1)


     ttk.Label(canvas, text="Select the Movie :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=14, padx=10, pady=25)

     seeallbtn = tk.Button(canvas, text="Movies of 2020", command=seeall)
     seeallbtn.place(x=180, y=310, width=150)


     n = tk.StringVar()
     monthchoosen = ttk.Combobox(canvas, width=27, textvariable=n)


     monthchoosen['values'] = ('Street Dancer 3D',
                              'Pati Patni Aur Woh',
                              'Bhoot (Vicky Kaushal)',
                              'Tanhaji- the Unsung Warrior',
                              )

     def checkcmbo():

         if monthchoosen.get() == "Street Dancer 3D":
            messagebox.showinfo("What user choose", "Do you like Street Dancer 3D ?")



            sql = "select * from streetdancer"
            assert isinstance(cursor, sql)
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Drama Movies")
            SciFi.geometry("800x800")
            SciFi.config(bg = "Lightblue")


            def create_graph():
                labels = ['Laal Singh Chaddha', 'Chehre', 'Jhund', 'Jawaani Jaaneman', 'Panga']
                sizes = [0, 0, 0, 464700, 339400]
                colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple','red']

                patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.title('Most Liked Movie by Critics')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()


            def openNewWindow():


                newWindow = Toplevel(SciFi)


                newWindow.title("Graph")


                newWindow.geometry("900x900")


                Label(newWindow,
                      print(plt)).pack()

            btn = Button(SciFi, text = "Wanna Compare?", command = create_graph )
            btn.pack(pady = 100)


            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)


            tv = ttk.Treeview(frm, columns=(1, 2, 3, 4), show="headings", height="10")
            tv.pack()

            def read_file(streetdancer):
             with open("streetdancer", 'rb') as f:
                 photo = f.read()
             return photo


            tv.heading(1, text="Movie_name")
            tv.heading(2, text="Actor")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Director")

            for i in rows:
                tv.insert('', 'end', values=i)




            SciFi.mainloop()

         elif monthchoosen.get() == "Pati Patni Aur Woh":
            messagebox.showinfo("What user choose", "Do you like Pati Patni Aur Woh ?")

            sql = "select * from patipatni"
            assert isinstance(cursor, object)
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("RomCom Movies")
            SciFi.geometry("800x800")
            SciFi.config(bg="deepskyblue")


            def create_graph():

                labels = ['Love Aaj Kal', 'Bhool Bhulaiyaa 2','Shubh Mangal Zyada Saavdhan', 'Coolie No. 1','Jayeshbhai Jordaar','Roohi Afzana']
                sizes = [545700, 0, 575800, 0, 0, 0]
                colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple','red']

                patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.title('Most Liked Movie by Critics')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()


            def openNewWindow():



                newWindow = Toplevel(SciFi)



                newWindow.title("Graph")


                newWindow.geometry("900x900")


                Label(newWindow,
                      print(plt)).pack()

            btn = Button(SciFi, text = "Wanna Compare?", command = create_graph )
            btn.pack(pady = 100)



            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_name")
            tv.heading(2, text="Actor")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Director")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()


         elif monthchoosen.get() == "Bhoot (Vicky Kaushal)":
            messagebox.showinfo("What user choose", "Do you like Bhoot (Vicky Kaushal) ?")

            sql = "select * from bhoot"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Horror Movies")
            text = Text(SciFi, height = 2, width = 50)
            text.insert(INSERT, "Due to 2020 situations, Only the displayed movies are released.")
            #TkHeadingFont
            text.pack()
            SciFi.geometry("800x800")
            SciFi.config(bg="deepskyblue")




            def create_graph():

                labels = ['Ghost Stories', 'Guilty','The Girl on the Train', 'Mumbai Saga']
                sizes = [365800, 308500, 0, 0]
                colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple','red']

                patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.title('Most Liked Movie by Critics')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()


            def openNewWindow():



                newWindow = Toplevel(SciFi)


                newWindow.title("Graph")


                newWindow.geometry("900x900")


                Label(newWindow,
                      print(plt)).pack()

            btn = Button(SciFi, text = "Wanna Compare?", command = create_graph )
            btn.pack(pady = 100)

            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_name")
            tv.heading(2, text="Actor")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Director")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()

         elif monthchoosen.get() == "Tanhaji- the Unsung Warrior":
            messagebox.showinfo("What user choose", "Do you like Tanhaji- the Unsung Warrior ?")

            sql = "select * from tanhaji"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Historical movies")
            SciFi.geometry("850x600")
            SciFi.config(bg="darkgray")




            def create_graph():

                labels = ['Laal Singh Chaddha', 'Brahmastra', 'Malang', 'Baaghi 3', 'Prithviraj']
                sizes = [0, 0, 437700, 618500, 0]
                colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple','red']

                patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.title('Most Liked Movie by Critics')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()


            def openNewWindow():


                newWindow = Toplevel(SciFi)


                newWindow.title("Graph")


                newWindow.geometry("900x900")


                Label(newWindow,
                      print(plt)).pack()

            btn = Button(SciFi, text = "Wanna Compare?", command = create_graph )
            btn.pack(pady = 100)

            frm = Frame(SciFi)
            frm.place(x=50, y=100, width=800)
            frm.pack(side=tk.LEFT, padx=20)



            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="7")
            tv.place(x=20, y=100)
            tv.pack()

            tv.heading(1, text="Movie_name")
            tv.heading(2, text="Actor")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Director")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()


         elif monthchoosen.get() == "":
            messagebox.showinfo("nothing to show!", "you have to be choose something")

     Nexttkk = ttk.Button(canvas,text="Next",command=checkcmbo)
     Nexttkk.grid(column=1, row=20)

     monthchoosen.grid(column=1, row=14)
     monthchoosen.current()
     canvas.mainloop()

def logintodb(user):
    savequery = "select * from login where username = %s"
    try:
        cursor.execute(savequery, (user))
        db.commit()
        print("Feedback saved succesfully")
    except:
        db.rollback()
        print("Error occured")

def seeall():
    sql = "select * from movie"
    cursor.execute(sql)
    rows = cursor.fetchall()
    total = cursor.rowcount
    print("Total Data entries" + str(total))

    obj = tk.Tk()
    obj.title("All Movies")
    obj.geometry("1050x700")
    obj.config(bg="black")

    frm = Frame(obj)
    #frm.pack(padx=20)
    frm.place(x = 20, y = 20, width = 1020)

    tv = ttk.Treeview(frm, columns=(1, 2, 3, 4), show="headings", height="32")
    tv.pack(fill = tk.X )
    tv.pack()

    tv.heading(1, text="Movie_name")
    tv.heading(2, text="Movie_Director")
    tv.heading(3, text="Celeb")
    tv.heading(4, text="Genre")

    for i in rows:
        tv.insert('', 'end', values=i)

    obj.resizable(FALSE, FALSE)
    obj.mainloop()

def regbtnact():

    def loginact():
        Regpage.destroy()

    def registeract():
        userreg = Usernamereg.get()
        passwreg = passwordreg.get()

        print(
            f"""The name entered by you is {userreg}  
               """)
        regtodb(userreg, passwreg)

    Regpage = Toplevel()
    Regpage.geometry('400x400')
    Regpage.title("Register page")
    my = Canvas(Regpage, bg="blue", height=400, width=400)



    background_label1 = Label(Regpage,bg='cornflowerblue')
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)


    lblreg = tk.Label(Regpage, text="Username - ", )
    lblreg.place(x=50, y=20)
    Usernamereg = tk.Entry(Regpage, width=35)
    Usernamereg.place(x=150, y=20, width=100)

    lbl2reg = tk.Label(Regpage, text="Password - ")
    lbl2reg.place(x=50, y=50)
    passwordreg = tk.Entry(Regpage, width=35, show = "*")
    passwordreg.place(x=150, y=50, width=100)

    regbtn = tk.Button(Regpage, text="Register", bg='gold', command=registeract)
    regbtn.place(x=120, y=120, width=55)

    regsitermsg = tk.Label(Regpage, text="Already a User? Click on Login - ")
    regsitermsg.place(x=10, y=250)
    logbtn = tk.Button(Regpage, text="Login", bg='gold', command=loginact)
    logbtn.place(x=190, y=250, width=55)
    Regpage.mainloop()



def regtodb(userreg,passwreg):
    regquery = "insert into login values(%s,%s)"
    try:
        cursor.execute(regquery, (userreg,passwreg))
        db.commit()
        print("Registered Successfully")
        msg = tk.messagebox.askquestion('Welcome msg', f"""Hello {userreg} your account was succesfully created! Select YES to visit Home Page""", )

        if msg == 'yes':
            openHome()
        else:
            messagebox.destroy()
    except:
        db.rollback()
        print("Error Occurred, Cannot Register!")



root = tk.Tk()
root.geometry("600x550")
root.title("Movie Recommendation System")

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file="C:/Users/Lenovo/Desktop//moviecalender1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=150, y=150)
Username = tk.Entry(root, width=35)
Username.place(x=300, y=150, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=150, y=250)
password = tk.Entry(root, width=35, show = "*")
password.place(x=300, y=250, width=100)


submitbtn = tk.Button(root, text="LOGIN", bg='orange', command=submitact)
submitbtn.place(x=240, y=300, width=55)

regsitermsg = tk.Label(root, text="New User?, Please Register First - ")
regsitermsg.place(x=10, y=510)



regbtn = tk.Button(root,text="REGISTER", bg = 'light blue',command=regbtnact)
regbtn.place(x=200,y=510,width=65)




root.mainloop()
