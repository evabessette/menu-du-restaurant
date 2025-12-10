# Structure de départ (Personne 1)
def main():
    print("---- MENU DU RESTAURANT ----")
    afficher_entrees()
    afficher_plats_principaux()
    afficher_desserts()
    #afficher_breuvages (personne 5 à valider)

    # Les autres ajouteront leur code ici


def afficher_entrees():
    print("---- ENTRÉES ----")
    print("1. Salade César - 8.99$")
    print("2. Soupe à l'oignon - 6.50$")
    print("3. Bruschettas maison - 7.25$")

def afficher_plats_principaux():
    print("---- PLATS PRINCIPAUX ----\n1. Poulet à l'orange \n2. Tacos \n3. Poutine")


def afficher_desserts ():
    desserts = ["1. Mousse au chocolat - 5.50$ ", "2.Mille-feuille - 6.00$", "3.Tiramisu - 6.50$"]
    for dessert in desserts:
        print (dessert)    



afficher_plats_principaux()
if __name__ == "__main__":
    main()
