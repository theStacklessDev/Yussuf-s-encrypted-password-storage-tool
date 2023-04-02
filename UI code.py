import tkinter

#configuring the window start
window = tkinter.Tk()
window.title("Password storage")
window.geometry("340x440")
window.configure(bg="#0276AB")
#configuring the window end

#Framing the window start (Making it responsive)
frame = tkinter.Frame(bg="#0276AB")
#Framing the window (Making it responsive)


#Creating widgets start
app_title = tkinter.Label(frame, text="Yussuf's secure password storage tool", bg="#0276AB" , font=("Calibri", 10))
website_label = tkinter.Label(frame, text="Website :", bg="#0276AB")
website_entry = tkinter.Entry(frame)
user_label = tkinter.Label(frame, text="Username :", bg="#0276AB")
username_entry = tkinter.Entry(frame)
password_entry = tkinter.Entry(frame, show="*")
password_label = tkinter.Label(frame, text="Password :", bg="#0276AB")
save_button = tkinter.Button(frame, text="Save & Encrypt")
#creating widgets end

#placing widgets start
app_title.grid(row=2, column=1, pady= 20)
website_entry.grid(row=3, column=1, padx=10, pady=10)
website_label.grid(row=3, column=0)
user_label.grid(row=4, column=0, padx= 10, pady=10)
username_entry.grid(row=4, column=1)
password_label.grid(row=5, column=0, padx=10, pady=10)
password_entry.grid(row=5, column=1)
save_button.grid(row=7,column=1)
#placing widgets end

frame.pack()

window.mainloop()
