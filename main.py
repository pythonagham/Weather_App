from tkinter import *
from tkinter import messagebox
import tkinter as tk
import requests
from time import strftime

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        API_key = "Your_Own_API_key"
        url = f"https://api.openweathermap.org/data/"\
              f"2.5/weather?q={city}&appid={API_key}"
        json_data=requests.get(url).json()
        condition=json_data["weather"][0]["main"]
        des=json_data["weather"][0]["description"]
        temp = int(json_data['main']['temp'] - 273.15)
        pressure=json_data["main"]["pressure"]
        humidity=json_data["main"]["humidity"]
        wind=json_data["wind"]["speed"]
        country=json_data["sys"]["country"]

        t.config(text=(str(temp) + "°C"))
        c.config(text=(condition))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=des)
        p.config(text=pressure)
        ct.config(text=f'{city}, {country}')

    except Exception as e:
        messagebox.showerror("Weather App",
                             "Invalid Entry!")

#search box
search_image=PhotoImage(file="search.png")
myimage=Label(image=search_image)
myimage.place(x=60,y=20)

textfield=tk.Entry(root,justify="center",
                   width=17,font=("poppins",
                   25,"bold"),bg="#404040",
                   border=0,fg="white")
textfield.place(x=85,y=40)
textfield.focus()

search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=search_icon, borderwidth=0,
                    cursor="hand2",bg="#404040",
                    command=getWeather)
myimage_icon.place(x=440,y=32)

#logo
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=190,y=110)

#bottom box
frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#label
label1=Label(root,text="Wind",
             font=("Helvetica",15,"bold"),
             fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="Humidity",
             font=("Helvetica",15,"bold"),
             fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="Description",
             font=("Helvetica",15,"bold"),
             fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="Pressure",
             font=("Helvetica",15,"bold"),
             fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),
        fg="#FA0053")
t.place(x=450,y=150)

c=Label(font=("arial",15,"bold"),
        fg="#414040")
c.place(x=455,y=255)

w=Label(text="...",font=("arial",20,"bold"),
        bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),
        bg="#1ab5ef")
h.place(x=270,y=430)

d=Label(text="...",font=("arial",20,"bold"),
        bg="#1ab5ef")
d.place(x=430,y=430)

p=Label(text="...",font=("arial",20,"bold"),
        bg="#1ab5ef")
p.place(x=670,y=430)

ct=Label(root,font=("arial",18,"bold"),fg="#0CBCE7")
ct.place(x=80, y=132)

clock=Label(font=("arial",16,"bold"),fg="#414040")
current_time=strftime('%I:%M %p')
clock.config(text=current_time)
clock.place(x=80,y=170)

root.mainloop()

