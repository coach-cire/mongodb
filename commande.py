#Afficher la liste des équipes
db.matchs.distinct("disputer.equipe_b.nom_equipe")
#Afficher la liste des matchs
db.matchs.find({},{"disputer.equipe_a.nom_equipe":1,"disputer.equipe_b.nom_equipe":1}).pretty()
#Afficher la liste des stades
db.matchs.distinct("stade.nom_stade")
#Afficher la liste des arbitres
db.matchs.distinct("arbitrer.arbitre.nom_arbitre")
#Afficher la liste des matchs avec les scores
db.matchs.find({},{"disputer.equipe_a.nom_equipe":1,"disputer.equipe_b.nom_equipe":1,"disputer.score":1}).pretty()
#Afficher la liste des joueurs pour un match donné
db.matchs.find({"_id":2},{"jouer.licence.joueur.nom_joueur":1}).pretty()
#Afficher les matchs de 1/4 de finale
db.matchs.find({"tour.libelle_tour":"Quart-final"},{"disputer.equipe_a.nom_equipe":1,"disputer.equipe_b.nom_equipe":1}).pretty()
#Afficher les matchs de 1/2 de finale
db.matchs.find({"tour.libelle_tour":"Demi-final"},{"disputer.equipe_a.nom_equipe":1,"disputer.equipe_b.nom_equipe":1}).pretty()
#Afficher la finale
db.matchs.find({"tour.libelle_tour":"Finale"},{"disputer.equipe_a.nom_equipe":1,"disputer.equipe_b.nom_equipe":1}).pretty()




