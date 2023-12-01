from include.objects import OCCScrapper
import pandas as pd


def run():

    collecor_objet = OCCScrapper()
    # Obtiene referencias de todos los links de las vacantes y crea un csv
    collecor_objet.get_all_href()
    # extrae atributos vacante por vacante y crea un csv
    collecor_objet.get_all_attributes()

