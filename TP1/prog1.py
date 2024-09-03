while True:
    try:
        nombre = float(input("Entrez un nombre (ou 'q' pour quitter) : "))
        if nombre == 'q':
            break
        carre = nombre * nombre
        print("Le carré de", nombre, "est", carre)
    except ValueError:
        print("Veuillez entrer un nombre valide.")