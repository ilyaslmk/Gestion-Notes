def verdict():
    if note < 10 :
        return 'rattrapage'
    elif note >= 10 and note < 12 :
        return 'passable'
    elif note >= 12 and note < 14 :
        return 'assez bien'
    elif note >= 14 and note < 16 :
        return 'bien'
    else :
        return 'tres bien'
classe = {}
print("bienvenue dans l'application Gestion de Notes")
while True :
    print("\n" + "="*30)
    print("1.ajouter un étudiant")
    print("2.voir la liste")
    print("3.sauvgarder dans un fichier")
    print("4.Quitter")
    print("="*30)
    choix = input("choisi votre choix (4-1) :")
    if choix == "1" :
        nom = input("Nom :")
        note = float(input("note :"))
        classe[nom] = verdict()
        print(f"{nom} a ete ajouter !")
    elif choix == "2" :
        print("\n--- Liste de la classe ---")
        print(classe)
    elif choix == "3" :
        f = open("classe_final.txt","w")
        f.write(str(classe))
        f.close()
        print("sauvgarde reussie dans 'classe_final.txt' ! ")
    elif choix == "4" :
        print(" Au revoir !")
        break
    else :
        print("choix invalide !")





    
