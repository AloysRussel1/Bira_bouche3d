"""TÂCHE « POSITION 3D » : position 3D de la bouche

Rôle
    Calculer la position réelle de la bouche dans l'espace (X, Y, Z, en mètres)
    à partir du nuage de points de la ZED Mini et du pixel de la bouche.
    Ce fichier contient seulement le calcul : il ne lit pas la caméra.
    La lecture de la caméra (webcam ou ZED) est faite dans camera.py.

Reçoit
    - Le nuage de points : un tableau NumPy de forme (hauteur, largeur, 3) qui donne
      X, Y, Z en mètres pour chaque pixel. Les mesures ratées valent NaN ou inf.
    - Le pixel de la bouche (u, v) : u = colonne, v = ligne.

Produit
    La position (X, Y, Z) en mètres dans le repère de la caméra
    (X vers la droite, Y vers le bas, Z vers l'avant),
    ou « invalide » (None) si la mesure n'est pas fiable.

Méthode
    1. Prendre une petite fenêtre de pixels autour de (u, v), sans sortir de l'image.
    2. Garder seulement les points valides (ni NaN ni inf).
    3. S'il y a trop peu de points valides : « invalide ».
    4. Sinon, prendre la médiane de X, de Y et de Z (décision D3).
    5. Si Z est hors de la plage de travail plausible : « invalide ».

Prérequis
    Pour développer et tester le calcul : seulement NumPy, avec des nuages inventés.
    Pour l'utiliser avec la vraie caméra : la ZED Mini (ou un fichier .svo), le ZED SDK
    et son module Python pyzed, qui exigent une carte graphique NVIDIA.

Dépend de
    Rien pour être développée : le pixel peut être choisi à la main.
    L'interface « détection → position 3D » ne sert qu'à l'assemblage.

Transmet à
    La tâche « stabilité et états » (stabilite_etats.py), par l'interface
    « position 3D → stabilité ».

Terminée quand
    - Les tests passent sur des nuages inventés : valeurs normales, point aberrant,
      fenêtre vide (NaN), pixel au bord de l'image, distance hors plage.
    - Avec la ZED, à la distance de travail, la position est cohérente avec une mesure
      à la règle, et le résultat est « invalide » plutôt qu'absurde quand la mesure
      est mauvaise.

À savoir
    La mesure est peu fiable dans les zones sombres, brillantes ou uniformes, comme
    l'intérieur d'une bouche ouverte : mieux vaut lire sur les lèvres ou le contour
    du visage. Dans un tableau NumPy, l'indice de ligne est v et celui de colonne est u :
    nuage[v, u].

Réglages à choisir (puis noter dans docs/decisions.md)
    Taille de la fenêtre, part minimale de points valides, plage de Z plausible.

Questions liées
    1, 5 et 8 de docs/mandat.md.
"""