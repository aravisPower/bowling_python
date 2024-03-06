# Bowling - V2
import random
import time

nombreToursJoueur1 = 0
nombreToursJoueur2 = 0
pointsJoueur1 = 0
pointsJoueur2 = 0

def lancer(nbreQuillesRestantes):
	'''tirage au sort du nombre de quilles renversées,
	puis renvoie le nombre de quilles qui restent debout'''
	tirage = random.randint(0, nbreQuillesRestantes)	# contient le nombre de quilles tombées
	return (nbreQuillesRestantes - tirage)

def jeu(joueur, tourDeJeu):
	'''effectue les tours de jeu et renvoie les points'''
	print("")
	print("Tour n°{}, {}".format(tourDeJeu, joueur))
	print("--------------------")
	nbreQuillesRestantes = lancer(10)
	if (nbreQuillesRestantes == 0):
		print("*** STRIKE !!!! ***")
		return 30
	else:
		print("Il reste {} quilles ; 2ème lancer".format(nbreQuillesRestantes))
		nbreQuillesApresTour2 = lancer(nbreQuillesRestantes)
		if (nbreQuillesApresTour2 == 0):
			print("*** SPARE !!!! ***")
			return 20
		else:
			print("Il reste {} quilles après le 2ème lancer. {} pts sont marqués par {}".format(nbreQuillesApresTour2, 10-nbreQuillesApresTour2, joueur)) 
			return (10 - nbreQuillesApresTour2)



for i in range(10):
	# Le joueur 1 joue
	pointsJoueur1 = pointsJoueur1 + jeu("Joueur 1", i+1)
	time.sleep(4)
	print("")
	# Le joueur 2 joue
	pointsJoueur2 = pointsJoueur2 + jeu("Joueur 2", i+1)
	time.sleep(4)
	#afficherScore(pointsJoueur1, pointsJoueur2)

print("")
print("Partie terminée **********")
print("")
print("Joueur 1 : {} pts".format(pointsJoueur1))
print("")
print("Joueur 2 : {} pts".format(pointsJoueur2))
print("")
if (pointsJoueur1 >= pointsJoueur2):
	vainqueur = "Joueur 1"
else: vainqueur = "Joueur 2"
print("Le vainqueur est {}".format(vainqueur))
