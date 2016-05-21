# coding: utf-8
def afficher_grille(s):
	for i in range(9):
		for j in range(9):
			print s[i][j],
			if j in (2, 5):
				print " ",
		print
		if i in (2, 5):
			print

def verifier_ligne(array, i_ligne, start, end, val_test):
	for i in range (start, end):
		if array[i_ligne][i] == val_test:
			return 0
	return 1

def verifier_colonne(array, i_col, start, end, val_test):
	for i in range (start, end):
		if array[i][i_col] == val_test:
			return 0
	return 1
	
def verifier_zone(array, l_start, c_start, taille, val_test):
	for i in range (l_start, l_start + taille):
		for j in range (c_start, c_start + taille):
			if array[i][j] == val_test:
				return 0
	return 1
	
def est_valeur_possible(s, i, j, test):
	if verifier_ligne(s, i, 0, 9, test):
		if verifier_colonne(s, j, 0, 9, test):
			#decoupage en zones
			l_z = 0 #indice de la ligne de depart de la zone
			c_z = 0 #indice de la colonne de depart de la zone
			if i > 2:
				l_z = 3
				if i > 5:
					l_z = 6
			if j > 2:
				c_z = 3
				if j > 5:
					c_z = 6
			return verifier_zone(s, l_z, c_z, 3, test)
		else: #verifier_colonne
			return 0
	else: #verifier_ligne
		return 0				
	
	return 1

def case_a_traiter(s):
	for i in range(9): # i = indice de la ligne de la grille
		for j in range(9): # j = indice de la colonne de la grille
			#si la case est vide...
			if s[i][j] == 0:
				return i, j

	return -1, -1

def resoudre_grille(s):
	trous = 0
	i, j = case_a_traiter(s)
	#si il reste encore des case avec un "0" (= trou)
	if i != -1 and j != -1:
		trous = trous + 1	
		#valeur a essayer
		for test in range (1, 10):
			if est_valeur_possible(s, i, j, test):
				s[i][j] = test
				if resoudre_grille(s) == 0:
					return 0
				else:
					s[i][j] = 0
							
	return trous
