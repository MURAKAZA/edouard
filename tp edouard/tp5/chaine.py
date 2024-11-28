import tkinter as tk
from tkinter import messagebox
#pour les images
from PIL import Image, ImageTk

def validate():
    #afficher les infos saisies
    prenom = entry_prenom.get()
    nom = entry_nom.get()
    ville = entry_ville.get()
    label_result.config(text=f"{prenom} / {nom} / {ville}")

def reset():
    #reinitialiser
    entry_prenom.delete(0, tk.END)
    entry_nom.delete(0, tk.END)
    entry_ville.delete(0, tk.END)
    label_result.config(text="")

#creation de la fenetre
root = tk.Tk()
root.title("Formulaire")

frame = tk.Frame(root)
frame.pack(pady=10)

#prenom
tk.Label(frame, text="Votre prénom :").grid(row=0, column=0, padx=5, pady=5)
entry_prenom = tk.Entry(frame, width=20)
entry_prenom.grid(row=0, column=1, padx=5, pady=5)

#nom
tk.Label(frame, text="Votre nom :").grid(row=1, column=0, padx=5, pady=5)
entry_nom = tk.Entry(frame, width=20)
entry_nom.grid(row=1, column=1, padx=5, pady=5)

#ville
tk.Label(frame, text="Votre ville :").grid(row=2, column=0, padx=5, pady=5)
entry_ville = tk.Entry(frame, width=20)
entry_ville.grid(row=2, column=1, padx=5, pady=5)

#boutons

#valider
btn_validate = tk.Button(frame, text="Valider", command=validate)
btn_validate.grid(row=3, column=0, padx=5, pady=5)

#reinitialiser
btn_reset = tk.Button(frame, text="Réinitialiser", command=reset)
btn_reset.grid(row=3, column=1, padx=5, pady=5)

label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=10)

#quitter
btn_quit = tk.Button(root, text="Quitter", command=root.destroy)
btn_quit.pack(pady=5)

#charger l'image
try:
    image=Image.open("C:/Users/HP/Desktop/tp edouard/tp5/chaine.jpg")
    image=image.resize((150,150))
    print("image chargee")
    photo=ImageTk.PhotoImage(image)
    label_image=tk.Label(root, image=photo)
    label_image.image=photo
    label_image.pack(padx=10, pady=10)
except FileNotFoundError:
    messagebox.showerror("Erreur","L'image 'chaine.jpg' est introuvable.")

#lancer la boucle principale
root.mainloop()