import tkinter
from tkinter import Text, font
from tkinter.constants import CENTER, DISABLED, E, END, INSERT, N, NE, W
from PIL import ImageTk, Image
import json
import ast
import pygame
from pygame.constants import TEXTINPUT


flag = 0
PatientDict = dict()
DoctorDict = dict()
SecurityData = list()
Departments  = list()
DepartmentsStrip = list()
DoctorName = list()
ReservedID = list()
ReservedIdstriped = list()
DeletedID = list()
DeletedIDstriped = list()

IDFile = open("Reserved ID" , "r")
ReservedID = IDFile.readlines()
for i in ReservedID:
    ReservedIdstriped.append(i.rstrip())

IDFile.close()
print(ReservedIdstriped)


IDFile = open("Deleted ID" , "r")
DeletedID = IDFile.readlines()
for i in DeletedID:
    DeletedIDstriped.append(i.rstrip())

IDFile.close()
print(DeletedIDstriped)

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
    PopUp.title("Alert")
    PopUp.geometry("+1050+650")
    PopUp.iconbitmap(r"Icon.ico")
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
    elif AdminChoice == 'Manage Doctors':
        ManageDoctors()

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
    EditButton = tkinter.Button(PatientsWindow , text = "Edit Patient" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30, command= EditPatient )
    EditButton.pack()
    FreeLabel = tkinter.Label(PatientsWindow , text = "\n" , bg = "white")
    FreeLabel.pack()
    DelButton = tkinter.Button(PatientsWindow , text = "Delete Patient" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 , command= DeletePatient)
    DelButton.pack()
    FreeLabel = tkinter.Label(PatientsWindow , text = "\n" , bg = "white")
    FreeLabel.pack()
    DisplayButton = tkinter.Button(PatientsWindow , text = "Display a patient" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 ,command = ViewPatientData)
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

def EditRefreshDoctor():
    global EditDoctorMenu , AddPatientWindow , EditDoctorVar
    if  not  Database[EditDepartmentVar.get()]['Doctor']:
        DoctorName.clear()
        DoctorName.append("There's no available Doctors")
        EditDoctorMenu.destroy()
        EditDoctorVar.set("There's no available Doctors")
        EditDoctorMenu = tkinter.OptionMenu(EditPatientWindow , EditDoctorVar ,*DoctorName)
        EditDoctorMenu.place(relx=0.23 , rely = 0.15 , anchor= W , width= 300 , height= 30)
    else:
        DoctorName.clear()
        for i in Database[EditDepartmentVar.get()]['Doctor']:
            DoctorName.append("Dr. " + i["Name"])
        EditDoctorMenu.destroy()
        EditDoctorVar.set(DoctorName[0])
        EditDoctorMenu = tkinter.OptionMenu(EditPatientWindow , EditDoctorVar ,*DoctorName)
        EditDoctorMenu.place(relx=0.23 , rely = 0.15 , anchor= W , width= 300 , height= 30)


def ReviewPatientData():
    global DeletedID,DeletedIDstriped ,NameEntry , DoctorVar , AgeSpinbox , AddressEntry , GenderVar, PhoneEntry,IDSpinBox,IDFile,RoomSpinBox,DatabaseFile , AddPatientWindow,DepartmentVar,IDFile,DeletedID,DeletedIDstriped
    # print(AgeSpinbox.get())
    PatientName =""
    PatientName=NameEntry.get()
    PhoneNumber =""
    PhoneNumber=PhoneEntry.get()
    # print(PatientName)

    DatabaseFile = open("Database" , "r")
    Context = DatabaseFile.read()
    Database = ast.literal_eval(Context)
    DatabaseFile.close()

    IDFile = open("Reserved ID" , "r")
    ReservedID = IDFile.readlines()
    for i in ReservedID:
        ReservedIdstriped.append(i.rstrip())
    IDFile.close()

    IDFile = open("Deleted ID" , "r")
    DeletedID = IDFile.readlines()
    for i in DeletedID:
        DeletedIDstriped.append(i.rstrip())

    IDFile.close()

    if DoctorVar.get() == "Press Refresh After Choosing Department" or DoctorVar.get() == "There's no available Doctors" :
        PopUpMsg("Please choose Doctor")
    elif PatientName == "" or PatientName.isspace() or PatientName.isnumeric() :
        PopUpMsg("Please enter correct patient name")
    elif int(AgeSpinbox.get()) > 150 or int(AgeSpinbox.get()) <= 0  :
        PopUpMsg("Please enter correct age")
    elif GenderVar.get() == "No Gender" :
        PopUpMsg("Please enter patient gender")
    elif AddressEntry.get() == "":
        PopUpMsg("Please enter patient address")
    elif  not PhoneNumber.isnumeric() :
        PopUpMsg("Please enter correct phone number")
    elif IDSpinBox.get() in  ReservedIdstriped or IDSpinBox.get() in DeletedIDstriped:
        PopUpMsg("This ID is already exist")
    
    else:
        IDFile = open("Reserved ID" ,"a")
        IDFile.write("\n"+IDSpinBox.get())
        PatientDict["ID"] = IDSpinBox.get()
        PatientDict["Department"] = DepartmentVar.get()
        PatientDict["Supervisor Doctor"] = DoctorVar.get()
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
        DatabaseFile.close()
        AddPatientWindow.destroy()
        PopUpMsg("Patient Data has been saved")
        

