import tkinter
from tkinter import font
from tkinter.constants import CENTER, E, END, N, NE, W
from PIL import ImageTk, Image
import json
import ast
import pygame

PatientDict = dict()
SecurityData = list()
Departments  = list()
DepartmentsStrip = list()
DoctorName = list()
ReservedID = list()
ReservedIdstriped = list()
IDFile = open("Reserved ID" , "r")
ReservedID = IDFile.readlines()
for i in ReservedID:
    ReservedIdstriped.append(i.rstrip())

IDFile.close()
print(ReservedIdstriped)

DepartmentsFile = open("Departments.cfg" , "r")
Departments = DepartmentsFile.readlines()
for i in Departments:
    DepartmentsStrip.append(i.rstrip())



print(DepartmentsStrip)
AdminFile = open("Admin" , "r")
SecurityData = AdminFile.readlines()
print(SecurityData)
AdminFile.close()
Counter = 2

DatabaseFile = open("Database" , "r")
Context = DatabaseFile.read()
Database = ast.literal_eval(Context)
print(Database)
for i in Database['Anesthetics']['Doctor']:
    DoctorName.append("Dr. " + i["Name"])

DatabaseFile.close()
pygame.mixer.init()


def play():
    pygame.mixer.music.load("audio/ErrorSound.mp3")
    pygame.mixer.music.play(loops=0)

def PopUpMsg(MSG):
    play()
    PopUp = tkinter.Tk()
    PopUp.geometry("+1050+650")
    # PopUp.wm_title("Error")
    MessageLabel = tkinter.Label(PopUp, text = MSG , fg="dodgerblue" , font = "Impact 12")
    MessageLabel.pack(side= "top" , fill= "x" , pady= 10)
    B1 = tkinter.Button(PopUp, text= "OK" , bg ="dimgray" ,fg ="dodgerblue" , command=PopUp.destroy ,width=5 )
    B1.pack()

