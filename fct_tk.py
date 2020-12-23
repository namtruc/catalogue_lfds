import pandas as pd

from tkinter import Tk
from tkinter.filedialog import askopenfilename


def choix_fichier (File):

    #input("\nAppuyer sur Entree pour choisir le fichier du catalogue francais non modifie\n")

    xl = pd.ExcelFile(File)
    
    if len(xl.sheet_names) > 1 :

    	print ("\n---Les differents feuilles presentes---")

    	for x in range (len(xl.sheet_names)) :
    		print (str(x)+" "+xl.sheet_names[x])
    
    	y = int(input("Entrer le numero de la feuille excel\n"))
    	v_sheet1 = xl.sheet_names[y]

    else :

        v_sheet1 = 0
    
    read_file = pd.read_excel(File,sheet_name=v_sheet1, skiprows = 1, header=None)		  
    
    return read_file

