from tkinter import*
from turtle import width

def se_ravitailler():
    winddd =Tk()
    winddd.geometry("530x530")
    winddd.title("Se-ravitailler")
    winddd.configure(bg="#37f0bb")

    frame= Frame(winddd, highlightthickness=2, highlightbackground="white",bg='#2a9c50')
    frame.pack(pady=50, ipadx=110, ipady=100)


    myLabelProd = Label(frame,text="Produit", width=15, height=2, bg='#2a9c50' ,font=("Arial", 18, "bold"))
    myEntryProd = Entry(frame, width=30, borderwidth=2)
    
    myLabelQte = Label(frame, text="Quantite", width=15, height=2, bg='#2a9c50', font=("Arial", 18, "bold"))
    myEntryQte = Entry(frame, width=30, borderwidth=2)

    myButtonValid = Button(frame, text="ENREGISTRER",font=("Arial", 23, "bold"))
    
    myLabelProd.grid(row=0, column=0, padx=20, pady=15, ipady=20)
    myEntryProd.grid(row=0, column=1, padx=0, ipady=10, )

    myLabelQte.grid(row=1, column=0, padx=20,pady=5, ipady=20)
    myEntryQte.grid(row=1, column=1, padx=0, ipady=10)
    myButtonValid.grid(row=2, columnspan=2, pady=50, padx=20, ipadx=100, ipady=10)
    
    winddd.mainloop()

def ajout_client():
    winddd1 =Tk()
    winddd1.geometry("500x500")
    winddd1.title("Se-ravitailler")
    winddd1.configure(bg="#36f53f")

    #formulaire d'enregistrement client

    frame =Frame(winddd1, bd=2, bg='red')
    myLabelNomClient = Label(frame,text="Produit" ,width=10)
    myEntryNomClient = Entry(frame,font="solid")

    myLabelPrenomClient = Label(frame, text="Quantite")
    myEntryPrenomClient = Entry(frame,width=40)

    myEmailClient = Label(frame, text="Email")
    myEntryEmailClient = Entry(frame,width=40)

    myLabelNomClient.grid()
    myEntryNomClient.grid()

    myLabelPrenomClient.grid()
    myEntryPrenomClient.grid()

    myEmailClient.grid()
    myEntryEmailClient.grid() 
    
    

def livraison():
    winddd2 =Tk()
    winddd2.geometry("500x500")
    winddd2.title("Se-ravitailler")
    winddd2.configure(bg="#7ef037")

    myLabelProd = Label(winddd2,text="Produit" , width=10)
    myEntryProd = Entry(winddd2,font="solid")
    myLabelQte = Label(winddd2, text="Quantite")
    myEntryQte = Entry(winddd2,width=40)

    myLabelProd.grid()
    myEntryProd.grid()

    myLabelQte.grid()
    myEntryQte.grid() 
    
def historique():
    winddd3 =Tk()
    winddd3.geometry("500x500")
    winddd3.title("Se-ravitailler")
    winddd3.configure(bg="#98d4c3")

    myLabelProd = Label(winddd3,text="Produit" , width=10)
    myEntryProd = Entry(winddd3,font="solid")
    myLabelQte = Label(winddd3, text="Quantite")
    myEntryQte = Entry(winddd3,width=40)
    
    myLabelProd.grid()
    myEntryProd.grid()

    myLabelQte.grid()
    myEntryQte.grid()
    
def produit_stock():
    winddd4 =Tk()
    winddd4.geometry("500x500")
    winddd4.title("Se-ravitailler")
    winddd4.configure(bg="#6ef5c1")

    myLabelProd = Label(winddd4,text="Produit" , width=10)
    myEntryProd = Entry(winddd4,font="solid")
    myLabelQte = Label(winddd4, text="Quantite")
    myEntryQte = Entry(winddd4,width=40)
    
    myLabelProd.grid()
    myEntryProd.grid()

    myLabelQte.grid()
    myEntryQte.grid()
    #6ef5c1
def edit_produit():
    winddd5 =Tk()
    winddd5.geometry("500x500")
    winddd5.title("Se-ravitailler")
    winddd5.configure(bg="#6ef5c1")

    myLabelProd = Label(winddd5,text="Produit" , width=10)
    myEntryProd = Entry(winddd5,font="solid")
    myLabelQte = Label(winddd5, text="Quantite")
    myEntryQte = Entry(winddd5,width=40)
    
    myLabelProd.grid()
    myEntryProd.grid()

    myLabelQte.grid()
    myEntryQte.grid()
    
def edit_client():
    winddd6 =Tk()
    winddd6.geometry("500x500")
    winddd6.title("Se-ravitailler")
    winddd6.configure(bg="#06c27a")

    myLabelProd = Label(winddd6,text="Produit" , width=10)
    myEntryProd = Entry(winddd6,font="solid")
    myLabelQte = Label(winddd6, text="Quantite")
    myEntryQte = Entry(winddd6,width=40)
    
    myLabelProd.grid()
    myEntryProd.grid()

    myLabelQte.grid()
    myEntryQte.grid()

def quiter():
    pass
 



   
