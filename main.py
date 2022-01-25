from cProfile import label
from tkinter import *
from turtle import left




fenetre = Tk()
fenetre.title('menu gestion')
fenetre.iconbitmap('cow.png')
fenetre.geometry("1000x500")# taille de de la fenetre
#fenetre.resizable(False, False)#empeche d'agrandir la fenetre

fenetre.configure(bg='light blue')

def se_ravitailler():
    myLabelProd = Label(text="Produit")
    myEntryProd = Entry(font="solid")
    myLabelQte = Label(  text="Quantite")
    myEntryQte = Entry(width=40)
    
    myLabelProd.grid()
    myEntryProd.grid()

    myLabelQte.grid()
    myEntryQte.grid()

    

def ajout_client():
    print("Bienvenue nouveau client!")
    

def livraison():
    print("Effectuer une nouvelle livraison!")
    
def historique():
    print("Votre historique est prêt")
    
def produit_stock():
    print("Produit en stock")
    
def edit_produit():
    print("Edition de produit")
    return
def edit_client():
    print("Edition de client")
    return  
def quiter():
    print("hello!")
 
labelWelcome = Label(fenetre, text="Welcome on my shop store",background="green",fg="white", width=50, height=2, font=("Arial", 33, "bold"))
labelWelcome.grid(row=0, columnspan=10, pady=10)

Button(fenetre,  text="Se-ravitailler", font=("Arial", 15, "bold"),command=se_ravitailler).grid(row=1 ,column=1, padx=10, pady=10)
Button(fenetre,  text="Ajout-client", font=("Arial", 15, "bold"), command=ajout_client).grid(row=1 ,column=2, padx=5, pady=10)
Button(fenetre,  text="Livraison", font=("Arial", 15, "bold"), command=livraison).grid(row=1 ,column=3, padx=5, pady=10)
Button(fenetre,  text="Historique", font=("Arial", 15, "bold"), command=historique).grid(row=1 ,column=4, padx=5)
Button(fenetre,  text="Produit-stock",font=("Arial", 15, "bold"), command=produit_stock).grid(row=1 ,column=5,pady=10,  padx=5)
Button(fenetre,  text="Edit-produit", font=("Arial", 15, "bold"), command=edit_produit).grid(row=1 ,column=6,pady=10, padx=5)
Button(fenetre,  text="Edit-client", font=("Arial", 15, "bold"), command=edit_client).grid(row=1 ,column=7,pady=10, padx=5)
Button(fenetre,  text="quiter",font=("Arial", 15, "bold"), command=fenetre.quit).grid(row=1 ,column=8,pady=10, padx=5)

"""mylabelframe= LabelFrame(width=500, borderwidth=3, height=40).pack(pady=10)"""

myFrame = Frame(fenetre,bg="light green",borderwidth=10, width=990, height=300 , bd=2, relief="solid").grid(row=9,padx=5, pady=20, columnspan=10)

fenetre.mainloop()