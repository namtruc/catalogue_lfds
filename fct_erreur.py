import os
from os import path as os_path

def ecriture(liste,myfile):
	for element in liste :
		myfile.write(str(element))
		myfile.write('\n')

def error (erreur1,erreur2,erreur3,erreur4,erreur5,erreur6,erreur7,erreur8,erreur9,erreur10,erreur11,erreur12,erreur13,erreur14):

    dossier_python = os_path.abspath(os_path.split(__file__)[0])
    dossier_usr = dossier_python + '/fichiers_utilisateur'

    os.chdir(dossier_usr)

    myfile = open("retour.txt", "w")

    myfile.write(
            '####\n'
            'Ce fichier recapitule les differences entre les deux catalogues trouvees par le script\n'
            'Le terme FR renvoie au catalogue fruitstock avec les noms en espagnol, le terme ES renvoie au catalogue Ruffino.\n'
            'Toutes les references et noms donnes font reference au catalogue FR sauf si mention contraire\n\n'
            'Le fichier retour.xlsx integre les differents erreures avec des codes couleurs\n'
	    'Couleur verte : le contenu des cellules a ete mise a jour automatiquement avec les donnees du catalogue ES. A noter que ce sont les seules donnees qui ont ete modifiees automatiquement par le script\n'
            'Couleur jaune : concerne les traductions des designations et origine produit pour lesquelles le nom espagnol a ete mis a jour\n'
            'Couleur marron : concerne les prix manquant ou avec une difference anormalement importante (plus de 30%) ainsi que les prix de gros qui auraient disparu cote espagnol. A verifier manuellement\n'
            'Couleur grise : erreur 04, produit probablement absent du catalogue ES\n'
            'Couleur rouge : erreurs rendant la comparaison automatique impossible, la ligne entiere sera a verifier manuellement\n'
            '####\n\n\n'
                )

##########################################################################
##########################################################################

    myfile.write(
            '\n\n################################\n'
            '################################\n'
            'VERT/JAUNE\n'
            '################################\n'
            '################################\n\n\n'
                )

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
    ecriture(erreur8,myfile)

    myfile.write(
            '\n\n\n####################\n'
            '##########\n'
            'Code 11\n'
            'Promo manquante cote francais \n'
            )
    myfile.write('################\n\n')
    ecriture(erreur11,myfile)

#    myfile.write(
#            '\n\n\n####################\n'
#            '##########\n'
#            'Code 13\n'
#            'Difference entre les origines\n'
#            )
#    myfile.write('##########\n\n')
#    ecriture(erreur13,myfile)

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
    ecriture(erreur6,myfile)

    myfile.write(
            '\n\n\n####################\n'
            '##########\n'
            'Code 10\n'
            'Difference de prix entre les 2 catalogues\n'
            'Si le nom ES/FR est different, les 2 seront ecrit pour eviter certaines erreurs avec des changements de produits qui gardent la meme ref\n'
            '##########\n\n'
            )
    ecriture(erreur10,myfile)

##########################################################################
########################################################################## 
             
    myfile.write(
            '\n\n\n################################\n'
            '################################\n'
            'MARRON\n'
            '################################\n'
            '################################\n\n\n'
                )

    myfile.write(
            '\n\n\n####################\n'
            '##########\n'
            'Code 09\n'
            'Prix manquant cote espagnol\n'
            'ex FR 7206 Poires 5 euros\n'
            '   ES 7206 Poires -------\n'
            '##########\n\n'
            )
    ecriture(erreur9,myfile)
    
    myfile.write(
            '\n\n\n####################\n'
            '##########\n'
            'Code 12\n'
            'Promo manquante cote espagnol\n'
            )
    myfile.write('##########\n\n')
    ecriture(erreur12,myfile)
##########################################################################
##########################################################################

    myfile.write(
            '\n\n\n################################\n'
            '################################\n'
            'ROUGE\n'
            '################################\n'
            '################################\n\n\n'
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
    ecriture(erreur1,myfile)
    
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
    ecriture(erreur2,myfile)
    
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
    ecriture(erreur3,myfile)

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
    ecriture(erreur5,myfile)

    myfile.write(
            '\n\n\n####################\n'
            '##########\n'
            'Code 14\n'
            'REF differentes et nom identique pour un produit present en doublon cote ES. A controler et corriger\n'
            'ex : FR 7206 Poires bio\n'
            '     ES 7260 Poires bio\n'
            '     ES 7260 Poires bio\n'
            '##########\n\n'
            )
    ecriture(erreur14,myfile)

##########################################################################
##########################################################################

    myfile.write(
            '\n\n\n################################\n'
            '################################\n'
            'GRIS\n'
            '################################\n'
            '################################\n\n\n'
                )

    myfile.write(
            '\n\n\n####################\n'
            '##########\n'
            'Code 04\n'
            'REF et nom non trouves dans catalogue ES\n '
            'Le produit n\'est probablement plus reference\n'
            '##########\n\n'
            )
    ecriture(erreur4,myfile)

##########################################################################
##########################################################################
    myfile.write(
            '\n\n\n################################\n'
            '################################\n'
            'NOIR\n'
            '################################\n'
            '################################\n\n\n'
                )

    myfile.write(
            '\n\n\n####################\n'
            '##########\n'
            'Code 07\n'
            '##########\n\n'
            )
    ecriture(erreur7,myfile)    

##########################################################################
##########################################################################
    
    myfile.close()
