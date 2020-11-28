import os
import csv
import pandas as pd
import numpy as np
import sys

from tkinter import Tk	  
from tkinter.filedialog import askopenfilename
from os import path as os_path

dossier_python = os_path.abspath(os_path.split(__file__)[0])

##############################################################
##Emplacement colonnes

ref_fr = 0	 #### A=0, B=1, etc...
prix_fr = 6
nom_fr = 3
ori_fr = 4
reduc1_fr = 8
reduc2_fr = 9
reduc3_fr = 10

ref_es = 0
prix_es = 3
nom_es = 2
ori_es = 8####################
reduc1_es = 4
reduc2_es = 5
reduc3_es = 6


##############################################################
##Fonctions

def ecriture(liste):
	for element in liste :
		myfile.write(str(element))
		myfile.write('\n')

def isDigit(x):
	try:
		float(x)
		return True
	except ValueError:
		return False

def comp_nom (n_es,n_fr,mot,ref,erreur):
	if (str(n_es)).strip() != (str(n_fr)).strip() :
		erreur.append(' '+ref+'\n  FR = '+n_fr+"\n  ES = "+n_es+'\n')

def comp_prix (p_es,p_fr, ref, n_fr, n_es):
	if p_es == 0 :
		erreur9.append('  '+ref+' '+n_fr)
	elif p_es != 0 and p_es != p_fr :
            if (str(n_es)).strip() == (str(n_fr)).strip() :
                erreur10.append('\n '+ref+' '+n_fr[:40]+"\n  ancien prix  "+str(p_fr)+"\n  nouveau prix "+str(p_es))
            else :
                erreur10.append('\n '+ref+'\n  nom FR : '+n_fr+'\n  nom ES : '+n_es+'\n  prix FR '+str(p_fr)+'\n  prix ES '+str(p_es))

def comp_promo (prom_es,prom_fr, n_fr, ref, num):
	if prom_es != 0 and not (prom_fr == 'X' or prom_fr == 'x') :
		erreur11.append('  '+ref+' '+n_fr+' promo '+num)
	elif prom_es == 0 and (str(prom_fr).strip() == 'X' or str(prom_fr).strip() == 'x'):
		erreur12.append('  '+ref+' '+n_fr+' promo '+num)

def rech_nom (dfObj, value, coll): 

	listOfPos = [] 
	result = dfObj.isin([value]) 
	rows = list(result[coll][result[coll] == True].index) 
  
	for row in rows: 
		listOfPos.append((row)) 

	if (len(listOfPos)) == 0 :
		return 'empty'
	elif (len(listOfPos)) > 1 :
		return 'doublon' 
	else :
		return listOfPos[0]

def comp_class ():
	comp_prix (dic_es['Prix_es'],dic_fr['Prix_fr'], dic_fr['R_fr'], dic_fr['N_fr'],dic_es['N_es'])
	comp_nom (dic_es['N_es'],dic_fr['N_fr'],'nom', dic_fr['R_fr'], erreur8)
	comp_nom (dic_es['Ori_es'],dic_fr['Ori_fr'],'origine',dic_fr['R_fr'], erreur13)
	comp_promo (dic_es['Reduc_es1'],dic_fr['Reduc_fr1'], dic_fr['N_fr'],dic_fr['R_fr'],'1')
	comp_promo (dic_es['Reduc_es2'],dic_fr['Reduc_fr2'], dic_fr['N_fr'],dic_fr['R_fr'],'2')
	comp_promo (dic_es['Reduc_es3'],dic_fr['Reduc_fr3'], dic_fr['N_fr'],dic_fr['R_fr'],'3')

##############################################################
##Choix fichier esp

input("\nAppuyer sur Entree pour choisir le fichier excel du catalogue espagnol non modifie\n")

Tk().withdraw() 
file_esp = askopenfilename()

#vligned = int(input("Numero de la ligne de debut de la liste des produits catalogue esp\n"))
#if vligned <= 1 :
#	vligned == 2

vligned = 2

##############################################################
## Lecture fichier esp

xl = pd.ExcelFile(file_esp)

v_sheet1 = 0

if len(xl.sheet_names) > 1 :
	print ("\n---Les differents feuilles presentes---")
	for x in range (len(xl.sheet_names)) :
		print (str(x)+" "+xl.sheet_names[x])

	y = int(input("Entrer le numero de la feuille excel\n"))
	v_sheet1 = xl.sheet_names[y]

read_file = pd.read_excel(file_esp,sheet_name=v_sheet1, skiprows = vligned-1, header=None)		   

