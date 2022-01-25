from tkinter import*
import main

def se_ravitailler():
    window = Tk()
    window.title("Gestion")
    
    myFrame = Frame(window,bg="gray",borderwidth=10, width=990, height=300 , bd=2, relief="solid")
    myFrame.pack(padx=0, pady=20, fill='both', expand=True)
    myLabelProd = Label(window, text="Produit")
    myEntryProd = Entry(myFrame ,font="solid")
    myLabelQte = Label(myFrame,  text="Quantite")
    myEntryQte = Entry(myFrame, width=40)
    
    myLabelProd.pack()
    myEntryProd.pack()

    myLabelQte.pack()
    myEntryQte.pack()