def EditPatient():
    global PatientPhoto , IDlabel , IDEntry , NextButton , Label1 , EditPatientWindow 
    EditPatientWindow = tkinter.Toplevel(PatientsWindow)
    EditPatientWindow.geometry("700x500+800+400")
    EditPatientWindow.title("Edit Patient")
    EditPatientWindow.iconbitmap(r"Icon.ico")
    EditPatientWindow.configure(background="white")
    Label1 = tkinter.Label(EditPatientWindow,image = PatientPhoto , width= 800 )
    Label1.place(relx=0.5,anchor=N )
    IDlabel = tkinter.Label(EditPatientWindow , text= "Enter Patient ID" , bg="white" , fg = "dodgerblue" ,font="Impact 18")
    IDlabel.place(relx=0.01,rely=0.5,anchor=W)
    IDEntry = tkinter.Entry(EditPatientWindow , bg="dimgray" , fg="dodgerblue" , font = "Impact 18")
    IDEntry.place(relx=0.3,rely=0.5,anchor=W , width= 300 , height= 30)
    NextButton = tkinter.Button(EditPatientWindow , text = "NEXT" , bg="dimgray" , fg="dodgerblue" , font = "Impact 16", command= EditPatientID)
    NextButton.place(relx= 0.75, rely= 0.5 , anchor=W , width= 100)
    
