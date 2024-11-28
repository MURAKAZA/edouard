from datetime import datetime

class Note:
    """Représente une note avec un mémo, des balises, une date de création et un identifiant unique."""
    last_id = 0

    def __init__(self, memo, tags=""):
        """Initialise une note avec un mémo, des balises et une date de création."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.now()
        Note.last_id += 1
        self.id = Note.last_id

    def match(self, search_term):
        """Retourne True si le mémo ou les balises contiennent la chaîne `search_term`."""
        return search_term.lower() in self.memo.lower() or search_term.lower() in self.tags.lower()


class Notebook:
    """Un conteneur pour gérer un ensemble de notes."""

    def __init__(self):
        """Initialise un carnet vide."""
        self.notes = []

    def add_note(self, memo, tags=""):
        """Ajoute une nouvelle note au carnet."""
        self.notes.append(Note(memo, tags))

    def find_note_by_id(self, note_id):
        """Recherche une note par son identifiant unique."""
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_note(self, note_id, new_memo=None, new_tags=None):
        """Modifie le mémo et/ou les balises d'une note spécifique."""
        note = self.find_note_by_id(note_id)
        if note:
            if new_memo:
                note.memo = new_memo
            if new_tags:
                note.tags = new_tags
            return True
        return False

    def search_notes(self, search_term):
        """Recherche toutes les notes correspondant au terme donné."""
        return [note for note in self.notes if note.match(search_term)]

class Menu:
    """Menu pour interagir avec le carnet via la ligne de commande."""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.add_note,
            "3": self.modify_note,
            "4": self.search_notes,
            "5": self.quit,
        }

    def display_menu(self):
        print("""
Carnet de Notes
1. Afficher toutes les notes
2. Ajouter une note
3. Modifier une note
4. Rechercher une note
5. Quitter
        """)

    def run(self):
        """Lance le menu."""
        while True:
            self.display_menu()
            choice = input("Entrez un choix : ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"'{choice}' n'est pas un choix valide.")

    def show_notes(self):
        """Affiche toutes les notes."""
        notes = self.notebook.notes
        if notes:
            for note in notes:
                print(f"ID: {note.id}, Mémo: {note.memo}, Balises: {note.tags}, Date: {note.creation_date}")
        else:
            print("Aucune note dans le carnet.")

    def add_note(self):
        """Ajoute une nouvelle note."""
        memo = input("Entrez le mémo : ")
        tags = input("Entrez les balises (séparées par des virgules) : ")
        self.notebook.add_note(memo, tags)
        print("Note ajoutée.")

    def modify_note(self):
        """Modifie une note existante."""
        note_id = int(input("Entrez l'ID de la note à modifier : "))
        new_memo = input("Entrez le nouveau mémo (laisser vide pour ne pas modifier) : ")
        new_tags = input("Entrez les nouvelles balises (laisser vide pour ne pas modifier) : ")
        if self.notebook.modify_note(note_id, new_memo or None, new_tags or None):
            print("Note modifiée.")
        else:
            print("Note introuvable.")

    def search_notes(self):
        """Recherche des notes."""
        search_term = input("Entrez le terme de recherche : ")
        results = self.notebook.search_notes(search_term)
        if results:
            for note in results:
                print(f"ID: {note.id}, Mémo: {note.memo}, Balises: {note.tags}, Date: {note.creation_date}")
        else:
            print("Aucune note ne correspond à votre recherche.")

    def quit(self):
        """Quitte l'application."""
        print("Merci d'avoir utilisé le Carnet de Notes. Au revoir !")
        exit()


if __name__ == "__main__":
    Menu().run()