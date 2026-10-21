"""INTERFACES : ce que les tâches s'échangent

Rôle
    Décrire le contrat entre les tâches. Tant que ces interfaces ne changent pas,
    chaque tâche peut être écrite et testée seule, sans attendre les autres.
    Ce fichier accueillera plus tard les types de données partagés par les tâches.

Règles communes
    Les distances sont en mètres et les temps en secondes.
    Pour un pixel, u est la colonne et v est la ligne.
    Les images sont au format BGR d'OpenCV. Le nuage de points est un tableau
    (hauteur, largeur, 3) en mètres ; les mesures ratées valent NaN ou inf.

Les quatre interfaces
    détection → position 3D : observation de la bouche
        Centre (u, v) en pixels, ouverture (rapport entre la hauteur et la largeur
        de la bouche), horodatage. S'il n'y a pas de bouche : « aucune bouche ».

    position 3D → stabilité : position 3D
        Position (X, Y, Z) en mètres dans le repère de la caméra, horodatage.
        Si la mesure n'est pas fiable : « invalide ».

    stabilité → envoi au bras : cible stabilisée
        Position stabilisée, état (recherche, suivi, prêt ou perdu), horodatage.
        À l'état « recherche » : pas de position.

    envoi au bras → bras : cible dans le repère du bras
        Position dans le repère du bras, état. Format à définir avec l'équipe
        (question 3 de docs/mandat.md).
"""