def Welcome():
    global Label1, Label2, Button1
    Label2.destroy()
    Button1.destroy()
    WelcomeLabel = tkinter.Label(root,text = "\nHospital Management System\n" ,bg = "white", fg = "dodgerblue" ,font = "Impact 24").pack()
    AdminButton  = tkinter.Button(root,text = "Admin Mode" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" , width = "20" , command= AdminMode ).pack()
    FreeLabel    = tkinter.Label(root,text = "\n" ,bg ="white").pack()
    UserButton   = tkinter.Button(root,text = "User Mode" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" , width = "20"  ).pack()


def AdminMode():
    global root , AdminWindow , UserNameEntry , PasswordEntry , FirstLoginLabel ,FirstLoginLabel2 ,UserNameLabel ,PasswordLabel, SaveButton , LoginLabel , EnterButton , SecurityData
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
    global UserNameEntry , PasswordEntry , AdminWindow , SecurityData
    AdminFile = open("Admin","w")
    Username = str(UserNameEntry.get())
    AdminFile.write(Username + "\n")
    AdminFile.write(PasswordEntry.get())
    AdminFile.close()
    AdminFile = open("Admin","r")
    FirstLoginLabel.destroy()
    FirstLoginLabel2.destroy()
    UserNameLabel.destroy()
    PasswordLabel.destroy()
    UserNameEntry.destroy()
    PasswordEntry.destroy()
    SaveButton.destroy()
    SecurityData = AdminFile.readlines()
    AdminFile.close()
    AdminMenuDisplay()

    
def AdminLoginChecker():
    global SecurityData , AdminWindow , Counter ,LoginLabel , EnterButton , TriesLabel
    Username = SecurityData[0]
    if  (UserNameEntry.get() == (SecurityData[0]).rstrip())  and (PasswordEntry.get() == SecurityData[1]):
        print("True")
        # Function to Display Admin Options
        LoginLabel.destroy()
        UserNameLabel.destroy()
        PasswordLabel.destroy()
        UserNameEntry.destroy()
        PasswordEntry.destroy()
        EnterButton.destroy()
        if Counter < 2 :
            TriesLabel.destroy()
        
        AdminMenuDisplay()
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
            if Counter < 2 :
                TriesLabel.destroy()
            TriesLabel = tkinter.Label(AdminWindow , text= "Remaining Tries " + str(Counter)  ,  bg="white" ,fg = "red" , font= "Impact 24" )
            TriesLabel.grid(row = 2 , column= 2)
            Counter-=1


def AdminMenuDisplay():
    global photo , VarList ,Counter , VarList
    Counter = 2
    Label1 = tkinter.Label(AdminWindow,image = photo , width= 800 )
    Label1.pack()
    AdminLabel = tkinter.Label(AdminWindow , text= "Welcome to Admin Mode" , bg= "white" , fg = "red" , font= "Impact 24")
    AdminLabel.pack()
    VarList = tkinter.StringVar(AdminWindow)
    VarList.set("Manage Patients")
    Option = ('Manage Patients' , 'Manage Doctors' , 'Book an Appointment')
    FeatureLabel = tkinter.Label(AdminWindow , text= "Please choose the feature:  " , bg= "white" , fg = "dodgerblue" , font= "Impact 18")
    FeatureLabel.pack(side='left')
    OptionMenu= tkinter.OptionMenu(AdminWindow , VarList , *Option )
    OptionMenu.pack(ipadx = 100 , ipady= 10, side = 'left')
    ConfirmButton = tkinter.Button(AdminWindow , text = "Confirm" , bg= "dimgray" , fg= "dodgerblue" , font = "Impact 18", command= ConfirmFeature)
    ConfirmButton.pack(ipadx = 20 , side = 'left' )
    # ManagePatientsButton = tkinter.Button(AdminWindow , text = "Manage Patients" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" )
    # ManagePatientsButton.pack()
    # ManageDoctorButton   = tkinter.Button(AdminWindow , text = "Manage Doctors" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" )
    # ManageDoctorButton.pack()
    # BookanAppointmentButton = tkinter.Button(AdminWindow , text = "Book an appointment" , bg = "dimgray" , fg = "dodgerblue" , font = "Impact 24" )
    # BookanAppointmentButton.pack()


def ConfirmFeature():
    global OptionMenu
    
    AdminChoice = VarList.get()
    print(AdminChoice)
    if AdminChoice == 'Manage Patients':
        ManagePatients()


def ManagePatients():
    global AdminWindow  , PatientPhoto , PatientsWindow
    PatientsWindow = tkinter.Toplevel(AdminWindow)
    PatientsWindow.geometry("800x600+750+350")
    PatientsWindow.title("Manage Patients")
    PatientsWindow.iconbitmap(r"Icon.ico")
    PatientsWindow.configure(background="white")
    Patient_Pic = Image.open("ManagePatient.jpg")
    resize = Patient_Pic.resize((800,150), Image.ANTIALIAS)
    PatientPhoto = ImageTk.PhotoImage(resize)
    Label1 = tkinter.Label(PatientsWindow,image = PatientPhoto , width= 800 )
    Label1.pack()
    ManagePatientLabel = tkinter.Label(PatientsWindow, text = "Manage Patients\n" ,bg ="White" , fg="red" , font = "Impact 24 ")
    ManagePatientLabel.pack()
    AddButton = tkinter.Button(PatientsWindow , text = "Add Patient" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 , command= AddPatient )
    AddButton.pack()
    FreeLabel = tkinter.Label(PatientsWindow , text = "\n" , bg = "white")
    FreeLabel.pack()
    EditButton = tkinter.Button(PatientsWindow , text = "Edit Patient" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 )
    EditButton.pack()
    FreeLabel = tkinter.Label(PatientsWindow , text = "\n" , bg = "white")
    FreeLabel.pack()
    DelButton = tkinter.Button(PatientsWindow , text = "Delete Patient" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 )
    DelButton.pack()
    FreeLabel = tkinter.Label(PatientsWindow , text = "\n" , bg = "white")
    FreeLabel.pack()
    DisplayButton = tkinter.Button(PatientsWindow , text = "Display a patient" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 )
    DisplayButton.pack()


def AddPatient():
    global AddPatientWindow , PatientsWindow , DoctorVar , DoctorName , DepartmentVar, GenderVar , DoctorMenu , AddPatientWindow , NameEntry , AgeSpinbox , GenderVar , AddressEntry, PhoneEntry, IDSpinBox , RoomSpinBox , DescribeText
    AddPatientWindow = tkinter.Toplevel(PatientsWindow)
    AddPatientWindow.geometry("700x500+800+400")
    AddPatientWindow.title("Add Patient")
    AddPatientWindow.iconbitmap(r"Icon.ico")
    AddPatientWindow.configure(background="white")
    # i = 0
    # while i < 12:
    #     AddPatientWindow.grid_columnconfigure(i,minsize = 10)
    #     AddPatientWindow.grid_rowconfigure(i,minsize = 10)
    #     i+=1
    # AddPatientLabel = tkinter.Label(AddPatientWindow , text = "Add Patient" , bg= "white" , fg= "red" ,font= "Impact 24" )
    # AddPatientLabel.place(relx=0.5 , rely = 0 , anchor= N)
    DepartmentLabel = tkinter.Label(AddPatientWindow , text = "Department: " , bg= "white" , fg = "dodgerblue" , font= "Impact 18")
    DepartmentLabel.place(relx=0.01 , rely = 0.05 , anchor= W)
    DepartmentVar = tkinter.StringVar(AddPatientWindow)
    DepartmentVar.set("Anesthetics")
    DepartmentMenu= tkinter.OptionMenu(AddPatientWindow , DepartmentVar , *DepartmentsStrip )
    DepartmentMenu.place(relx=0.23 , rely = 0.05 , anchor= W , width= 300 , height= 30)
    DoctorLabel = tkinter.Label(AddPatientWindow , text = "Doctor:" , bg = "white" , fg ="dodgerblue" , font = "Impact 18")
    DoctorLabel.place(relx=0.01 , rely=0.15 ,anchor= W  )
    DoctorVar = tkinter.StringVar(AddPatientWindow)
    DoctorVar.set("Press Refresh After Choosing Department")
    DoctorMenu = tkinter.OptionMenu(AddPatientWindow , DoctorVar ,*DoctorName)
    DoctorMenu.place(relx=0.23 , rely = 0.15 , anchor= W , width= 300 , height= 30)
    RefreshButton = tkinter.Button(AddPatientWindow , text="Refresh" , bg="dimgray" ,fg = "dodgerblue" , font = "Impact 12" , command= RefreshDoctor)
    RefreshButton.place(relx=0.75 , rely = 0.15 , anchor= E )
    NameLabel = tkinter.Label(AddPatientWindow ,text = "Patient Name: " , bg = "white" , fg ="dodgerblue" , font = "Impact 18")
    NameLabel.place(relx=0.01 , rely= 0.25 , anchor= W)
    NameEntry = tkinter.Entry(AddPatientWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
    NameEntry.place(relx=0.23 , rely = 0.25 , anchor= W , width= 300 , height= 30)
    AgeLabel = tkinter.Label(AddPatientWindow , text = "Age:" , bg= "White" , fg="dodgerblue" , font= "Impact 18" )
    AgeLabel.place(relx=0.01 , rely = 0.35 , anchor= W)
    AgeSpinbox = tkinter.Spinbox(AddPatientWindow , from_=  1 , to = 150 , bg ="lightgray" , fg= "dodgerblue" , font = "Impact 12")
    AgeSpinbox.place(relx=0.23 , rely= 0.35 , anchor= W , width=300 , height= 30)
    YearsLabel = tkinter.Label(AddPatientWindow , text= "Years" , bg="white" , fg="dodgerblue" , font="Impact 18")        
    YearsLabel.place(relx=0.67 , rely= 0.35 , anchor=W)
    GenderLabel = tkinter.Label(AddPatientWindow , text= "Gender:" ,bg="White" , fg= "dodgerblue" , font= "Impact 18")
    GenderLabel.place(relx=0.01 , rely= 0.45 , anchor=W)
    GenderVar = tkinter.StringVar(AddPatientWindow)
    GenderVar.set("No Gender")
    GenderMaleRadioButton = tkinter.Radiobutton(AddPatientWindow , text= "Male" , variable = GenderVar , value= "Male" ,bg="White" , fg ="dodgerblue" , font = "Impact 12")
    GenderMaleRadioButton.place(relx=0.23 , rely= 0.45 , anchor=W)
    GenderFemaleRadioButton = tkinter.Radiobutton(AddPatientWindow , text= "Female" , variable = GenderVar , value= "Female" ,bg="White" , fg ="dodgerblue" , font = "Impact 12")
    GenderFemaleRadioButton.place(relx=0.43 , rely= 0.45 , anchor=W)
    AddressLabel = tkinter.Label(AddPatientWindow , text = "Address:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    AddressLabel.place(relx = 0.01 , rely=0.55 , anchor= W)
    AddressEntry = tkinter.Entry(AddPatientWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
    AddressEntry.place(relx=0.23 , rely = 0.55 , anchor= W , width= 300 , height= 30)
    PhoneLabel = tkinter.Label(AddPatientWindow , text = "Phone Number:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    PhoneLabel.place(relx=0.01 , rely = 0.65 , anchor= W)
    PhoneEntry = tkinter.Entry(AddPatientWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
    PhoneEntry.place(relx=0.23 , rely = 0.65 , anchor= W , width= 300 , height= 30)
    RoomLabel = tkinter.Label(AddPatientWindow , text = "Room Number:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    RoomLabel.place(relx=0.01 , rely = 0.75 , anchor= W)
    RoomSpinBox = tkinter.Spinbox(AddPatientWindow , from_=  1000 , to = 10000 , bg ="lightgray" , fg= "dodgerblue" , font = "Impact 12")
    RoomSpinBox.place(relx=0.23 , rely = 0.75 , anchor= W , width= 300 , height= 30)
    DescribeLabel = tkinter.Label(AddPatientWindow , text = "Describtion:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    DescribeLabel.place(relx = 0.01 , rely= 0.85 , anchor= W)
    DescribeText = tkinter.Text(AddPatientWindow , bg= "lightgrey"  , font= "Impact 12",fg= "dodgerblue" ,width= 25)
    DescribeText.place(relx=0.23 , rely = 0.85 , anchor= W , width= 300 , height= 30)
    IDLabel = tkinter.Label(AddPatientWindow , text = "ID:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    IDLabel.place(relx=0.01 , rely = 0.95 , anchor= W )
    IDSpinBox = tkinter.Spinbox(AddPatientWindow , from_=  1 , to = 10000 , bg ="lightgray" , fg= "dodgerblue" , font = "Impact 12")
    IDSpinBox.place(relx=0.23 , rely = 0.95 , anchor= W , width= 300 , height= 30)
    PatientEnterButton = tkinter.Button(AddPatientWindow , text= "Enter" , bg ="dimgray" ,fg="dodgerblue" , font = "Impact 18" , command= ReviewPatientData)
    PatientEnterButton.place(relx= 0.8 , rely= 0.9, anchor=W)


def RefreshDoctor():
    global DoctorMenu , AddPatientWindow , DoctorVar
    if 'Doctor' not in Database[DepartmentVar.get()]:
        DoctorName.clear()
        DoctorName.append("There's no available Doctors")
        DoctorMenu.destroy()
        DoctorVar.set("There's no available Doctors")
        DoctorMenu = tkinter.OptionMenu(AddPatientWindow , DoctorVar ,*DoctorName)
        DoctorMenu.place(relx=0.23 , rely = 0.15 , anchor= W , width= 300 , height= 30)
    else:
        DoctorName.clear()
        for i in Database[DepartmentVar.get()]['Doctor']:
            DoctorName.append("Dr. " + i["Name"])
        DoctorMenu.destroy()
        DoctorVar.set(DoctorName[0])
        DoctorMenu = tkinter.OptionMenu(AddPatientWindow , DoctorVar ,*DoctorName)
        DoctorMenu.place(relx=0.23 , rely = 0.15 , anchor= W , width= 300 , height= 30)


def ReviewPatientData():
    global NameEntry , DoctorVar , AgeSpinbox , AddressEntry , GenderVar, PhoneEntry,IDSpinBox,IDFile,RoomSpinBox,DatabaseFile , AddPatientWindow
    # print(AgeSpinbox.get())
    PatientName =""
    PatientName=NameEntry.get()
    PhoneNumber =""
    PhoneNumber=PhoneEntry.get()
    # print(PatientName)
    if DoctorVar.get() == "Press Refresh After Choosing Department" or DoctorVar.get() == "There's no available Doctors" :
        PopUpMsg("Please choose Doctor")
    elif PatientName == "" or PatientName.isspace() or not PatientName.isalpha() :
        PopUpMsg("Please enter correct patient name")
    elif int(AgeSpinbox.get()) > 150 or int(AgeSpinbox.get()) <= 0  :
        PopUpMsg("Please enter correct age")
    elif GenderVar.get() == "No Gender" :
        PopUpMsg("Please enter patient gender")
    elif AddressEntry.get() == "":
        PopUpMsg("Please enter patient address")
    elif  not PhoneNumber.isnumeric() :
        PopUpMsg("Please enter correct phone number")
    elif IDSpinBox.get() in  ReservedIdstriped:
        PopUpMsg("This ID is already exist")
    
    else:
        IDFile = open("Reserved ID" ,"a")
        IDFile.write("\n"+IDSpinBox.get())
        PatientDict["ID"] = IDSpinBox.get()
        PatientDict["Doctor"] = DoctorVar.get()
        PatientDict["Name"] = PatientName
        PatientDict["Age"] = AgeSpinbox.get()
        PatientDict["Gender"] = GenderVar.get()
        PatientDict["Address"] = AddressEntry.get()
        PatientDict["Phone Number"] = PhoneNumber
        PatientDict["Room Number"] = RoomSpinBox.get()
        PatientDict["Describtion"] = DescribeText.get("1.0",END).rstrip()
        DatabaseFile = open("Database" , "w")
        Database[DepartmentVar.get()]['Patients'].append(PatientDict)
        # print(Database)
        DatabaseFile.write(json.dumps(Database))
        AddPatientWindow.destroy()
        PopUpMsg("Patient Data has been saved")
        





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