os.chdir(dossier_python)
read_file.to_csv ("Test1.csv",	
				  index = None, 
				  header = True)

df1 = pd.DataFrame(pd.read_csv("Test1.csv")) 

###########################################
## Nettoyage fichier esp

refa_es = df1.columns.values[ref_es] 
prixa_es = df1.columns.values[prix_es] 
noma_es = df1.columns.values[nom_es] 
reduca1_es = df1.columns.values[reduc1_es]
reduca2_es = df1.columns.values[reduc2_es]
reduca3_es = df1.columns.values[reduc3_es]

check = pd.isna(df1[refa_es])
check2 = pd.isna(df1[prixa_es])
check3 = pd.isna(df1[noma_es])

for x in range(len(df1.index)):
	if check[x] == True :   # si ref vide : ref=vide
		df1.iat[x,ref_es] = 'vide'

for x in range(len(df1.index)):
	if check[x] == True and check2[x] == True : # si prix et ref vide suppr ligne
		df1 = df1.drop([x])
	
for x in range(len(df1.index)):# si produit vide suppr ligne
	if check3[x] == True :
		df1 = df1.drop([x])

df1[prixa_es] = pd.to_numeric(df1[prixa_es],errors='coerce') # si prix = str => 0
df1 = df1.replace(np.nan, 0, regex=True)
df1[prixa_es] = df1[prixa_es].astype(float)

df1[reduca1_es] = pd.to_numeric(df1[reduca1_es],errors='coerce') # si prix = str => 0
df1 = df1.replace(np.nan, 0, regex=True)
df1[reduca1_es] = df1[reduca1_es].astype(float)

df1[reduca2_es] = pd.to_numeric(df1[reduca2_es],errors='coerce') # si prix = str => 0
df1 = df1.replace(np.nan, 0, regex=True)
df1[reduca2_es] = df1[reduca2_es].astype(float)

df1[reduca3_es] = pd.to_numeric(df1[reduca3_es],errors='coerce') # si prix = str => 0
df1 = df1.replace(np.nan, 0, regex=True)
df1[reduca3_es] = df1[reduca3_es].astype(float)

df1 = df1.drop_duplicates(subset=[prixa_es, refa_es, noma_es])# supr des vrais doublons

df1[prixa_es] = round((df1[prixa_es] * 1.37),2)

list2 = [] ### reconstruction de l'index

for x in range (len(df1.index)):
	list2.append(x)

df1.index = list2

#####################################
#### recherche duplicata fichier esp

list_es = df1[refa_es].tolist()

dupl_es = [] 

if not len(list_es) == len(set(list_es)):
	for i in list_es:
		if list_es.count(i) > 1 and i != 'vide':
			dupl_es.append(i)

##############################################################
## Choix fichier fr

input("\nAppuyer sur Entree pour choisir le fichier du catalogue francais non modifie\n")

Tk().withdraw() 
file_fr = askopenfilename()

#vligned_fr = int(input("Numero de la ligne de debut de la liste des produits catalogue fr\n"))
#if vligned_fr <= 1 :
	#vligned_fr == 2

vligned_fr =2

##############################################################
## Lecture fichier fr

xl = pd.ExcelFile(file_fr)

v_sheet1 = 0

if len(xl.sheet_names) > 1 :
	print ("\n---Les differents feuilles presentes---")
	for x in range (len(xl.sheet_names)) :
		print (str(x)+" "+xl.sheet_names[x])

	y = int(input("Entrer le numero de la feuille excel\n"))
	v_sheet1 = xl.sheet_names[y]

read_file = pd.read_excel(file_fr,sheet_name=v_sheet1, skiprows = vligned-1, header=None)		  

os.chdir(dossier_python)
read_file.to_csv ("Test2.csv",	
				  index = None, 
				  header = True)

df2 = pd.DataFrame(pd.read_csv("Test2.csv")) 

##############################################################
## Verif fichier fr

refa_fr = df2.columns.values[ref_fr]
prixa_fr = df2.columns.values[prix_fr] 
noma_fr = df2.columns.values[nom_fr]

df2[prixa_fr] = pd.to_numeric(df2[prixa_fr])  ## convertion des prix, arret programme erreur 
df2[prixa_fr] = df2[prixa_fr].astype(float)
df2[prixa_fr] = round((df2[prixa_fr]),2)

if (df2[refa_fr].isnull) == True :
	print ("\nReference manquante dans le catalogue fr")
	sys.exit()

list_fr = df2[refa_fr].tolist()
dupl_fr = set() 

