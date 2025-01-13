def verifier_plage(prompt, limite_inf, limite_sup):
    while True:
        try:
            valeur = int(input(prompt))
            if limite_inf <= valeur <= limite_sup:
                return valeur
            else:
                print(f"Erreur : la valeur n'est pas dans la plage autorisée ({limite_inf}..{limite_sup})")
        except ValueError:
            print("Erreur : mauvaise entrée, veuillez saisir à nouveau la valeur")

# Exemple d'utilisation de la fonction
limite_inf = 1
limite_sup = 100
prompt = f"Veuillez entrer une valeur entre {limite_inf} et {limite_sup}: "
valeur = verifier_plage(prompt, limite_inf, limite_sup)
print("La valeur entrée est :", valeur)
