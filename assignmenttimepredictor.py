import pickle
from tkinter import *

model=pickle.load(open("assignmenttimepredictor.sav","rb"))


def calculatetime():
    p=int(entry_1.get())
    d=int(entry_02.get())
    a=[]
    a.append([p,d])
    ans=model.predict(a)
    lblans=Label(base,text=f'Total minutes required to complete the assignment are-: {ans[0]}',width=60,font=("bold",10))
    lblans.place(x=10,y=280)


base = Tk()
base.geometry('500x500')
base.title("ASSIGNMENT TIME PREDICTOR")

labl_0 = Label(base, text="Assignment Time Predictor", width=20, font=("bold", 20))
labl_0.place(x=90, y=53)

labl_1 = Label(base, text="Total Pages", width=20, font=("bold", 10))
labl_1.place(x=80, y=130)

entry_1 = Entry(base)
entry_1.place(x=240, y=130)

labl_2 = Label(base, text="Total Diagrams", width=20, font=("bold", 10))
labl_2.place(x=68, y=180)

entry_02 = Entry(base)
entry_02.place(x=240, y=180)

Button(base, text='Calculate',width=20,bg='brown',fg='white',command=calculatetime).place(x=180,y=240)

base.mainloop()