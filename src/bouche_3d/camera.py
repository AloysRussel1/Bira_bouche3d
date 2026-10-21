"""CAMÉRA : lecture des images et de la profondeur

Rôle
    Fournir aux autres fichiers les images de la caméra, et le nuage de points quand
    la caméra est une ZED. Toutes les sources s'utilisent de la même façon :
    - une webcam (pour développer la détection sans ZED) ;
    - la ZED Mini en direct ;
    - un enregistrement de la ZED (fichier .svo), pour rejouer les mêmes images.

Reçoit
    Le choix de la source (webcam, ZED ou chemin d'un fichier .svo) et ses réglages.

Produit
    À chaque image :
    - l'image couleur (format BGR d'OpenCV) ;
    - le nuage de points (tableau NumPy de forme (hauteur, largeur, 3), X, Y, Z en mètres),
      seulement avec la ZED ; None avec une webcam ;
    - l'heure de l'image, en secondes.
    Signale aussi quand plus aucune image n'est disponible (fin du fichier, caméra débranchée).

Prérequis
    Webcam : OpenCV.
    ZED et fichier .svo : le ZED SDK et pyzed, qui exigent une carte graphique NVIDIA.
    pyzed ne doit être importé que si la ZED est utilisée, pour que la webcam fonctionne
    sur un PC sans ZED SDK.

Dépend de
    Rien dans le projet.

Transmet à
    La tâche « détection de la bouche » (l'image) et la tâche « position 3D »
    (le nuage de points), au moment de l'assemblage.

Terminée quand
    - La webcam fournit des images en direct.
    - La ZED fournit l'image et le nuage de points en mètres, et un pixel visé
      donne une distance cohérente avec une mesure à la règle.
    - Un fichier .svo se rejoue comme la caméra en direct.
    - La caméra est toujours libérée à la fin, même en cas d'erreur.

À savoir
    - Régler l'unité en mètres à l'ouverture de la ZED (coordinate_units = METER).
    - L'image de la ZED a 4 canaux (BGRA) : la convertir en BGR pour OpenCV et MediaPipe.
    - Le nuage de la ZED a 4 valeurs par pixel (X, Y, Z, couleur) : ne garder que X, Y, Z.
    - Les mesures ratées valent NaN ou inf : ne pas les corriger ici, position_3d.py s'en charge.
    - Utiliser l'image gauche de la ZED : c'est celle qui correspond au nuage de points.

Réglages à choisir (puis noter dans docs/decisions.md)
    Résolution, nombre d'images par seconde, mode de profondeur de la ZED, distance minimale.

Questions liées
    1, 5 et 8 de docs/mandat.md.
"""
