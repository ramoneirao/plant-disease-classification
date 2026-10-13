# Script para descompactar os arquivos.

import logging
import zipfile

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

caminho_zip = "data/PlantVillage.zip"
pasta_destino = "data"

with zipfile.ZipFile(caminho_zip, "r") as arquivo_zip:
    arquivo_zip.extractall(pasta_destino)
    logging.info("Arquivos descompactados com sucesso!")