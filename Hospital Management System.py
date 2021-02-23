import tkinter
from PIL import ImageTk, Image
SecurityData = list()

AdminFile = open("Admin" , "r")
SecurityData = AdminFile.readlines()
print(SecurityData)
AdminFile.close()
Counter = 2

def Welcome():
    global Label1, Label2, Button1
    Label2.destroy()
    Button1.destroy()
    WelcomeLabel = tkinter.Label(root,text = "\nHospital Management System\n" ,bg = "white", fg = "dodgerblue" ,font = "Impact 24").pack()
    AdminButton  = tkinter.Button(root,text = "Admin Mode" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" , width = "20" , command= AdminMode ).pack()
    FreeLabel    = tkinter.Label(root,text = "\n" ,bg ="white").pack()
    UserButton   = tkinter.Button(root,text = "User Mode" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" , width = "20"  ).pack()


def AdminMode():
    global root , AdminWindow , UserNameEntry , PasswordEntry , FirstLoginLabel ,FirstLoginLabel2 ,UserNameLabel ,PasswordLabel, SaveButton , LoginLabel , EnterButton
    AdminWindow = tkinter.Toplevel(root)
    AdminWindow.geometry("800x600+750+350")
    AdminWindow.title("Admin Mode")
    AdminWindow.iconbitmap(r"Icon.ico")
    AdminWindow.configure(background="white")
    i = 0
    while i < 12:
        AdminWindow.grid_columnconfigure(i,minsize = 30)
        AdminWindow.grid_rowconfigure(i,minsize = 30)
        i+=1


    # Security = AdminFile.read()
    # print("Before->"+Security)
    if not SecurityData:
        FirstLoginLabel  = tkinter.Label(AdminWindow , text = "First Login", bg="white" ,fg = "red" , font= "Impact 24" )
        FirstLoginLabel.grid(row = 1 , column= 2)
        FirstLoginLabel2 = tkinter.Label(AdminWindow , text = "       Please Set Username and Password\n", bg="white" ,fg = "dodgerblue" , font= "Impact 24" )
        FirstLoginLabel2.grid(row = 2 , column= 2)
        UserNameLabel    = tkinter.Label(AdminWindow , text= "Username" , bg="white" ,fg = "dodgerblue" , font= "Impact 18")
        UserNameLabel.grid(row = 7 , column= 1)
        PasswordLabel    = tkinter.Label(AdminWindow , text= "Password" , bg="white" ,fg = "dodgerblue" , font= "Impact 18")
        PasswordLabel.grid(row = 10 , column= 1)
        UserNameEntry    = tkinter.Entry(AdminWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
        UserNameEntry.grid(row= 7 , column= 2)
        PasswordEntry    = tkinter.Entry(AdminWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 ,show= "*")
        PasswordEntry.grid(row= 10 , column= 2)
        SaveButton       = tkinter.Button(AdminWindow , text = "Save" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" , command= SecurityAdminData)
        SaveButton.grid(row= 12 , column= 2)
        # WarningWindow = tkinter.Toplevel(AdminWindow)
        # WarningWindow.geometry("+1050+650")
        # WarningWindow.title("Warning")
        # WarningWindow.iconbitmap(r"Icon.ico")
        # WarningWindow.configure(background="white")
        # WarningLabel  = tkinter.Label(WarningWindow , text= "First Login" , bg= "white" , fg = "dodgerblue" , font= "Impact").pack()
        # WarningButton = tkinter.Button(WarningWindow , text= "Ok" , bg= "dimgray" , fg = "dodgerblue" ,  font = "Impact" , command = WarningWindow.destroy).pack()
        # AdminFile.write("TRUE")
        AdminFile.close()
        # AdminFile = open("Admin" , "r")
        # Security = AdminFile.read()
        # print("After->"+Security)
    else:
        LoginLabel = tkinter.Label(AdminWindow , text = "  Please Enter Username and Password", bg="white" ,fg = "red" , font= "Impact 24" )
        LoginLabel.grid(row = 1 , column= 2)
        UserNameLabel    = tkinter.Label(AdminWindow , text= "Username" , bg="white" ,fg = "dodgerblue" , font= "Impact 18")
        UserNameLabel.grid(row = 7 , column= 1)
        PasswordLabel    = tkinter.Label(AdminWindow , text= "Password" , bg="white" ,fg = "dodgerblue" , font= "Impact 18")
        PasswordLabel.grid(row = 10 , column= 1)
        UserNameEntry    = tkinter.Entry(AdminWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
        UserNameEntry.grid(row= 7 , column= 2)
        PasswordEntry    = tkinter.Entry(AdminWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 ,show= "*")
        PasswordEntry.grid(row= 10 , column= 2)
        EnterButton       = tkinter.Button(AdminWindow , text = "Enter" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" ,command= AdminLoginChecker)
        EnterButton.grid(row= 12 , column= 2)


def SecurityAdminData():
    # global UserNameEntry , PasswordEntry , AdminWindow
    AdminFile = open("Admin","w")
    Username = str(UserNameEntry.get())
    AdminFile.write(Username + "\n")
    AdminFile.write(PasswordEntry.get())
    AdminFile.close()
    FirstLoginLabel.destroy()
    FirstLoginLabel2.destroy()
    UserNameLabel.destroy()
    PasswordLabel.destroy()
    UserNameEntry.destroy()
    PasswordEntry.destroy()
    SaveButton.destroy()
    
def AdminLoginChecker():
    global SecurityData , AdminWindow , Counter ,LoginLabel , EnterButton , TriesLabel
    Username = SecurityData[0]
    if  (UserNameEntry.get() == (SecurityData[0]).rstrip())  and (PasswordEntry.get() == SecurityData[1]):
        print("True")
        # Function to Display Admin Options
    else:
        if Counter <= 0:
            LoginLabel.destroy()
            UserNameLabel.destroy()
            PasswordLabel.destroy()
            UserNameEntry.destroy()
            PasswordEntry.destroy()
            EnterButton.destroy()
            # TriesLabel.destroy()
            TriesLabel = tkinter.Label(AdminWindow , text= "\t     Remaining Tries " + str(Counter)  ,  bg="white" ,fg = "red" , font= "Impact 24" )
            TriesLabel.grid(row = 2 , column= 2)
            BlockingLabel = tkinter.Label(AdminWindow , text= "\t   System Blocked" , bg="white" ,fg = "red" , font= "Impact 30" )
            BlockingLabel.grid(row=7 , column= 2)
        else:
            TriesLabel = tkinter.Label(AdminWindow , text= "Remaining Tries " + str(Counter)  ,  bg="white" ,fg = "red" , font= "Impact 24" )
            TriesLabel.grid(row = 2 , column= 2)
            Counter-=1



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
