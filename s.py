# coding: utf-8

def verifier_ligne(array, i_ligne, val_test):
	""" Dans le Sudoku, une valeur ne peut apparaitre qu'une seule fois par ligne."""

	for i in range (9):
		if array[i_ligne][i] == val_test:
			return 0
	return 1

def verifier_colonne(array, i_col, val_test):
	""" Dans le Sudoku, une valeur ne peut apparaitre qu'une seule fois par colonne."""
	
	for i in range (9):
		if array[i][i_col] == val_test:
			return 0
	return 1
	
def verifier_zone(array, l_start, c_start, val_test):
	""" Dans le Sudoku, une valeur ne peut apparaitre qu'une seule fois par zone de 3 x 3."""
	
	for i in range (l_start, l_start + 3):
		for j in range (c_start, c_start + 3):
			if array[i][j] == val_test:
				return 0
	return 1
	
def est_valeur_possible(s, i, j, test):
	if verifier_ligne(s, i, test) and verifier_colonne(s, j, test):
		#decoupage en zones de 3 x 3 suivant la coordonnée de la case
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
		return verifier_zone(s, l_z, c_z, test)
	else:
		return 0				
	
	return 1

def case_a_traiter(grille):
	""" Retourne un tulple (indices de la grille) de la prochaine
	case à traiter. 0 est la valeur indiquant	une case "vide"."""
	
	#a_traiter est une liste de listes de tulpes
	a_traiter = [[(index_row, index_col) for index_col, val in enumerate(ligne) if val == 0] for index_row, ligne in enumerate(grille)]

	#ne pas reprendre les liste vides (== plus rien à traiter)
	liste_tulpes = [[tulpe for tulpe in ligne] for ligne in a_traiter if len(ligne) > 0]
	
	#retourner le premier élément de tout ce bordel
	try:
		return liste_tulpes[0][0]
	except IndexError:
		return None

	
def resoudre_grille(s):
	trous = 0
	coord = case_a_traiter(s)
	#si il reste encore des case avec un "0" (= trou)
	if coord != None:
		i = coord[0]
		j = coord[1]
	
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