


from tkinter import *
from turtle import left

fenetre = Tk()
fenetre.title('menu gestion')
fenetre.iconbitmap('cow.png')

fenetre.configure(bg='light blue')

def se_ravitailler():
    print("hello!")
    return 
def ajout_client():
    print("hello!")
    return 

def livraison():
    print("hello!")
    return 
def historique():
    print("hello!")
    return 
def edit_produit():
    print("hello!")
    return 
def quiter():
    print("hello!")
    return 
myFrame =Frame(fenetre,bg="orange",borderwidth=10, border=4, width=700, height=600).pack(padx=0, pady=20)

Button(myFrame, bg="gray", text="Se ravitailler", command=se_ravitailler).pack(side="left",padx=10, pady=5)
Button(myFrame, bg="gray", text="Ajout un produit", command=se_ravitailler).pack(side=LEFT,padx=30, pady=5)
Button(myFrame, bg="gray", text="Livraison", command=ajout_client).pack(side=LEFT,padx=10, pady=5)
Button(myFrame, bg="gray", text="Historique", command=livraison ).pack(side=LEFT,padx=20, pady=5)
Button(myFrame, bg="gray", text="Historique", command=historique ).pack(side=LEFT,padx=20, pady=5)
Button(myFrame, bg='gray', text="quiter", ).pack(side=LEFT,padx=10, pady=5)

"""mylabelframe= LabelFrame(width=500, borderwidth=3, height=40).pack(pady=10)"""








fenetre.mainloop()