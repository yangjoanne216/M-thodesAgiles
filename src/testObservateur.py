from Kingdom import Prince, Princess
from Serie import Serie


if __name__ == "__main__":
    princess = Princess("Ariel")
    prince   = Prince("Eric")

    serie1 = Serie(titre="La Belle et la Bête", nb_saisons=2)
    serie2 = Serie(titre="La Petite Sirène", nb_saisons=1)
    # Ajouter une suite à serie2 au préalable :
    serie2.suite = Serie(titre="La Petite Sirène – Suite", nb_saisons=1)

    # Abonner toutes les séries à l'événement "saved" de la princesse
    princess.events.subscribe("saved", serie1)
    princess.events.subscribe("saved", serie2)

    # Sauver la princesse
    prince.savePrincess(princess)

 # Afficher ensuite l'état de chaque série pour voir celles qui ont réellement ajouté une suite
    print(serie1)  # Devrait afficher « Suite »
    print(serie2)  # Conserver la suite existante, ne pas en ajouter une autre