def EditPatientID():
    global IDlabel , IDEntry , NextButton , Label1 , EditPatientWindow , PatientDict , IDFile,Department , Index ,PatientDataDict , PatientInfoWindow
    global EditNameEntry , EditDoctorVar , EditAgeSpinbox , EditAddressEntry , EditGenderVar, EditPhoneEntry,EditRoomSpinBox,DatabaseFile ,EditPatientWindow,EditDepartmentVar , EditDescribeText , EditDoctorMenu

    IDFile = open("Reserved ID" , "r")
    ReservedID = IDFile.readlines()
    ReservedIdstriped.clear()
    for i in ReservedID:
        ReservedIdstriped.append(i.rstrip())

    IDFile.close()
    # print(ReservedIdstriped)

    if IDEntry.get() not in ReservedIdstriped or IDEntry.get() in DeletedIDstriped :
        PopUpMsg("Invalid Patient ID")

    else:
        flag = 0
        Index = -1
        for i in Database.values():
            if flag == 1:
                break
            Index = -1 
            for n in i['Patients']:
                Index+=1
                print("\n\n")
                if IDEntry.get() == n['ID']:
                    PatientDataDict = n
                    print(PatientDataDict)
                    print(Index)
                    flag = 1
                    break
        
        if flag == 0:
            PopUpMsg("Invalid Patient ID")
        else:
            PatientInfoWindow = tkinter.Tk()
            PatientInfoWindow.geometry("+150+300")
            PatientInfoWindow.iconbitmap(r"Icon.ico")
            PatientInfoWindow.title("Patient Information")
            PatientInfo = tkinter.Label(PatientInfoWindow,text = PatientDataDict ,bg="white" , fg ="red" , font = "Impact 15")
            PatientInfo.pack()
            IDlabel.destroy()
            IDEntry.destroy()
            NextButton.destroy()
            Label1.destroy()
            EditDepartmentLabel = tkinter.Label(EditPatientWindow , text = "Department: " , bg= "white" , fg = "dodgerblue" , font= "Impact 18")
            EditDepartmentLabel.place(relx=0.01 , rely = 0.05 , anchor= W)
            EditDepartmentVar = tkinter.StringVar(EditPatientWindow)
            EditDepartmentVar.set(PatientDataDict['Department'])
            EditDepartmentMenu= tkinter.OptionMenu(EditPatientWindow , EditDepartmentVar , *DepartmentsStrip )
            EditDepartmentMenu.place(relx=0.23 , rely = 0.05 , anchor= W , width= 300 , height= 30)
            EditDoctorLabel = tkinter.Label(EditPatientWindow , text = "Doctor:" , bg = "white" , fg ="dodgerblue" , font = "Impact 18")
            EditDoctorLabel.place(relx=0.01 , rely=0.15 ,anchor= W  )
            EditDoctorVar = tkinter.StringVar(EditPatientWindow)
            EditDoctorVar.set(PatientDataDict['Supervisor Doctor'])
            EditDoctorMenu = tkinter.OptionMenu(EditPatientWindow , EditDoctorVar ,*DoctorName)
            EditDoctorMenu.place(relx=0.23 , rely = 0.15 , anchor= W , width= 300 , height= 30)
            EditRefreshButton = tkinter.Button(EditPatientWindow , text="Refresh" , bg="dimgray" ,fg = "dodgerblue" , font = "Impact 12" , command= EditRefreshDoctor)
            EditRefreshButton.place(relx=0.75 , rely = 0.15 , anchor= E )
            EditNameLabel = tkinter.Label(EditPatientWindow ,text = "Patient Name: " , bg = "white" , fg ="dodgerblue" , font = "Impact 18")
            EditNameLabel.place(relx=0.01 , rely= 0.25 , anchor= W)
            EditNameEntry = tkinter.Entry(EditPatientWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
            EditNameEntry.place(relx=0.23 , rely = 0.25 , anchor= W , width= 300 , height= 30)
            EditAgeLabel = tkinter.Label(EditPatientWindow , text = "Age:" , bg= "White" , fg="dodgerblue" , font= "Impact 18" )
            EditAgeLabel.place(relx=0.01 , rely = 0.35 , anchor= W)
            EditAgeSpinbox = tkinter.Spinbox(EditPatientWindow , from_=  1 , to = 150 , bg ="lightgray" , fg= "dodgerblue" , font = "Impact 12")
            EditAgeSpinbox.place(relx=0.23 , rely= 0.35 , anchor= W , width=300 , height= 30)
            EditYearsLabel = tkinter.Label(EditPatientWindow , text= "Years" , bg="white" , fg="dodgerblue" , font="Impact 18")        
            EditYearsLabel.place(relx=0.67 , rely= 0.35 , anchor=W)
            EditGenderLabel = tkinter.Label(EditPatientWindow , text= "Gender:" ,bg="White" , fg= "dodgerblue" , font= "Impact 18")
            EditGenderLabel.place(relx=0.01 , rely= 0.45 , anchor=W)
            EditGenderVar = tkinter.StringVar(EditPatientWindow)
            EditGenderVar.set(PatientDataDict['Gender'])
            EditGenderMaleRadioButton = tkinter.Radiobutton(EditPatientWindow , text= "Male" , variable = EditGenderVar , value= "Male" ,bg="White" , fg ="dodgerblue" , font = "Impact 12")
            EditGenderMaleRadioButton.place(relx=0.23 , rely= 0.45 , anchor=W)
            EditGenderFemaleRadioButton = tkinter.Radiobutton(EditPatientWindow , text= "Female" , variable = EditGenderVar , value= "Female" ,bg="White" , fg ="dodgerblue" , font = "Impact 12")
            EditGenderFemaleRadioButton.place(relx=0.43 , rely= 0.45 , anchor=W)
            EditAddressLabel = tkinter.Label(EditPatientWindow , text = "Address:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
            EditAddressLabel.place(relx = 0.01 , rely=0.55 , anchor= W)
            EditAddressEntry = tkinter.Entry(EditPatientWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
            EditAddressEntry.place(relx=0.23 , rely = 0.55 , anchor= W , width= 300 , height= 30)
            EditPhoneLabel = tkinter.Label(EditPatientWindow , text = "Phone Number:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
            EditPhoneLabel.place(relx=0.01 , rely = 0.65 , anchor= W)
            EditPhoneEntry = tkinter.Entry(EditPatientWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
            EditPhoneEntry.place(relx=0.23 , rely = 0.65 , anchor= W , width= 300 , height= 30)
            EditRoomLabel = tkinter.Label(EditPatientWindow , text = "Room Number:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
            EditRoomLabel.place(relx=0.01 , rely = 0.75 , anchor= W)
            EditRoomSpinBox = tkinter.Spinbox(EditPatientWindow , from_=  1000 , to = 10000 , bg ="lightgray" , fg= "dodgerblue" , font = "Impact 12")
            EditRoomSpinBox.place(relx=0.23 , rely = 0.75 , anchor= W , width= 300 , height= 30)
            EditDescribeLabel = tkinter.Label(EditPatientWindow , text = "Describtion:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
            EditDescribeLabel.place(relx = 0.01 , rely= 0.85 , anchor= W)
            EditDescribeText = tkinter.Text(EditPatientWindow , bg= "lightgrey"  , font= "Impact 12",fg= "dodgerblue" ,width= 25)
            EditDescribeText.place(relx=0.23 , rely = 0.85 , anchor= W , width= 300 , height= 30)
            EditPatientEnterButton = tkinter.Button(EditPatientWindow , text= "Enter" , bg ="dimgray" ,fg="dodgerblue" , font = "Impact 18" , command= EditPatientData)
            EditPatientEnterButton.place(relx= 0.8 , rely= 0.9, anchor=W)

def EditPatientData():
    global EditNameEntry , EditDoctorVar , EditAgeSpinbox , EditAddressEntry , EditGenderVar, EditPhoneEntry,EditRoomSpinBox,DatabaseFile ,EditPatientWindow,EditDepartmentVar ,EditDescribeText ,Index , PatientInfoWindow

    PatientName = ""
    PatientName=EditNameEntry.get()
    PhoneNumber = ""
    PhoneNumber=EditPhoneEntry.get()

    if EditDoctorVar.get() == "Press Refresh After Choosing Department" or EditDoctorVar.get() == "There's no available Doctors" :
        PopUpMsg("Please choose Doctor")
    elif PatientName == "" or PatientName.isspace() or  PatientName.isnumeric():
        PopUpMsg("Please enter correct patient name")
    elif int(EditAgeSpinbox.get()) > 150 or int(EditAgeSpinbox.get()) <= 0  :
        PopUpMsg("Please enter correct age")
    elif EditGenderVar.get() == "No Gender" :
        PopUpMsg("Please enter patient gender")
    elif EditAddressEntry.get() == "":
        PopUpMsg("Please enter patient address")
    elif  not PhoneNumber.isnumeric() :
        PopUpMsg("Please enter correct phone number")
    
    else:
        PatientDict["ID"] = PatientDataDict['ID']
        PatientDict["Department"] = EditDepartmentVar.get()
        PatientDict["Supervisor Doctor"] = EditDoctorVar.get()
        PatientDict["Name"] = PatientName
        PatientDict["Age"] = EditAgeSpinbox.get()
        PatientDict["Gender"] = EditGenderVar.get()
        PatientDict["Address"] = EditAddressEntry.get()
        PatientDict["Phone Number"] = PhoneNumber
        PatientDict["Room Number"] = EditRoomSpinBox.get()
        PatientDict["Describtion"] = EditDescribeText.get("1.0",END).rstrip()
        DatabaseFile = open("Database" , "w")
        Database[EditDepartmentVar.get()]['Patients'].append(PatientDict)
        Database[PatientDataDict['Department']]['Patients'].pop(Index)
        # print(Database)
        DatabaseFile.write(json.dumps(Database))
        EditPatientWindow.destroy()
        PatientInfoWindow.destroy()
        PopUpMsg("Patient Data has been saved")
        
def DeletePatient():
    global DelIDEntry ,DelPatientWindow
    DelPatientWindow = tkinter.Toplevel(PatientsWindow)
    DelPatientWindow.geometry("700x500+800+400")
    DelPatientWindow.title("Edit Patient")
    DelPatientWindow.iconbitmap(r"Icon.ico")
    DelPatientWindow.configure(background="white")
    Label1 = tkinter.Label(DelPatientWindow,image = PatientPhoto , width= 800 )
    Label1.place(relx=0.5,anchor=N )
    IDlabel = tkinter.Label(DelPatientWindow , text= "Enter Patient ID" , bg="white" , fg = "dodgerblue" ,font="Impact 18")
    IDlabel.place(relx=0.01,rely=0.5,anchor=W)
    DelIDEntry = tkinter.Entry(DelPatientWindow , bg="dimgray" , fg="dodgerblue" , font = "Impact 18")
    DelIDEntry.place(relx=0.3,rely=0.5,anchor=W , width= 300 , height= 30)
    NextButton = tkinter.Button(DelPatientWindow , text = "Confirm" , bg="dimgray" , fg="dodgerblue" , font = "Impact 16", command= DelPatientDict)
    NextButton.place(relx= 0.75, rely= 0.5 , anchor=W , width= 100)


def DelPatientDict():
    global IDFile,ReservedID,ReservedIdstriped,DelIDEntry,flag,Index,Database,Key,DatabaseFile ,DelPatientWindow,DeletedID,DeletedIDstriped
    Key = ""
    IDFile = open("Reserved ID" , "r")
    ReservedID = IDFile.readlines()
    ReservedIdstriped.clear()
    for i in ReservedID:
        ReservedIdstriped.append(i.rstrip())

    IDFile.close()

    IDFile = open("Deleted ID" , "r")
    DeletedID = IDFile.readlines()
    for i in DeletedID:
        DeletedIDstriped.append(i.rstrip())

    IDFile.close()

    if DelIDEntry.get() not in ReservedIdstriped or DelIDEntry.get() in DeletedIDstriped :
        PopUpMsg("Invalid Patient ID")

    else:
        flag = 0
        Index = -1
        for i in Database.values():
            if flag == 1:
                break
            for n in i['Patients']:
                Index+=1
                print("\n\n")
                if DelIDEntry.get() == n['ID']:
                    flag = 1
                    Key = n['Department']
                    print(Key)
                    break

        Database[Key]['Patients'].pop(Index)               
        ReservedIdstriped.remove(DelIDEntry.get())
        IDFile = open("Reserved ID" , "w")
        for i in ReservedIdstriped:
            IDFile.write(i+"\n")
        IDFile.close()
        IDFile = open("Deleted ID","a")
        IDFile.write("\n" + DelIDEntry.get())
        IDFile.close()
        DatabaseFile = open("Database" , "w")
        DatabaseFile.write(json.dumps(Database))
        DatabaseFile.close()
        DelPatientWindow.destroy()
        PopUpMsg("Patient has been successfully deleted")

def ViewPatientData():
    global ViewIDEntry,ViewPatientWindow
    ViewPatientWindow = tkinter.Toplevel(PatientsWindow)
    ViewPatientWindow.geometry("700x500+800+400")
    ViewPatientWindow.title("Edit Patient")
    ViewPatientWindow.iconbitmap(r"Icon.ico")
    ViewPatientWindow.configure(background="white")
    Label1 = tkinter.Label(ViewPatientWindow,image = PatientPhoto , width= 800 )
    Label1.place(relx=0.5,anchor=N )
    ViewIDlabel = tkinter.Label(ViewPatientWindow , text= "Enter Patient ID" , bg="white" , fg = "dodgerblue" ,font="Impact 18")
    ViewIDlabel.place(relx=0.01,rely=0.5,anchor=W)
    ViewIDEntry = tkinter.Entry(ViewPatientWindow , bg="dimgray" , fg="dodgerblue" , font = "Impact 18")
    ViewIDEntry.place(relx=0.3,rely=0.5,anchor=W , width= 300 , height= 30)
    ViewNextButton = tkinter.Button(ViewPatientWindow , text = "NEXT" , bg="dimgray" , fg="dodgerblue" , font = "Impact 16", command= PatientData)
    ViewNextButton.place(relx= 0.75, rely= 0.5 , anchor=W , width= 100)
    ViewAllPatientButton = tkinter.Button(ViewPatientWindow , text="View All Patient" , bg ="dimgray" ,fg="dodgerblue" ,font = "impact 16", command = ViewAllPatientData)
    ViewAllPatientButton.place(relx = 0.3 , rely= 0.8 , anchor= W , width= 300 )


def ViewAllPatientData():
    global ViewPatientWindow
    ViewPatientWindow.destroy()    
    PatientInfoWindow = tkinter.Tk()
    PatientInfoWindow.geometry("+150+290")
    PatientInfoWindow.iconbitmap(r"Icon.ico")
    PatientInfoWindow.title("Patient Information")
    flag = 0
    for i in Database.values():
        for n in i['Patients']:
            PatientDataDict = n
            PatientInfo = tkinter.Label(PatientInfoWindow,text = PatientDataDict ,bg="white" , fg ="red" , font = "Impact 15")
            PatientInfo.pack(pady=10)
  

def PatientData():
    global IDFile , ReservedID , ReservedIdstriped ,ViewIDEntry,ViewPatientWindow
    IDFile = open("Reserved ID" , "r")
    ReservedID = IDFile.readlines()
    ReservedIdstriped.clear()
    for i in ReservedID:
        ReservedIdstriped.append(i.rstrip())

    IDFile.close()
    # print(ReservedIdstriped)

    if ViewIDEntry.get() not in ReservedIdstriped or ViewIDEntry.get() in DeletedIDstriped :
        PopUpMsg("Invalid Patient ID")

    else:
        PatientInfoWindow = tkinter.Tk()
        PatientInfoWindow.geometry("+150+290")
        PatientInfoWindow.iconbitmap(r"Icon.ico")
        PatientInfoWindow.title("Patient Information")
        flag = 0
        Index = -1
        for i in Database.values():
            if flag == 1:
                break
            for n in i['Patients']:
                Index+=1
                if ViewIDEntry.get() == n['ID']:
                    PatientDataDict = n
                    print(PatientDataDict)
                    flag = 1
                    break

        PatientInfo = tkinter.Label(PatientInfoWindow,text = PatientDataDict ,bg="white" , fg ="red" , font = "Impact 15")
        PatientInfo.pack()
        ViewPatientWindow.destroy()           






def ManageDoctors():
    global AdminWindow  , DoctorPhoto , DoctorWindow 
    
    DoctorWindow = tkinter.Toplevel(AdminWindow)
    DoctorWindow.geometry("800x600+750+350")
    DoctorWindow.title("Manage Doctors")
    DoctorWindow.iconbitmap(r"Icon.ico")
    DoctorWindow.configure(background="white")
    Doctor_Pic = Image.open("ManageDoctor.jpg")
    resize = Doctor_Pic.resize((800,150), Image.ANTIALIAS)
    DoctorPhoto = ImageTk.PhotoImage(resize)
    Label1 = tkinter.Label(DoctorWindow,image = DoctorPhoto , width= 800 )
    Label1.pack()
    ManageDoctorLabel = tkinter.Label(DoctorWindow, text = "Manage Doctors\n" ,bg ="White" , fg="red" , font = "Impact 24 ")
    ManageDoctorLabel.pack()
    DoctorAddButton = tkinter.Button(DoctorWindow , text = "Add Doctor" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 , command= AddDoctor )
    DoctorAddButton.pack()
    DoctorFreeLabel = tkinter.Label(DoctorWindow , text = "\n" , bg = "white")
    DoctorFreeLabel.pack()
    DoctorEditButton = tkinter.Button(DoctorWindow , text = "Edit Doctor" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30, command= EditDoctor )
    DoctorEditButton.pack()
    DoctorFreeLabel = tkinter.Label(DoctorWindow , text = "\n" , bg = "white")
    DoctorFreeLabel.pack()
    DoctorDelButton = tkinter.Button(DoctorWindow , text = "Delete Doctor" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 , command= DeletePatient)
    DoctorDelButton.pack()
    DoctorFreeLabel = tkinter.Label(DoctorWindow , text = "\n" , bg = "white")
    DoctorFreeLabel.pack()
    DoctorDisplayButton = tkinter.Button(DoctorWindow , text = "Display Doctor Inforamtion" , bg = "dimgray" , fg = "dodgerblue" , font= "Impact 18" ,width= 30 ,command = ViewPatientData)
    DoctorDisplayButton.pack()


def AddDoctor():
    global AddDoctorWindow , DoctorWindow  , DoctorDepartmentVar , DoctorNameEntry , DoctorAddressEntry, DoctorPhoneEntry, DoctorIDSpinBox ,DoctorPhoto
    AddDoctorWindow = tkinter.Toplevel(DoctorWindow)
    AddDoctorWindow.geometry("700x500+800+400")
    AddDoctorWindow.title("Add Doctor")
    AddDoctorWindow.iconbitmap(r"Icon.ico")
    AddDoctorWindow.configure(background="white")

    Label1 = tkinter.Label(AddDoctorWindow,image = DoctorPhoto , width= 800 )
    Label1.place(relx=0.5,anchor=N)
    DepartmentLabel = tkinter.Label(AddDoctorWindow , text = "Department: " , bg= "white" , fg = "dodgerblue" , font= "Impact 18")
    DepartmentLabel.place(relx=0.01 , rely = 0.4 , anchor= W)
    DoctorDepartmentVar = tkinter.StringVar(AddDoctorWindow)
    DoctorDepartmentVar.set("Anesthetics")
    DepartmentMenu= tkinter.OptionMenu(AddDoctorWindow , DoctorDepartmentVar , *DepartmentsStrip )
    DepartmentMenu.place(relx=0.23 , rely = 0.4 , anchor= W , width= 300 , height= 30)
    DoctorNameLabel = tkinter.Label(AddDoctorWindow ,text = "Doctor Name: " , bg = "white" , fg ="dodgerblue" , font = "Impact 18")
    DoctorNameLabel.place(relx=0.01 , rely= 0.5 , anchor= W)
    DoctorNameEntry = tkinter.Entry(AddDoctorWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
    DoctorNameEntry.place(relx=0.23 , rely = 0.5 , anchor= W , width= 300 , height= 30)
    DoctorAddressLabel = tkinter.Label(AddDoctorWindow , text = "Address:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    DoctorAddressLabel.place(relx = 0.01 , rely=0.6 , anchor= W)
    DoctorAddressEntry = tkinter.Entry(AddDoctorWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
    DoctorAddressEntry.place(relx=0.23 , rely = 0.6 , anchor= W , width= 300 , height= 30)
    DoctorPhoneLabel = tkinter.Label(AddDoctorWindow , text = "Phone Number:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    DoctorPhoneLabel.place(relx=0.01 , rely = 0.7 , anchor= W)
    DoctorPhoneEntry = tkinter.Entry(AddDoctorWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
    DoctorPhoneEntry.place(relx=0.23 , rely = 0.7 , anchor= W , width= 300 , height= 30)
    IDLabel = tkinter.Label(AddDoctorWindow , text = "ID:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
    IDLabel.place(relx=0.01 , rely = 0.8 , anchor= W )
    DoctorIDSpinBox = tkinter.Spinbox(AddDoctorWindow , from_=  1 , to = 10000 , bg ="lightgray" , fg= "dodgerblue" , font = "Impact 12")
    DoctorIDSpinBox.place(relx=0.23 , rely = 0.8 , anchor= W , width= 300 , height= 30)
    PatientEnterButton = tkinter.Button(AddDoctorWindow , text= "Enter" , bg ="dimgray" ,fg="dodgerblue" , font = "Impact 18" , command= ReviewDoctorData)
    PatientEnterButton.place(relx= 0.8 , rely= 0.9, anchor=W)


def ReviewDoctorData():
    global DeletedID ,DoctorNameEntry  , DoctorAddressEntry , DoctorPhoneEntry,DoctorIDSpinBox,IDFile,DatabaseFile ,AddDoctorWindow ,DoctorDepartmentVar,IDFile,DeletedID,DeletedIDstriped
    # print(AgeSpinbox.get())
    DoctorName =""
    DoctorName=DoctorNameEntry.get()
    PhoneNumber =""
    PhoneNumber=DoctorPhoneEntry.get()
    # print(PatientName)


    DatabaseFile = open("Database" , "r")
    Context = DatabaseFile.read()
    Database = ast.literal_eval(Context)
    DatabaseFile.close()

    IDFile = open("Reserved ID" , "r")
    ReservedID = IDFile.readlines()
    for i in ReservedID:
        ReservedIdstriped.append(i.rstrip())
    IDFile.close()

    IDFile = open("Deleted ID" , "r")
    DeletedID = IDFile.readlines()
    for i in DeletedID:
        DeletedIDstriped.append(i.rstrip())

    IDFile.close()

    if DoctorName == "" or DoctorName.isspace() or DoctorName.isnumeric() :
        PopUpMsg("Please enter correct patient name")
    elif DoctorAddressEntry.get() == "":
        PopUpMsg("Please enter patient address")
    elif  not PhoneNumber.isnumeric() :
        PopUpMsg("Please enter correct phone number")
    elif DoctorIDSpinBox.get() in  ReservedIdstriped or DoctorIDSpinBox.get() in DeletedIDstriped:
        PopUpMsg("This ID is already exist")
    
    else:
        if  DoctorDict:
            DoctorDict.clear()

        IDFile = open("Reserved ID" ,"a")
        IDFile.write("\n"+DoctorIDSpinBox.get())
        IDFile.close()
        DoctorDict["ID"] = DoctorIDSpinBox.get()
        DoctorDict["Department"] = DoctorDepartmentVar.get()
        DoctorDict["Name"] = DoctorName
        DoctorDict["Address"] = DoctorAddressEntry.get()
        DoctorDict["Phone Number"] = PhoneNumber
        DatabaseFile = open("Database" , "w")
        Database[DoctorDepartmentVar.get()]['Doctor'].append(DoctorDict)
        print(Database)
        DatabaseFile.write(json.dumps(Database))
        DatabaseFile.close()
        AddDoctorWindow.destroy()
        PopUpMsg("Doctor Data has been saved")


def EditDoctor():
    global DoctorPhoto , DoctorIDlabel , DoctorIDEntry , DoctorNextButton , DoctorLabel1 , EditDoctorWindow ,DoctorWindow
    EditDoctorWindow = tkinter.Toplevel(DoctorWindow)
    EditDoctorWindow.geometry("700x500+800+400")
    EditDoctorWindow.title("Edit Doctor")
    EditDoctorWindow.iconbitmap(r"Icon.ico")
    EditDoctorWindow.configure(background="white")
    DoctorLabel1 = tkinter.Label(EditDoctorWindow,image = DoctorPhoto , width= 800 )
    DoctorLabel1.place(relx=0.5,anchor=N )
    DoctorIDlabel = tkinter.Label(EditDoctorWindow , text= "Enter Doctor ID" , bg="white" , fg = "dodgerblue" ,font="Impact 18")
    DoctorIDlabel.place(relx=0.01,rely=0.5,anchor=W)
    DoctorIDEntry = tkinter.Entry(EditDoctorWindow , bg="dimgray" , fg="dodgerblue" , font = "Impact 18")
    DoctorIDEntry.place(relx=0.3,rely=0.5,anchor=W , width= 300 , height= 30)
    DoctorNextButton = tkinter.Button(EditDoctorWindow , text = "NEXT" , bg="dimgray" , fg="dodgerblue" , font = "Impact 16", command= EditDoctorID)
    DoctorNextButton.place(relx= 0.75, rely= 0.5 , anchor=W , width= 100)


def EditDoctorID():
    global  DoctorWindow  , EditDoctorDepartmentVar , EditDoctorNameEntry , EditDoctorAddressEntry, EditDoctorPhoneEntry, EditDoctorIDSpinBox ,DoctorPhoto
    global DoctorPhoto , DoctorIDlabel , DoctorIDEntry , DoctorNextButton , DoctorLabel1 , EditDoctorWindow ,DoctorDataDict , DoctorInfoWindow, DoctorIndex

    IDFile = open("Reserved ID" , "r")
    ReservedID = IDFile.readlines()
    ReservedIdstriped.clear()
    for i in ReservedID:
        ReservedIdstriped.append(i.rstrip())

    IDFile.close()
    # print(ReservedIdstriped)
    if DoctorIDEntry.get() not in ReservedIdstriped or DoctorIDEntry.get() in DeletedIDstriped :
        PopUpMsg("Invalid Doctor ID")
    else:
        flag = 0
        DoctorIndex = -1
        for i in Database.values():
            if flag == 1:
                break
            DoctorIndex = -1
            for n in i['Doctor']:
                DoctorIndex+=1
                print("\n\n")
                if DoctorIDEntry.get() == n['ID']:
                    DoctorDataDict = n
                    print(DoctorDataDict)
                    print(DoctorIndex)
                    flag = 1
                    break
        
        if(flag == 0):
            PopUpMsg("Invalid Doctor ID")
        else:
            DoctorInfoWindow = tkinter.Tk()
            DoctorInfoWindow.geometry("+150+300")
            DoctorInfoWindow.iconbitmap(r"Icon.ico")
            DoctorInfoWindow.title("Doctor Information")
            PatientInfo = tkinter.Label(DoctorInfoWindow,text = DoctorDataDict ,bg="white" , fg ="red" , font = "Impact 15")
            PatientInfo.pack()


            DoctorIDlabel.destroy()
            DoctorIDEntry.destroy()
            DoctorNextButton.destroy()
            
            DepartmentLabel = tkinter.Label(EditDoctorWindow , text = "Department: " , bg= "white" , fg = "dodgerblue" , font= "Impact 18")
            DepartmentLabel.place(relx=0.01 , rely = 0.4 , anchor= W)
            EditDoctorDepartmentVar = tkinter.StringVar(EditDoctorWindow)
            EditDoctorDepartmentVar.set(DoctorDataDict["Department"])
            DepartmentMenu= tkinter.OptionMenu(EditDoctorWindow , EditDoctorDepartmentVar , *DepartmentsStrip )
            DepartmentMenu.place(relx=0.23 , rely = 0.4 , anchor= W , width= 300 , height= 30)
            DoctorNameLabel = tkinter.Label(EditDoctorWindow ,text = "Doctor Name: " , bg = "white" , fg ="dodgerblue" , font = "Impact 18")
            DoctorNameLabel.place(relx=0.01 , rely= 0.5 , anchor= W)
            EditDoctorNameEntry = tkinter.Entry(EditDoctorWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
            EditDoctorNameEntry.place(relx=0.23 , rely = 0.5 , anchor= W , width= 300 , height= 30)
            DoctorAddressLabel = tkinter.Label(EditDoctorWindow , text = "Address:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
            DoctorAddressLabel.place(relx = 0.01 , rely=0.6 , anchor= W)
            EditDoctorAddressEntry = tkinter.Entry(EditDoctorWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
            EditDoctorAddressEntry.place(relx=0.23 , rely = 0.6 , anchor= W , width= 300 , height= 30)
            DoctorPhoneLabel = tkinter.Label(EditDoctorWindow , text = "Phone Number:" , bg = "White" , fg = "dodgerblue" , font= "Impact 18")
            DoctorPhoneLabel.place(relx=0.01 , rely = 0.7 , anchor= W)
            EditDoctorPhoneEntry = tkinter.Entry(EditDoctorWindow , bg= "lightgrey"  , font= "Impact 18",fg= "dodgerblue" ,width= 25 )
            EditDoctorPhoneEntry.place(relx=0.23 , rely = 0.7 , anchor= W , width= 300 , height= 30)
            PatientEnterButton = tkinter.Button(EditDoctorWindow , text= "Enter" , bg ="dimgray" ,fg="dodgerblue" , font = "Impact 18" , command= EditDoctorData)
            PatientEnterButton.place(relx= 0.8 , rely= 0.9, anchor=W)



def EditDoctorData():
    global DoctorIndex , DoctorDataDict, DoctorInfoWindow , DoctorDict , DeletedID,DeletedIDstriped ,EditDoctorNameEntry  , EditDoctorAddressEntry , EditDoctorPhoneEntry,EditDoctorIDSpinBox,IDFile,DatabaseFile ,AddDoctorWindow ,EditDoctorDepartmentVar,IDFile,DeletedID,DeletedIDstriped
    # print(AgeSpinbox.get())
    DoctorName =""
    DoctorName=EditDoctorNameEntry.get()
    PhoneNumber =""
    PhoneNumber=EditDoctorPhoneEntry.get()
    # print(PatientName)

    IDFile = open("Deleted ID" , "r")
    DeletedID = IDFile.readlines()
    for i in DeletedID:
        DeletedIDstriped.append(i.rstrip())

    IDFile = open("Deleted ID" , "r")
    DeletedID = IDFile.readlines()
    for i in DeletedID:
        DeletedIDstriped.append(i.rstrip())

    IDFile.close()

    if DoctorName == "" or DoctorName.isspace() or DoctorName.isnumeric() :
        PopUpMsg("Please enter correct patient name")
    elif EditDoctorAddressEntry.get() == "":
        PopUpMsg("Please enter patient address")
    elif  not PhoneNumber.isnumeric() :
        PopUpMsg("Please enter correct phone number")

    
    else:
        DoctorDict["ID"] = DoctorDataDict['ID']
        DoctorDict["Department"] = EditDoctorDepartmentVar.get()
        DoctorDict["Name"] = DoctorName
        DoctorDict["Address"] = EditDoctorAddressEntry.get()
        DoctorDict["Phone Number"] = PhoneNumber
        DatabaseFile = open("Database" , "w")
        Database[EditDoctorDepartmentVar.get()]['Doctor'].append(DoctorDict)
        Database[DoctorDataDict['Department']]['Doctor'].pop(DoctorIndex)
        # print(Database)
        DatabaseFile.write(json.dumps(Database))
        EditDoctorWindow.destroy()
        DoctorInfoWindow.destroy()
        PopUpMsg("Doctor Data has been saved")
        


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