if not len(list_fr) == len(set(list_fr)):
	# ~ print ("\nDoublon de reference cote fr ")
	for i in list_fr:
		if list_fr.count(i) > 1:
			dupl_fr.add(i)

##############################################################
##	Comparaison

myfile = open("retour.txt", "w")

erreur1 = []
erreur2 = []
erreur3 = []
erreur4 = []
erreur5 = []
erreur6 = []
erreur7 = []
erreur8 = []
erreur9 = []
erreur10 = []
erreur11 = []
erreur12 = []
erreur13 = []
erreur14 = []

def fdico_es () :
	dico_es  =	{
				'N_es' : df1.iat[a,nom_es],
				'R_es' : df1.iat[a,ref_es],
				'Prix_es' : df1.iat[a,prix_es],
				'Ori_es' : df1.iat[a,ori_es],
				'Reduc_es1' : df1.iat[a,reduc1_es],
				'Reduc_es2' : df1.iat[a,reduc2_es],
				'Reduc_es3' : df1.iat[a,reduc3_es]
				}
	return dico_es

def fdico_fr () :
	dico_fr = {
				'N_fr' : df2.iat[x,nom_fr],
				'R_fr' : df2.iat[x,ref_fr],
				'Prix_fr' : df2.iat[x,prix_fr],
				'Ori_fr' : df2.iat[x,ori_fr],
				'Reduc_fr1' : df2.iat[x,reduc1_fr],
				'Reduc_fr2' : df2.iat[x,reduc2_fr],
				'Reduc_fr3' : df2.iat[x,reduc3_fr]
				}
	return dico_fr

for x in dupl_fr :	### Verif si les doublons fr sont aussi des doublons es
	if not x in dupl_es :
		erreur1.append("Produit ref "+x)

for x in range (len(df2.index)) :
	dic_fr = fdico_fr() ### Redef des valeurs avec changement x
	if dic_fr['R_fr'] in dupl_es :				 ## Recherche si ref est en doublon cote esp
		a = rech_nom (df1, dic_fr['N_fr'], noma_es) ## Recherche par nom
		if a == 'empty' :
			erreur2.append('  '+dic_fr['R_fr']+' '+dic_fr['N_fr'])
		elif a == 'doublon' :
			erreur3.append('  '+dic_fr['R_fr']+' '+dic_fr['N_fr'])
		else :
			dic_es = fdico_es()
			if dic_fr['R_fr'] == dic_es['R_es']:
				comp_class ()			   #### Comparaison classique
			else :
				erreur14.append(' REF FR = '+dic_fr['R_fr']+'\n REF ES = '+dic_es['R_es']+'\n '+dic_fr['N_fr'])

	else :
		a = rech_nom (df1, dic_fr['R_fr'], refa_es)		   ## Recherche ref cote esp
		if a == 'empty' :							   ## Echec recherche
			a = rech_nom (df1, dic_fr['N_fr'], noma_es)    ## Recherche nom
			if a == 'empty' :						   ## Echec
				erreur4.append('  '+dic_fr['R_fr']+' '+dic_fr['N_fr'])
			elif a == 'doublon' :
				erreur5.append('  '+dic_fr['R_fr']+' '+dic_fr['N_fr'])
			else :	
				dic_es = fdico_es()								
				erreur6.append('  Ref FR = '+dic_fr['R_fr']+' ' +dic_fr['N_fr'][:20]+'\n'
                                               +'  Ref ES = '+dic_es['R_es'])
				comp_class()					  #### Comparaison classique
		elif a == 'doublon' :
			erreur7.append("!!!!!!!!erreur anormale dans la detection des doublons (a signaler), la comparaison pour le produit"+dic_fr['R_fr'])
		else : 
			dic_es = fdico_es()  
			comp_class ()####possible erreur prix		   #### Comparaison classique



myfile.write(
        '####\n'
        'Ce fichier recapitule les differences entre les deux catalogues trouvees par le script\n'
        'Le terme FR renvoie au catalogue fruitstock avec les noms en espagnol, le terme ES renvoie au catalogue Ruffino.\n'
        'Toutes les references et noms donnes font reference au catalogue FR sauf si mention contraire\n'
        'Les produits qui devront etre verifies et compares manuellement a partir des catalogues originaux seront indiques, sinon les comparaisons et rectification pourront se faire uniquement a partir de ce fichier\n'
        '####\n\n\n'
            )

