# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
from s import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	grille = [[0 for i in range(9)] for j in range(9)]
	
	#exemple hard-codé. TODO : générateur de grille valide...
	grille[0] = [0,1,0, 0,2,5, 0,7,0]
	grille[1] = [0,0,5, 0,1,7, 0,6,9]
	grille[2] = [7,8,9, 0,3,0, 0,0,0]

	grille[3] = [0,5,0, 0,0,0, 0,0,0]
	grille[4] = [0,6,3, 1,9,2, 7,4,5]
	grille[5] = [0,0,0, 0,0,6, 1,3,2]

	grille[6] = [0,0,1, 0,7,0, 0,5,0]
	grille[7] = [2,0,0, 0,5,1, 9,8,7]
	grille[8] = [5,0,8, 3,0,0, 2,1,0]
	
	if request.method == 'POST':
		resoudre_grille(grille)
	
	return render_template('index.html', grille = grille)

if __name__ == '__main__':
	app.run()
