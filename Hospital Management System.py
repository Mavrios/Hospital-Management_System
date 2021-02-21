import tkinter
from PIL import ImageTk, Image

def Welcome():
    global Label1, Label2, Button1
    Label2.destroy()
    Button1.destroy()
    WelcomeLabel = tkinter.Label(root,text = "\nHospital Management System\n" ,bg = "white", fg = "dodgerblue" ,font = "Impact 24").pack()
    AdminButton  = tkinter.Button(root,text = "Admin Mode" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" , width = "20" , command= AdminMode ).pack()
    FreeLabel    = tkinter.Label(root,text = "\n" ,bg ="white").pack()
    UserButton   = tkinter.Button(root,text = "User Mode" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" , width = "20"  ).pack()


def AdminMode():
    global root , WarningWindow
    AdminWindow = tkinter.Toplevel(root)
    AdminWindow.geometry("800x600+750+350")
    AdminWindow.title("Admin Mode")
    AdminWindow.iconbitmap(r"Icon.ico")
    AdminWindow.configure(background="dimgray")
    AdminFile = open("Admin" , "r")
    DEBUG = AdminFile.read()
    print("Before->"+DEBUG)
    if DEBUG != "x":
        AdminFile.close()
        AdminFile = open("Admin","w")
        FirstLoginLabel  = tkinter.Label(AdminWindow , text = "\nFirst Login\n", bg="dimgray" ,fg = "dodgerblue" , font= "Impact 24" ).grid(row = 0 , column= 5)
        FirstLoginLabel2 = tkinter.Label(AdminWindow , text = "Please Set Username and Password\n", bg="dimgray" ,fg = "dodgerblue" , font= "Impact 24" ).grid(row = 1 , column= 5)
        UserNameLabel    = tkinter.Label(AdminWindow , text= "Username" , bg="dimgray" ,fg = "dodgerblue" , font= "Impact 24").grid()

        # WarningWindow = tkinter.Toplevel(AdminWindow)
        # WarningWindow.geometry("+1050+650")
        # WarningWindow.title("Warning")
        # WarningWindow.iconbitmap(r"Icon.ico")
        # WarningWindow.configure(background="white")
        # WarningLabel  = tkinter.Label(WarningWindow , text= "First Login" , bg= "white" , fg = "dodgerblue" , font= "Impact").pack()
        # WarningButton = tkinter.Button(WarningWindow , text= "Ok" , bg= "dimgray" , fg = "dodgerblue" ,  font = "Impact" , command = WarningWindow.destroy).pack()
        AdminFile.write("TRUE")
        AdminFile.close()
        AdminFile = open("Admin" , "r")
        DEBUG = AdminFile.read()
        print("After->"+DEBUG)





root = tkinter.Tk()
root.geometry("800x600+700+300")
root.title("Hospital Management System")
root.iconbitmap(r"Icon.ico")
root.configure(background="White")
root.resizable(False,False)

My_Pic = Image.open("Cover.jpg")
resize = My_Pic.resize((800,200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resize)
Label1 = tkinter.Label(root,image = photo , width= 800 )
Label1.pack()
Label2 = tkinter.Label(root,text = "\n\nWelcome To Hospital Management System\n\n",bg= "White" ,fg= "dodgerblue" ,font="Impact 24")
Label2.pack()

Button1 = tkinter.Button(root , text="Continue" , bg="dimgray" ,fg="dodgerBlue" , font="Impact 24" ,width="20" , command=Welcome)
Button1.pack()
root.mainloop()