myfile.write(
      '\n\n\n####################\n'
      '##########\n'
      'Code 01\n'
      'FR : reference en doublon, ES : une seule reference.\n'
      'A verifier manuellement\n'
      'Attention ces produits peuvent apparaitre plus bas dans ce fichier en provoquant des faux positifs\n\n'
      'ex : FR 7206 Poires 500g\n'
      '     FR 7206 Poires 1kg\n'
      '     ES 7206 Poires 1kg\n'
      '##########\n\n'
           )
ecriture(erreur1)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 02\n'
        'Ref FR presente au moins deux fois dans catalogue ES mais nom different\n'
        'A verifier manuellement\n'
        'ex : FR 7206 Poires\n'
        '     ES 7206 Poires Bio\n'
        '     ES 7206 Poires du verger\n'
        '##########\n\n'
             )
ecriture(erreur2)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 03\n'
        'Reference et nom en doublon cote espagnol, prix probablement different.\n'
        'A verifier manuellement \n'
        'ex : FR 7206 Poires bio\n'
        '     ES 7206 Poires bio\n'
        '     ES 7206 Poires bio\n'
        '##########\n\n'
        )
ecriture(erreur3)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 04\n'
        'REF et nom non trouves dans catalogue ES\n '
        'Le produit n\'est probablement plus reference\n'
        '##########\n\n'
        )
ecriture(erreur4)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 05\n'
        'REF FR non trouve cote ES mais nom trouve au moins 2 fois\n'
        'A verifier manuellement\n'
        'ex : FR 7206 Poires bio\n'
        '     ES 7260 Poires bio\n'
        '     ES 7280 Poires bio\n'
        '##########\n\n'
       )
ecriture(erreur5)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 06\n'
        'REF differentes FR vs ES et nom identique\n'
        'Verification manuelle inutile\n'
        'ex : FR 7206 Poires bio\n'
        '     ES 7270 Poires bio\n'
        '##########\n\n'
        )
ecriture(erreur6)


myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 08\n'
        'Difference entre les noms\n'
        'Verification manuelle inutile\n'
        'ex : FR 7206 Poires \n'
        '     ES 7206 Poires bio\n'
        '##########\n\n'
        )
ecriture(erreur8)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 09\n'
        'Prix manquant cote espagnol\n'
        'ex FR 7206 Poires 5 euros\n'
        '   ES 7206 Poires -------\n'
        '##########\n\n'
        )
ecriture(erreur9)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 10\n'
        'Difference de prix entre les 2 catalogues\n'
        'Si le nom ES/FR est different, les 2 seront ecrit pour eviter certaines erreurs avec des changements de produits qui gardent la meme ref\n'
        '##########\n\n'
        )
ecriture(erreur10)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 11\n'
        'Promo manquante cote francais \n'
        )
myfile.write('################\n\n')
ecriture(erreur11)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 12\n'
        'Promo manquante cote espagnol\n'
        )
myfile.write('##########\n\n')
ecriture(erreur12)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 13\n'
        'Difference entre les origines\n'
        )
myfile.write('##########\n\n')
ecriture(erreur13)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 14\n'
        'REF differentes et nom identique. A controler et corriger\n'
        '##########\n\n'
        )
ecriture(erreur14)

myfile.write(
        '\n\n\n####################\n'
        '##########\n'
        'Code 07\n'
        '##########\n\n'
        )
ecriture(erreur7)

myfile.close()

os.remove("Test2.csv")

print("\nComparaison terminee, resultat sauve dans retour.txt dans le dossier contenant le script\n")


rep = int(input('Taper 1 pour creer un tableur comportant tous les produits du catalogue espagnol non presents dans le catalogue francais sinon taper 2\n'))

if rep != 1:
	os.remove("Test1.csv")
	sys.exit()

df3 = df1

for a in range (len(df1.index)):
	dic_es = fdico_es()
	x= rech_nom (df2, dic_es['N_es'], noma_fr)
	if x != 'empty':
		df3 = df3.drop([a])
	if df1.iat[a,prix_es] == 0 : 
		df3 = df3.drop([a])

df1 = df3
df1.drop(df1.columns[[1,7,9,10,11,12]], axis = 1, inplace = True) 
df1.columns =['Ref', 'Nom', 'Prix', 'Promo','Promo2','Promo3','Origine'] 
df1 = df1.sort_values('Nom')
df1['Promo'] = round((df1['Promo']),2)
df1['Promo2'] = round((df1['Promo2']),2)
df1['Promo3'] = round((df1['Promo3']),2)
df1.to_csv('Comparaison.csv',index=False) 
os.remove("Test1.csv")

print("\nComparaison terminee, resultat sauve dans Comparaison.csv dans le dosier contenant le script\n")
input("Appuyer sur entree pour quitter le programme")
