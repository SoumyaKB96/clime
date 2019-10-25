from tkinter import *
import backend

window=Tk()
window.title("Clime")


def get_city():
    res=backend.backend_city_name(city.get())
    if not res:
        t1.insert(END,"Sorry...City Not found!!")
    else:
        t1.delete(1.0,END)
        d1=res["main"]
        d2=res['weather']
        d2=d2[0]
        t1.insert(END,"Conditions :  \t")
        t1.insert(END,d2["description"])
        t1.insert(END,"\n")
        t1.insert(END,"Temperature : \t")
        t1.insert(END,round((d1["temp"]-273.15),1))
        t1.insert(END," \u2103 \n")
        t1.insert(END,"Humidity :\t \t")
        t1.insert(END,(d1["humidity"]))
        t1.insert(END,"% \n")
        t1.insert(END,"Min.:\t\t")
        t1.insert(END,round((d1["temp_min"]-273.15),1))
        t1.insert(END," \u2103 \n")
        t1.insert(END,"Max. :\t\t")
        t1.insert(END,round((d1["temp_max"]-273.15),1))
        t1.insert(END," \u2103 \n")


def clear_command():
    e1.delete(0,END)
    t1.delete(1.0,END)

l1=Label(window,text="City")
l1.grid(row=1,column=1)

l1=Label(window,text="Weather")
l1.grid(row=2,column=2)

city=StringVar()
e1=Entry(window,textvariable=city)
e1.grid(row=1,column=2)


t1=Text(window,height=8,width=30)
t1.grid(row=3,column=2)

b1=Button(window,text="Search",command=get_city)
b1.grid(row=1,column=3)

b2=Button(window,text="  Clear ",command=clear_command)
b2.grid(row=2,column=3)



window.mainloop()
