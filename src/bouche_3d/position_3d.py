"""TÂCHE « POSITION 3D » : position 3D de la bouche

Rôle
    Obtenir la position réelle de la bouche dans l'espace (X, Y, Z, en mètres)
    à partir de la carte de profondeur de la ZED Mini et du pixel donné par la tâche
    « détection de la bouche ».
    Ce fichier accueillera aussi la lecture de la caméra (webcam ou ZED).

Reçoit
    La carte de profondeur (un point 3D pour chaque pixel) et un pixel (u, v).

Produit
    La position (X, Y, Z) en mètres dans le repère de la caméra, ou « invalide »
    si la mesure n'est pas fiable.

Prérequis
    Une ZED Mini ou un enregistrement de la ZED (fichier .svo). Le ZED SDK, qui exige
    une carte graphique NVIDIA (sur le Jetson, sa version doit correspondre à celle
    de JetPack), et son module Python pyzed.

Dépend de
    Rien pour être développée : on peut choisir un pixel à la main. L'interface
    « détection → position 3D » ne sert qu'à l'assemblage.

Transmet à
    La tâche « stabilité et états » (stabilite_etats.py), par l'interface
    « position 3D → stabilité ».

Terminée quand
    À la distance de travail, elle renvoie une position cohérente (vérifiée à la règle)
    et « invalide » plutôt qu'une valeur absurde quand la mesure est mauvaise.

À savoir
    La mesure est peu fiable dans les zones sombres, brillantes ou uniformes, comme
    l'intérieur d'une bouche ouverte : lire la distance sur les lèvres ou le contour
    du visage. On lit plusieurs pixels autour du point et on garde la valeur médiane
    (décision D3). Dans un tableau, la ligne correspond à v et la colonne à u.

Questions liées
    1, 5 et 8 de docs/mandat.md.
"""
