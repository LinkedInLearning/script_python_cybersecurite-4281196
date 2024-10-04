import os

class LogReader:
    def __init__(self, repertoire):
        """
        Constructeur qui initialise l'objet avec le chemin du répertoire contenant les fichiers de logs.
        """
        self.repertoire = repertoire  # Attribut pour stocker le chemin du répertoire
        self.lignes_lues = []  # Liste pour stocker les lignes lues de tous les fichiers

    def trouver_fichiers_logs(self, extension=".log"):
        """
        Parcourt le répertoire et renvoie une liste de fichiers de logs avec l'extension spécifiée.

        Paramètres :
        extension (str) : Extension des fichiers à rechercher (par défaut '.log').

        Retourne :
        list : Liste des fichiers de logs trouvés dans le répertoire.
        """
        fichiers_logs = []
        try:
            # Parcourt le répertoire et récupère tous les fichiers avec l'extension donnée
            for fichier in os.listdir(self.repertoire):
                if fichier.endswith(extension):
                    fichiers_logs.append(os.path.join(self.repertoire, fichier))
            return fichiers_logs
        except FileNotFoundError:
            print(f"Erreur : Le répertoire {self.repertoire} n'a pas été trouvé.")
            return []

    def lire_logs(self, fichier_log):
        """
        Lit un fichier de logs et ajoute son contenu dans l'attribut 'lignes_lues'.

        Paramètres :
        fichier_log (str) : Chemin vers le fichier de logs à lire.
        """
        try:
            with open(fichier_log, 'r') as f:
                self.lignes_lues.extend(f.readlines())  # Ajouter les lignes lues dans l'attribut 'lignes_lues'
            print(f"Le fichier {fichier_log} a été lu avec succès.")
        except FileNotFoundError:
            print(f"Erreur : Le fichier {fichier_log} n'a pas été trouvé.")
    
    def afficher_lignes_lues(self):
        """
        Affiche le nombre de lignes lues et les premières lignes de tous les fichiers.
        """
        if self.lignes_lues:
            print(f"Nombre total de lignes lues : {len(self.lignes_lues)}")
            print("Premières lignes lues :")
            for ligne in self.lignes_lues[:5]:  # Afficher les 5 premières lignes lues
                print(ligne.strip())
        else:
            print("Aucune ligne n'a été lue.")