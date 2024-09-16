import fonctions as f

#f.puissance( 4.2,2.3)

while True:
	a = int(input("Entrez la base (a) : "))
	b = int(input("Entrez l'exposant (b) : "))

	res = f.puissance(a, b)

	print(f"{res}")
    #except ValueError:
    	#print("Veuillez entrer un nombre valide.")
