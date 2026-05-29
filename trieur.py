import os
import shutil
from datetime import datetime

# Configuration des paramètres globaux
PATH = "C:/Users/[nom_utilisateur]/Desktop/Test_Job" 
LOG_NAME = "rapport_activite.txt"

def executer_tri():
    """
    Parcourt le répertoire cible, trie les fichiers par extension 
    et consigne chaque opération dans un journal d'audit.
    """
    if not os.path.exists(PATH):
        print(f"Erreur : Le répertoire {PATH} est introuvable.")
        return

    # Analyse du contenu du répertoire
    files = os.listdir(PATH)
    log_path = os.path.join(PATH, LOG_NAME)

    # Initialisation de la session dans le fichier log
    with open(log_path, "a", encoding="utf-8") as log:
        horodatage = datetime.now().strftime("%d/%m/%Y %H:%M")
        log.write(f"\n--- SESSION DE MAINTENANCE DU {horodatage} ---\n")

        for file in files:
            # Exclusion du fichier log et des scripts source de l'automatisation
            if file == LOG_NAME or file.endswith(".py"):
                continue
                
            # Séparation du nom et de l'extension
            filename, extension = os.path.splitext(file)
            ext_name = extension[1:].lower() 

            # Ignorer les dossiers ou fichiers sans extension
            if ext_name == "": 
                continue

            # Création dynamique du répertoire de destination si inexistant
            target_folder = os.path.join(PATH, ext_name)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # Execution du transfert sécurisé
            try:
                shutil.move(os.path.join(PATH, file), os.path.join(target_folder, file))
                log.write(f"[OK] Migration de {file} vers le dossier {ext_name}\n")
            except Exception as e:
                log.write(f"[ERREUR] Échec du traitement pour {file} : {e}\n")

if __name__ == "__main__":
    executer_tri()
    print("Processus d'automatisation terminé. Rapport généré.")