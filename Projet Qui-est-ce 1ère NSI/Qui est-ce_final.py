# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:17:57 2024

@author: MARION, EDWARD, INES
"""

##-----Importation des Modules-----##
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import random
##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Qui est-ce ?')
global nbr_essai, ouinon, message
rep=None
compteur_label=Label(fen, text="Essais restants : ...", bg="#333333", font="Roman", fg="white",height=2)
compteur_label.grid(row=1,column=0, columnspan=5)
ouinon=Label(fen, text=rep, bg="#333333", font="Roman", fg="white",height=2)
ouinon.grid(row=1,column=2, columnspan=5)
'''
# Créer une list où l'on peut selectionner une réponse pour afficher les noms des personnages restants
liste_personnages = Listbox(fen, selectmode=SINGLE)
liste_personnages.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
'''

'''
Les caractéristiques des personnages des grilles dans des dictionnaires
ayant pour clés le nom du personnage et valeurs un autre dictionnaire contenant
le nom de la caractéristique pour clé et la caractéristique du personnage pour valeur
'''

personnages = {
    'gojo': {'genre': "homme", 'cheveux': "blanc", 'yeux': "bleu", 'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'livai': {'genre': "homme", 'cheveux': "brun", 'yeux': "gris", 'expression': "aigris", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'senku': {'genre': "homme", 'cheveux': "vert", 'yeux': "rouge", 'expression': "fiere", 'traits du visage': "cicatrices", 'bouche': "fermee", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'itachi': {'genre': "homme", 'cheveux': "noir", 'yeux': "rouge", 'expression': "aigris", 'bouche': "ouverte", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'deku': {'genre': "homme", 'cheveux': "vert", 'yeux': "vert", 'expression': "triste", 'traits du visage': "tache de rousseur", 'bouche': "fermee", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'killua': {'genre': "homme", 'cheveux': "blanc", 'yeux': "gris", 'expression': "aigris", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien', 'bijoux': "non"},
    'nobara': {'genre': "femme", 'cheveux': "orange", 'yeux': "marron", 'expression': "triste", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'shikimori': {'genre': "femme", 'cheveux': "rose", 'yeux': "bleu", 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'millim': {'genre': "femme", 'cheveux': "rose", 'yeux': "bleu", 'expression': "heureuse", 'bouche': "ouverte" ,'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'maomao': {'genre': "femme", 'cheveux': "vert", 'yeux': "bleu", 'expression': "aigris", 'traits du visage': "tache de rousseur", 'bouche': "fermee", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'nami': {'genre': "femme", 'cheveux': "orange", 'yeux': "marron", 'expression': "fiere", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'natsu': {'genre': "homme", 'cheveux': "rose", 'yeux': "gris", 'expression': "fiere", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'noelle': {'genre': "femme", 'cheveux': "blanc", 'yeux': "rose", 'expression': "fiere", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'robin': {'genre': "femme", 'cheveux': "noir", 'yeux': "bleu", 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"},
    'kyo': {'genre': "homme", 'cheveux': "orange", 'yeux': "orange", 'expression': "triste", 'bouche': "ouverte", 'traits du visage':"rien", 'couleur de peau': 'blanche','accessoire': 'rien','bijoux': "non"}
}
personnagedisney= {
    'aladdin': {'genre': 'homme', 'cheveux': 'noir', 'yeux': 'marron', 'accessoire': 'chapeau', 'couleur de peau': 'metisse', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "ouverte"},
    'ariel': {'genre': 'femme', 'cheveux': 'roux', 'yeux': 'bleu', 'bijoux': "boucle d'oreille", 'couleur de peau': 'blanche','accessoire': 'rien', 'traits du visage':"rien", 'expression': "heureuse",'bouche': "ouverte"},
    'aurore': {'genre': 'femme', 'cheveux': 'blond', 'yeux': 'marron', 'accessoire': 'couronne', 'couleur de peau': 'blanche', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "ouverte"},
    'flynn': {'genre': 'homme', 'cheveux': 'chatain', 'yeux': 'marron', 'couleur de peau': 'blanche','accessoire': 'rien', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "fermee"},
    'elsa': {'genre': 'femme', 'cheveux': 'blond', 'yeux': 'bleu', 'couleur de peau': 'blanche','accessoire': 'rien', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "ouverte"},
    'hercule': {'genre': 'homme', 'cheveux': 'roux', 'yeux': 'bleu', 'accessoire': 'bandeau', 'couleur de peau': 'metisse', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "ouverte"},
    'joe': {'genre': 'homme', 'cheveux': 'noir', 'yeux': 'vert', 'accessoire': 'chapeau', 'couleur de peau': 'noir', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "fermee"},
    'jasmine': {'genre': 'femme', 'cheveux': 'noir', 'yeux': 'marron', 'bijoux': 'collier et boucle d\'oreille', 'couleur de peau': 'metisse','accessoire': 'rien', 'traits du visage':"rien", 'expression': "heureuse",'bouche': "fermee"},
    'naveen': {'genre': 'homme', 'cheveux': 'chatain', 'yeux': 'marron', 'accessoire': 'couronne', 'couleur de peau': 'metisse', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "ouverte"},
    'li': {'genre': 'homme', 'cheveux': 'noir', 'yeux': 'marron', 'couleur de peau': 'blanche','accessoire': 'rien', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "fermee"},
    'ralph': {'genre': 'homme', 'cheveux': 'chatain', 'yeux': 'vert', 'couleur de peau': 'blanche','accessoire': 'rien', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "fermee"},
    'raiponce': {'genre': 'femme', 'cheveux': 'blond', 'yeux': 'vert', 'couleur de peau': 'blanche','accessoire': 'rien', 'traits du visage':"rien",'bijoux': "non", 'expression': "heureuse",'bouche': "fermee"},
    'tiana': {'genre': 'femme', 'cheveux': 'noir', 'yeux': 'marron', 'accessoire': 'couronne', 'bijoux': 'boucle d\'oreille', 'couleur de peau': 'noir', 'traits du visage':"rien", 'expression': "heureuse",'bouche': "ouverte"},
    'vaiana': {'genre': 'femme', 'cheveux': 'chatain', 'yeux': 'marron', 'bijoux': 'collier', 'couleur de peau': 'metisse','accessoire': 'rien', 'traits du visage':"rien", 'expression': "heureuse",'bouche': "fermee"},
    'belle':{'genre':"femme", 'cheveux':"chatain", 'yeux':"marron", 'couleur de peau':"blanche",'expression': "heureuse", 'bouche': "ouverte",'traits du visage':"rien",'accessoire': 'noeud','bijoux': "non"}
} 
personnagecelebre = {
    
    'ariana': {'genre': 'femme', 'cheveux': 'blond', 'yeux': 'marron', 'bijoux': "boucle d'oreille", 'couleur de peau': 'blanche', 'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"rien",'accessoire': 'rien'},
    'becky': {'genre': 'femme', 'cheveux': 'chatain', 'yeux': 'marron', 'bijoux': 'collier', 'couleur de peau': 'blanche', 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"rien",'accessoire': 'rien'},
    'jenna': {'genre': 'femme', 'cheveux': 'chatain', 'yeux': 'marron', 'bijoux': "boucle d'oreille", 'couleur de peau': 'metisse', 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"rien",'accessoire': 'rien'},
    'johnny': {'genre': 'homme', 'cheveux': 'chatain', 'yeux': 'marron', 'bijoux': 'collier,bracelet et bagues', 'couleur de peau': 'blanche', 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"barbe",'accessoire': 'lunettes'},
    'lena': {'genre': 'femme', 'cheveux': 'chatain', 'yeux': 'marron', 'bijoux': 'boucle d\'oreille,bague et bracelet', 'couleur de peau': 'metisse', 'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"rien",'accessoire': 'rien'},
    'leonardo': {'genre': 'homme', 'cheveux': 'blond', 'yeux': 'bleu', 'couleur de peau': 'blanche','bijoux': "non", 'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"rien",'accessoire': 'rien'},
    'millie': {'genre': 'femme', 'cheveux': 'blond', 'yeux': 'vert', 'bijoux': "boucle d'oreille", 'couleur de peau': 'blanche', 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"rien",'accessoire': 'rien'},
    'squeezie': {'genre': 'homme', 'cheveux': 'blond', 'yeux': 'bleu', 'bijoux': "boucle d'oreille", 'couleur de peau': 'blanche', 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"barbe",'accessoire': 'rien'},
    'morgan': {'genre': 'homme', 'cheveux': 'blond', 'yeux': 'marron', 'couleur de peau': 'noir','bijoux': "non", 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"barbe",'accessoire': 'rien'},
    'robert': {'genre': 'homme', 'cheveux': 'chatain', 'yeux': 'marron', 'couleur de peau': 'blanche','bijoux': "non", 'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"barbe",'accessoire': 'lunettes'},
    'theweeknd': {'genre': 'homme', 'cheveux': 'noir', 'yeux': 'marron', 'bijoux': 'collier', 'couleur de peau': 'noir', 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"barbe",'accessoire': 'lunettes'},
    'tom': {'genre': 'homme', 'cheveux': 'chatain', 'yeux': 'marron', 'couleur de peau': 'blanche','bijoux': "non", 'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"rien",'accessoire': 'rien'},
    'whoopi': {'genre': 'femme', 'cheveux': 'noir', 'yeux': 'marron', 'bijoux': "boucle d'oreille", 'couleur de peau': 'noir', 'expression': "heureuse", 'bouche': "fermee", 'traits du visage':"rien",'accessoire': 'lunettes'},
    'zoe': {'genre': 'femme', 'cheveux': 'noir', 'yeux': 'marron', 'bijoux': "boucle d'oreille", 'couleur de peau': 'noir', 'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"non",'accessoire': 'rien'},
    'will':{'genre':"homme", 'cheveux':"noir", 'yeux':"marron", 'couleur de peau':"noir",'expression': "heureuse", 'bouche': "ouverte", 'traits du visage':"barbe",'accessoire': 'rien','bijoux': "non"}
}


#Création des options des menus déroulant de base
cheveux_options = ["Couleur des cheveux"] + list(set(caracteristiques['cheveux'] for caracteristiques in personnagecelebre.values()))
yeux_options = ["Couleur des yeux"] + list(set(caracteristiques['yeux'] for caracteristiques in personnagecelebre.values()))
genre_options = ["Genre"] + list(set(caracteristiques['genre'] for caracteristiques in personnagecelebre.values()))
expression_options = ["Expression"] + list(set(caracteristiques['expression'] for caracteristiques in personnagecelebre.values()))
bouche_options = ["Bouche"] + list(set(caracteristiques['bouche'] for caracteristiques in personnagecelebre.values()))
visage_options = ["Traits du visage"] + list(set(caracteristiques['traits du visage'] for caracteristiques in personnagecelebre.values()))
peau_options = ["Couleur de peau"] + list(set(caracteristiques['couleur de peau'] for caracteristiques in personnagecelebre.values()))
accessoire_options = ["Accessoire"] + list(set(caracteristiques['accessoire'] for caracteristiques in personnagecelebre.values()))
bijoux_options = ["Bijoux"] + list(set(caracteristiques['bijoux'] for caracteristiques in personnagecelebre.values()))


#Création des menus déroulants de base
cacheveux = ttk.Combobox(fen, values=cheveux_options)
cacheveux.grid(row=2, column=6, padx=5, pady=5, sticky="ne")

cayeux = ttk.Combobox(fen, values=yeux_options)
cayeux.grid(row=2, column=7, padx=5, pady=5, sticky="ne")  

cagenre = ttk.Combobox(fen, values=genre_options)
cagenre.grid(row=2, column=6, padx=5, pady=5, sticky="e") 

caexpression = ttk.Combobox(fen, values=expression_options)
caexpression.grid(row=2, column=6, padx=5, pady=5, sticky="se") 

cabouche = ttk.Combobox(fen, values=bouche_options)
cabouche.grid(row=2, column=7, padx=5, pady=5, sticky="e")

cavisage = ttk.Combobox(fen, values=visage_options)
cavisage.grid(row=2, column=7, padx=5, pady=5, sticky="se")

capeau = ttk.Combobox(fen, values=peau_options)
capeau.grid(row=2, column=6, padx=5, pady=5,sticky="se")

caaccessoire = ttk.Combobox(fen, values=accessoire_options)
caaccessoire.grid(row=3, column=6, padx=5, pady=50,sticky="ne")

cabijoux = ttk.Combobox(fen,values=bijoux_options)
cabijoux.grid(row=3, column=7, padx=5, pady=50,sticky="ne")
##----- Définition des Fonctions -----##



    
def filtrer_personnages():
    
    """Cette fonction filtre les personnages en fonction des caractéristiques sélectionnées et 
    du personnage à deviner. Elle compare les caractéristiques de chaque personnage avec celles 
    du 'persotrouver' (personnage à trouver, choisi aléatoirement dans la fonction 'perso_a_trouver')
    et détermine quels personnages doivent être supprimés (grisés) en fonction de si la caractéristique
    choisi est une des caracteristique du personnage à trouver ou non. Ensuite, elle 
    appelle 'griser_boutons' pour effectuer l'action de griser les boutons correspondants aux 
    personnages à supprimer.
    """
    global grillef, persotrouver, cacheveux, cayeux, cagenre, caexpression, cabouche, cavisage, capeau, caaccessoire, cabijoux, rep, ouinon
    
    # Sélectionner le dictionnaire des personnages en fonction de la grille choisie
    if grillef == "Célébrité":
        persos = personnagecelebre
    elif grillef == "Disney":
        persos = personnagedisney
    elif grillef == "Manga":
        persos = personnages
    else:
        persos = {}

    # Récupérer les caractéristiques du personnage à deviner à partir du dictionnaire des personnages sélectionné
    persotrouver_caracs = persos[persotrouver]

    # Récupérer les valeurs sélectionnées dans les combobox
    cheveux = cacheveux.get()
    yeux = cayeux.get()
    genre = cagenre.get()
    expression = caexpression.get()
    bouche = cabouche.get()
    visage = cavisage.get()
    peau = capeau.get()
    accessoire = caaccessoire.get()
    bijoux = cabijoux.get()

    # Liste des caractéristiques et leur valeur sélectionnée Liste des caractéristiques : Les caractéristiques et leurs valeurs sélectionnées sont stockées dans un dictionnaire pour une vérification ultérieure.
    caracteristiques = {
        'cheveux': cheveux,
        'yeux': yeux,
        'genre': genre,
        'expression': expression,
        'bouche': bouche,
        'traits du visage': visage,
        'couleur de peau': peau,
        'accessoire': accessoire,
        'bijoux': bijoux
    }

    # Tableau pour stocker les personnages à supprimer
    personnages_a_supp = []

    # Vérifier chaque caractéristique sélectionnée
    '''
    Boucle sur chaque caractéristique : Pour chaque caractéristique dans le dictionnaire caracteristiques :
    Si la valeur de la caractéristique est significative (pas vide et pas une étiquette générique), alors :
    Si la caractéristique du persotrouver correspond à la valeur sélectionnée (persotrouver_caracs[caract] == valeur), ajouter à personnages_a_supp tous les personnages qui n'ont pas cette caractéristique.
    Sinon, ajouter à personnages_a_supp tous les personnages qui ont cette caractéristique.
    '''
    for caract, valeur in caracteristiques.items(): 
    #Boucle sur chaque caractéristique : Pour chaque caractéristique dans le dictionnaire caracteristiques :
        
        if valeur not in ["", "Couleur des cheveux", "Couleur des yeux", "Genre", "Expression", "Bouche", "Traits du visage", "Couleur de peau", "Accessoire", "Bijoux"]:
        #Si la valeur de la caractéristique n'est pas vide, alors :   
            
            if persotrouver_caracs[caract] == valeur:
            #Si la caractéristique du personnage à trouver correspond à la valeur sélectionnée
                #Ajouter à personnages_a_supp tous les personnages qui n'ont pas cette caractéristique.  
                rep="    Oui, le personnage a cette caractéristique    "
                personnages_a_supp.extend([nom for nom, details in persos.items() if details[caract] != valeur])
            
            else:
                #Sinon, ajouter à personnages_a_supp tous les personnages qui ont cette caractéristique.
                rep="Non, le personnage n'a pas cette caractéristique"
                personnages_a_supp.extend([nom for nom, details in persos.items() if details[caract] == valeur])
    
    #Mettre a jour le message disant si le personnage à trouver a la caractéristique séléctionnée
    ouinon.config(text=rep)
    
    print(persotrouver)
    print(personnages_a_supp)
    # Appeler la fonction pour griser les boutons des personnages à supprimer
    griser_boutons(list(set(personnages_a_supp)))  # Utiliser set pour éviter les doublons
    compteur()

def charger_images(repertoire_images):
    global buttons, nbr_essai, compteur_label
    buttons={}
    noms_images = os.listdir(repertoire_images)
    for i in range(3):
        for j in range(5):
            # Chargement de l'image
            nom_image = noms_images[i * 5 + j]
            chemin_image = os.path.join(repertoire_images, noms_images[i * 5 + j])#chemin de l'image
            image = Image.open(chemin_image)
            image = image.resize((150, 170), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            
            # Affichage de l'image dans un label
            button_i_j = Button(fen, image=photo)
            button_i_j.image = photo  # Garder une référence à l'objet image pour éviter la garbage collection
            button_i_j.grid(row=i+2, column=j, padx=5, pady=5)
            nom_personnage = os.path.splitext(nom_image)[0]
            buttons[nom_personnage] = button_i_j
    nbr_essai=6
    compteur_label.config(text=f"Essais restants : {nbr_essai}")

def griser_boutons(personnages_a_supp):
    for personnage in personnages_a_supp:
        if personnage in buttons:
            buttons[personnage].config(state=DISABLED)#Grise le bouton et ne le bloque
    if len(personnages_a_supp)==14:
        victoire()
#Fonction qui met a jour les menus déroulant            
def mise_a_jour_menu():
    global cacheveux, cayeux, cagenre, caexpression, cabouche, cavisage, capeau, caaccessoire, cabijoux
    
    #Fait disparaitre les menus
    cacheveux.grid_remove()
    cayeux.grid_remove()
    cagenre.grid_remove()
    caexpression.grid_remove()
    cabouche.grid_remove()
    cavisage.grid_remove()
    capeau.grid_remove()
    caaccessoire.grid_remove()
    cabijoux.grid_remove()
    
    #Attributs les bonne options a chacun
    cacheveux = ttk.Combobox(fen, values=cheveux_options)
    cayeux = ttk.Combobox(fen, values=yeux_options)
    cagenre = ttk.Combobox(fen, values=genre_options)
    caexpression = ttk.Combobox(fen, values=expression_options)
    cabouche = ttk.Combobox(fen, values=bouche_options)
    cavisage = ttk.Combobox(fen, values=visage_options)
    capeau = ttk.Combobox(fen, values=peau_options)
    caaccessoire = ttk.Combobox(fen, values=accessoire_options)
    cabijoux = ttk.Combobox(fen,values=bijoux_options)
    
    #Les places dans la grille
    cacheveux.grid(row=2, column=6, padx=5, pady=5, sticky="ne")
    cayeux.grid(row=2, column=7, padx=5, pady=5, sticky="ne")  
    cagenre.grid(row=2, column=6, padx=5, pady=5, sticky="e") 
    caexpression.grid(row=2, column=6, padx=5, pady=5, sticky="se") 
    cabouche.grid(row=2, column=7, padx=5, pady=5, sticky="e")
    cavisage.grid(row=2, column=7, padx=5, pady=5, sticky="se")
    capeau.grid(row=2, column=6, padx=5, pady=5,sticky="se")
    caaccessoire.grid(row=3, column=6, padx=5, pady=50,sticky="ne")
    cabijoux.grid(row=3, column=7, padx=5, pady=50,sticky="ne")
    
    #Met la première option visible
    cacheveux.current(0)
    cayeux.current(0)
    cagenre.current(0)
    caexpression.current(0)
    cabouche.current(0)
    cavisage.current(0)
    capeau.current(0)
    caaccessoire.current(0)
    cabijoux.current(0)

charger_images("Vide")       

#Lorsque le bouton "Grille Célébrité" est pressé, la grille associé s'affiche (fonction charger_images),
#les menus déroulant sont mis a jour et un personnage de la grille est selectionné aléatoirement (fonction "perso_a_trouver")
def image_C():
    global grillef, cheveux_options, yeux_options, genre_options, expression_options, bouche_options, visage_options, peau_options, accessoire_options, bijoux_options
    grillef="Célébrité" #savoir dans quelle grille sommes nous pour la fonction 'filtrer_personnages'
    perso_a_trouver("Célébrité")#selectionne un perso aléatoire
    charger_images("Célébrité")#met les bonnes images
    #liste des options des menus déroulants pour cette grille
    cheveux_options = ["Couleur des cheveux"] + list(set(caracteristiques['cheveux'] for caracteristiques in personnagecelebre.values()))
    yeux_options = ["Couleur des yeux"] + list(set(caracteristiques['yeux'] for caracteristiques in personnagecelebre.values()))
    genre_options = ["Genre"] + list(set(caracteristiques['genre'] for caracteristiques in personnagecelebre.values()))
    expression_options = ["Expression"] + list(set(caracteristiques['expression'] for caracteristiques in personnagecelebre.values()))
    bouche_options = ["Bouche"] + list(set(caracteristiques['bouche'] for caracteristiques in personnagecelebre.values()))
    visage_options = ["Traits du visage"] + list(set(caracteristiques['traits du visage'] for caracteristiques in personnagecelebre.values()))
    peau_options = ["Couleur de peau"] + list(set(caracteristiques['couleur de peau'] for caracteristiques in personnagecelebre.values()))
    accessoire_options = ["Accessoire"] + list(set(caracteristiques['accessoire'] for caracteristiques in personnagecelebre.values()))
    bijoux_options = ["Bijoux"] + list(set(caracteristiques['bijoux'] for caracteristiques in personnagecelebre.values()))
    mise_a_jour_menu()
    caexpression.grid_remove() 

#Lorsque le bouton "Grille Disney" est pressé, la grille associé s'affiche (fonction charger_images),
#les menus déroulant sont mis a jour et un personnage de la grille est selectionné aléatoirement (fonction "perso_a_trouver")
def image_D():
    global grillef, cheveux_options, yeux_options, genre_options, expression_options, bouche_options, visage_options, peau_options, accessoire_options, bijoux_options

    grillef="Disney"
    perso_a_trouver("Disney")
    charger_images("Disney")
    cheveux_options = ["Couleur des cheveux"] + list(set(caracteristiques['cheveux'] for caracteristiques in personnagedisney.values()))
    yeux_options = ["Couleur des yeux"] + list(set(caracteristiques['yeux'] for caracteristiques in personnagedisney.values()))
    genre_options = ["Genre"] + list(set(caracteristiques['genre'] for caracteristiques in personnagedisney.values()))
    expression_options = ["Expression"] + list(set(caracteristiques['expression'] for caracteristiques in personnagedisney.values()))
    bouche_options = ["Bouche"] + list(set(caracteristiques['bouche'] for caracteristiques in personnagedisney.values()))
    visage_options = ["Traits du visage"] + list(set(caracteristiques['traits du visage'] for caracteristiques in personnagedisney.values()))
    peau_options = ["Couleur de peau"] + list(set(caracteristiques['couleur de peau'] for caracteristiques in personnagedisney.values()))
    accessoire_options = ["Accessoire"] + list(set(caracteristiques['accessoire'] for caracteristiques in personnagedisney.values()))
    bijoux_options = ["Bijoux"] + list(set(caracteristiques['bijoux'] for caracteristiques in personnagedisney.values()))
    mise_a_jour_menu()
    caexpression.grid_remove()
    cavisage.grid_remove()    

#Lorsque le bouton "Grille Manga" est pressé, la grille associé s'affiche (fonction charger_images),
#les menus déroulant sont mis a jour et un personnage de la grille est selectionné aléatoirement (fonction "perso_a_trouver")
def image_M():
    global grillef, cheveux_options, yeux_options, genre_options, expression_options, bouche_options, visage_options, peau_options, accessoire_options, bijoux_options
    grillef="Manga"
    perso_a_trouver("Manga")
    charger_images("Manga")
    cheveux_options = ["Couleur des cheveux"] + list(set(caracteristiques['cheveux'] for caracteristiques in personnages.values()))
    yeux_options = ["Couleur des yeux"] + list(set(caracteristiques['yeux'] for caracteristiques in personnages.values()))
    genre_options = ["Genre"] + list(set(caracteristiques['genre'] for caracteristiques in personnages.values()))
    expression_options = ["Expression"] + list(set(caracteristiques['expression'] for caracteristiques in personnages.values()))
    bouche_options = ["Bouche"] + list(set(caracteristiques['bouche'] for caracteristiques in personnages.values()))
    visage_options = ["Traits du visage"] + list(set(caracteristiques['traits du visage'] for caracteristiques in personnages.values()))
    peau_options = ["Couleur de peau"] + list(set(caracteristiques['couleur de peau'] for caracteristiques in personnages.values()))
    accessoire_options = ["Accessoire"] + list(set(caracteristiques['accessoire'] for caracteristiques in personnages.values()))
    bijoux_options = ["Bijoux"] + list(set(caracteristiques['bijoux'] for caracteristiques in personnages.values()))
    mise_a_jour_menu()
    capeau.grid_remove()
    caaccessoire.grid_remove()
    cabijoux.grid_remove()
    
#Fonction pour démarrer une nouvelle partie
def recommencer():
    charger_images("Vide")
    cabijoux.grid()
    caaccessoire.grid()
    capeau.grid()
    caexpression.grid()
    cavisage.grid()
    nbr_essai=6
    
    button_C.config(state=NORMAL)
    button_D.config(state=NORMAL)
    button_M.config(state=NORMAL)
    bouton_recuperer.config(state=NORMAL)
    message.grid_remove()
    
#Choisis aléatoirement le personnage a trouver en fonction de la grille    
def perso_a_trouver(grille):
    global persotrouver, dico_persotrouver
    if grille == "Célébrité":
        persotrouver=random.choice(list(personnagecelebre.keys()))
        dico_persotrouver=personnagecelebre[persotrouver]
    elif grille == "Disney":
        persotrouver=random.choice(list(personnagedisney.keys()))
        dico_persotrouver=personnagedisney[persotrouver]
    elif grille == "Manga":
        persotrouver=random.choice(list(personnages.keys()))
        dico_persotrouver=personnages[persotrouver]
    compteur_label.config(text=f"Essais restants : {nbr_essai}")
    print(dico_persotrouver) 
    
#Fonction qui affiche la fenêtre des règles du jeu lorque le bouton "Règles du jeu" est pressé 
def new_fen():
    global nouv_fen
    nouv_fen=Tk()
    nouv_fen.title("Règles du jeu")
    label = Label(nouv_fen, text="Voici les règles du jeu : \n1. Le personnage est choisi aléatoirement\n2. Vous utiliserez les menus déroulants pour choisir les caractéristiques\n3. Choisir une caractéristique puis valider (seulement une par essai), les personnages qui ne seront pas concernés par la caractéristique que vous avez sélectionné deviendra grisâtre.\n4.Reproduire cette façon de jouer jusqu’à la fin du jeu\n5 Bonne chance à vous et amusez vous bien !!!")
    label.pack()  # 'pack' organise le widget dans la fenêtre
        # Lancer la boucle principale de la nouvelle fenêtre
    nouv_fen.mainloop()
    
#Fonction pour compter le nombre d'essais a chaque fois que le bouton "valider" est pressé
def compteur():
    global nbr_essai
    nbr_essai -= 1
    compteur_label.config(text=f"Essais restants : {nbr_essai}")
    button_C.config(state=DISABLED)
    button_D.config(state=DISABLED)
    button_M.config(state=DISABLED)
    if nbr_essai == 0:
        defaite()

# Fonction lorsque le joueur perd
def defaite():
    global message
    message=Label(fen, text=f"Vous avez perdu ! Le personnage était {persotrouver.capitalize()}")
    message.grid(row=4, column=6, columnspan=2)
    bouton_recuperer.config(state=DISABLED)
#Fonction lorsque le joueur gagne

def victoire():
    global message
    message=Label(fen, text=f"Vous avez gagné !")
    message.grid(row=4, column=6, columnspan=2)
    bouton_recuperer.config(state=DISABLED)
##-----Création des zones de texte-----##


##-----Création des boutons de changement de grille-----##
button_C = Button(fen, text="Grille célébrité", command=image_C)
button_C.grid(column=0, row=0, columnspan=2, sticky="ns")

button_D = Button(fen, text="Grille Disney", command=image_D)
button_D.grid(column=2, row=0, sticky="ns")

button_M = Button(fen, text="Grille Manga", command=image_M)
button_M.grid(column=3, row=0, columnspan=2, sticky="ns")

#Boutons recommencer et quitter
bouton_recommencer = Button(fen, text='Recommencer', command = recommencer)
bouton_recommencer.grid(row = 6, column = 1, padx=3, pady=3, sticky = S+W+E)
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 6, column = 2, padx=3, pady=3, sticky = S+W+E)

# Créer un bouton pour valider la selection et appeler la fonction de filtrage
bouton_recuperer = Button(fen, text="Valider", command=filtrer_personnages)
bouton_recuperer.grid(row=3, column=6, columnspan=2, padx=5, pady=5, sticky="s")

#Bouton ouvrant la fenêtre des règles du jeu
bouton_regles = Button(fen, text="Règles du jeu", command=new_fen)
bouton_regles.grid(row=0, column=7,padx=5,pady=5)

#Taille de la fenêtre et boucle finale
fen.configure(bg="#333333", padx=10, pady=10)
fen.mainloop()  
