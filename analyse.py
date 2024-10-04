import argparse
from modules.log_reader import LogReader

def main():
    # Gestion des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Script d'analyse de logs")
    parser.add_argument("repertoire", help="Chemin vers le répertoire contenant les fichiers de logs", type=str)
    args = parser.parse_args()

    # Créer une instance de LogReader avec le chemin du répertoire
    lecteur = LogReader(args.repertoire)

    # Trouver tous les fichiers de logs dans le répertoire
    fichiers_logs = lecteur.trouver_fichiers_logs()

    # Si des fichiers de logs sont trouvés, les lire un par un
    if fichiers_logs:
        for fichier_log in fichiers_logs:
            print(f"\nLecture du fichier : {fichier_log}")
            lecteur.lire_logs(fichier_log)  # Lire le fichier de logs

        # Afficher les lignes lues
        lecteur.afficher_lignes_lues()
    else:
        print("Aucun fichier de logs trouvé dans le répertoire.")

if __name__ == "__main__":
    main()