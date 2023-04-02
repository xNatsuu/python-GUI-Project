
# GUI program to calculate the Open Circuit and Short Circuit parameters 
from tkinter import *
from tkinter.font import BOLD

Input_window=Tk()

# Assigning the open circuit variables
ocpower=DoubleVar()
ocvolt=DoubleVar()
occurrent=DoubleVar()

# Assigning the short circuit variables
scpower=DoubleVar()
scvolt=DoubleVar()
sccurrent=DoubleVar()

#Assigning input window title to be shown
Input_window.title("Input Data")

# Assigning size of the window
Input_window.geometry("1000x600")

# Icon Image
Input_window.iconbitmap(r"C:\Users\shrim\Downloads\power_energy_bolt_thunderbolt_electricity_icon_191388.ico")

# background Image 
bg2=PhotoImage(file=r"C:\Users\shrim\Downloads\wew.png")
bg=PhotoImage(file=r"C:\Users\shrim\Downloads\teahub.io-light-wallpaper-hd-360584.png")
my_label=Label(Input_window,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)

# Creating a new window
def openNewWindow():
    a=DoubleVar()
    b=DoubleVar()
    Output_window =Toplevel()
# Assigning output window title to be shown
    Output_window.title("Equivalent Circuit parameters Results")

# Assigning size of the window and background image
    Output_window.geometry("1920x1200")
    Output_window.iconbitmap(r"C:\Users\shrim\Downloads\ecoicon05_122077.ico")
    Output_Label=Label(Output_window,image=bg2)
    Output_Label.place(x=0,y=300,relheight=1,relwidth=2)
    Output_Label.pack()
    
    Label(Output_window,text="EQUIVALENT PARAMETERS",font=("Times New Roman",20,BOLD,'underline'),bg="light green").place(x=550,y=0)
  
    #  Main calculation part of the problem
    # Calculation of Open circuit compenent
    # Here a is no load power factor ie cos component of the angle
    a=(ocpower.get())/(ocvolt.get()*occurrent.get())

    # Working component is the Iw current
    workingComponent=(ocpower.get())/(ocvolt.get())

    # Magnetizing component is the Im current
    magnetizingComponent=((occurrent.get())**2-(workingComponent**2))**0.5
    
    

    # Output parameters
    Label(Output_window,text="Core Loss Resistance = %sΩ"%str(coreloss.__round__(3)),font=("Times New Roman",20,BOLD)).place(x=300,y=600)
    Label(Output_window,text="Magnetising Reactance = %sΩ"%str(magnetisingReac.__round__(3)),font=("Times New Roman",20,BOLD)).place(x=300,y=650)
    Label(Output_window,text="Equivalent Resistance = %sΩ"%str(EquivalentResistance.__round__(3)),font=("Times New Roman",20,BOLD)).place(x=300,y=700)
    Label(Output_window,text="Equivalent Reactance = %sΩ"%str(EquivalentReactance.__round__(3)),font=("Times New Roman",20,BOLD)).place(x=800,y=600)
    Label(Output_window,text="Working component current = %sA"%str(workingComponent.__round__(3)),font=("Times New Roman",20,BOLD)).place(x=800,y=650)
    Label(Output_window,text="Magnetizing component current = %sA"%str(magnetizingComponent.__round__(3)),font=("Times New Roman",20,BOLD)).place(x=800,y=700)


   # DIAGRAM

    Label(
        Output_window,
        text="%sΩ" % str(magnetisingReac.__round__(3)),
        font=("Times New Roman", 20, BOLD),
    ).place(x=800, y=250)
    Label(
        Output_window,
        text="%sΩ" % str(coreloss.__round__(3)),
        font=("Times New Roman", 20, BOLD),
    ).place(x=410, y=250)
    Label(
        Output_window,
        text="%sΩ" % str(EquivalentReactance.__round__(3)),
        font=("Times New Roman", 20, BOLD),
    ).place(x=1050, y=140)
    Label(
        Output_window,
        text="%sΩ" % str(EquivalentResistance.__round__(3)),
        font=("Times New Roman", 20, BOLD),
    ).place(x=870, y=105)
    Label(
        Output_window,
        text="%sA" % str(workingComponent.__round__(3)),
        font=("Times New Roman", 20, BOLD),
    ).place(x=590, y=140)
    Label(
        Output_window,
        text="%sA" % str(magnetizingComponent.__round__(3)),
        font=("Times New Roman", 20, BOLD),
    ).place(x=770, y=140)

# Input and text which is to be displayed in the window
Label(Input_window,text="OPEN CIRCUIT TEST",font=("Times New Roman",20,BOLD,'underline'),bg="light blue").place(x=50,y=10)
Label(Input_window,text="Rated Power(W) -",font=("Times New Roman",20),bg="light blue").place(x=30,y=90)
Label(Input_window,text="Rated Voltage(V) -",font=("Times New Roman",20),bg="light blue").place(x=30,y=140)
Label(Input_window,text="Rated Current(A) -",font=("Times New Roman",20),bg="light blue").place(x=30,y=190) 

Entry(Input_window,textvariable=ocpower,font=("Times New Roman",18),width=17,bg="white").place(x=260,y=90)
Entry(Input_window,textvariable=ocvolt,font=("Times New Roman",18),width=17,bg="white").place(x=260,y=140)
Entry(Input_window,textvariable=occurrent,font=("Times New Roman",18),width=17,bg="white").place(x=260,y=190)


Label(Input_window,text="SHORT CIRCUIT TEST",font=("Times New Roman",20,BOLD,'underline'),bg="light yellow").place(x=500,y=10)
Label(Input_window,text="Rated Power(W) -",font=("Times New Roman",20),bg="light yellow").place(x=500,y=90)
Label(Input_window,text="Rated Voltage(V) -",font=("Times New Roman",20),bg="light yellow").place(x=500,y=140)
Label(Input_window,text="Rated Current(A) -",font=("Times New Roman",20),bg="light yellow").place(x=500,y=190)

Entry(Input_window,textvariable=scpower,font=("Times New Roman",18),width=17,bg="white").place(x=730,y=90)
Entry(Input_window,textvariable=scvolt,font=("Times New Roman",18),width=17,bg="white").place(x=730,y=140)
Entry(Input_window,textvariable=sccurrent,font=("Times New Roman",18),width=17,bg="white").place(x=730,y=190)

# Creating is button tab which will give us the result for the input quantites
Button(Input_window,bg="white",text="CALCULATE",font=("Times New Roman",17,BOLD),command=openNewWindow).place(x=380,y=340)

# Execution of the propgram
mainloop()