import time
import shutil
import os

# Dossier contenant les logs statiques
SOURCE_LOG = "ElasticSearch/firefox_build.log"  

TARGET_LOG = "ElasticSearch/live_firefox.log"

# Supprime l'ancien fichier live s'il existe
if os.path.exists(TARGET_LOG):
    os.remove(TARGET_LOG)

print("Simulation de flux en temps réel démarrée...")
with open(SOURCE_LOG, "r", encoding="utf-8") as source:
    with open(TARGET_LOG, "a", encoding="utf-8") as target:
        for line in source:
            target.write(line)
            target.flush()  # force l’écriture immédiate
            time.sleep(0.5)  # envoie une ligne toutes les 0.5 secondes
print("Simulation terminée.")
