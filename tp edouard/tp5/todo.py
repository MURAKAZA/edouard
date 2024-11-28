import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrée vide", "Veuillez entrer une tâche avant d'ajouter.")

def mark_complete():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        selected_task = tasks_listbox.get(selected_task_index)
        # Ajouter un indicateur de tâche terminée
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{selected_task} ✅")
    except IndexError:
        messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une tâche à marquer comme terminée.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une tâche à supprimer.")

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("ToDo List")

# Création des widgets
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Ajouter", command=add_task)
complete_button = tk.Button(root, text="Terminer", command=mark_complete)
delete_button = tk.Button(root, text="Supprimer", command=delete_task)
tasks_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)

# Positionnement des widgets
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
add_button.grid(row=0, column=2, padx=10, pady=10)
tasks_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
complete_button.grid(row=2, column=0, padx=10, pady=10)
delete_button.grid(row=2, column=2, padx=10, pady=10)

# Lancement de la boucle principale
root.mainloop()