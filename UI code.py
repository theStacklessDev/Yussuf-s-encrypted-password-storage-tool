import tkinter

#configuring the window start
window = tkinter.Tk()
window.title("Password storage")
window.geometry("340x440")
window.configure(bg="#0276AB")
#configuring the window end

#Creating widgets start
app_title = tkinter.Label(window, text="Yussuf's secure password storage tool", bg="#0276AB" , font=("Calibri", 10))
website_label = tkinter.Label(window, text="Website :", bg="#0276AB")
website_entry = tkinter.Entry(window)
user_label = tkinter.Label(window, text="Username :", bg="#0276AB")
username_entry = tkinter.Entry(window)
password_entry = tkinter.Entry(window, show="*")
password_label = tkinter.Label(window, text="Password :", bg="#0276AB")
save_button = tkinter.Button(window, text="save")
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


window.mainloop()