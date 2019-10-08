#import pandas et MongoClient
import pandas as pd
from pymongo import MongoClient
#Connection au serveur mongodb
serveur = MongoClient()
serveur = MongoClient('localhost', 27017)
#Création de la base de données mongodb
database = serveur.mamadouba
#Création de la collection
regions = database.cirelo
#Importation du fichier csv vers la base de données mongodb
envoie = pd.read_csv("donnee.csv")
#Convertion dataframe en dictionnaire
a= envoie.to_dict(orient = 'records')
affiche = database.regions.insert_many(a)
