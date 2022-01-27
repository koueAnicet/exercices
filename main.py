from tkinter import *
from turtle import left
from PIL import ImageTk,Image
import fonctions

fenetre = Tk()
fenetre.title('menu gestion')
fenetre.iconbitmap('/Users/imac-05/Desktop/test/cow.png')
fenetre.geometry("2000x2000")# taille de de la fenetre
#fenetre.resizable(False, False)#empeche d'agrandir la fenetre
fenetre.configure(bg='light blue')


labelWelcome = Label(fenetre, text="BIENVENUE SUR MA BOUTIQUE EN LIGNE",background="green",fg="white", width=100, height=2, font=("Arial", 33, "bold"))
labelWelcome.grid(row=0, columnspan=10, padx=35, pady=10)

Button(fenetre,  text="Se-ravitailler", font=("Arial", 15, "bold", ),command=fonctions.se_ravitailler).grid(row=1 ,column=1, padx=10, pady=10)
Button(fenetre,  text="Ajout-client", font=("Arial", 15, "bold"), command=fonctions.ajout_client).grid(row=1 ,column=2, padx=5, pady=10)
Button(fenetre,  text="Livraison", font=("Arial", 15, "bold"), command=fonctions.livraison).grid(row=1 ,column=3, padx=5, pady=10)
Button(fenetre,  text="Historique", font=("Arial", 15, "bold"), command=fonctions.historique).grid(row=1 ,column=4, padx=5)
Button(fenetre,  text="Produit-stock",font=("Arial", 15, "bold"), command=fonctions.produit_stock).grid(row=1 ,column=5,pady=10,  padx=5)
Button(fenetre,  text="Edit-produit", font=("Arial", 15, "bold"), command=fonctions.edit_produit).grid(row=1 ,column=6,pady=10, padx=5)
Button(fenetre,  text="Edit-client", font=("Arial", 15, "bold"), command=fonctions.edit_client).grid(row=1 ,column=7,pady=10, padx=5)
Button(fenetre,  text="quiter",font=("Arial", 15, "bold"), command=fenetre.quit).grid(row=1 ,column=8,pady=10, padx=5)



"""mylabelframe= LabelFrame(width=500, borderwidth=3, height=40).pack(pady=10)"""

myFrame = Frame(fenetre, bg="light green",borderwidth=10, width=1900, height=890 , bd=2, relief="solid").grid(row=9,padx=5, pady=20, columnspan=10)

fenetre.mainloop()