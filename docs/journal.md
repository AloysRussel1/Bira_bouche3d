# Journal de travail

> **À propos de ce fichier**
> - **Rôle :** garder la trace, session après session, de ce qui a été fait, appris, essayé et décidé. Il permet à une autre personne de reprendre le travail sans repartir de zéro.
> - **Pour qui :** l'auteur du travail, et toute personne qui reprend le module.
> - **À mettre à jour :** à la fin de chaque session de travail, en cinq minutes. Noter aussi ce qui n'a pas marché : c'est ce qui évite de perdre du temps deux fois.

## Comment l'utiliser

- Ajouter chaque nouvelle entrée en haut de la liste (la plus récente en premier).
- Copier le modèle ci-dessous.
- Donner des chiffres quand c'est possible, et renvoyer vers `mesures.md` pour le détail.
- Renvoyer vers `decisions.md` pour les choix techniques.

## Modèle d'entrée

```
### AAAA-MM-JJ : titre court
- Auteur :
- Tâche concernée (détection de la bouche, position 3D, stabilité et états, envoi au bras, assemblage et tests, ou « général ») :
- Objectif de la session :
- Ce qui a été fait :
- Résultats (avec chiffres) :
- Ce qui n'a pas marché :
- Décisions prises (et pourquoi) :
- Prochaine étape :
```

## Entrées

### 2026-10-14 : réorganisation et préparation avant Git
- **Auteur :** membre 1
- **Tâche concernée :** général
- **Objectif de la session :** préparer le dossier pour travailler à deux.
- **Ce qui a été fait :** suppression du niveau de dossier en trop ; lettres A–E remplacées par les noms des tâches ; ajout de pyproject.toml, de tests/positions_simulees.py (en-tête), de la section « Qui fait quoi » et de la ligne « Auteur » dans le journal ; .gitignore complété. Python 3.10 installé ; environnement virtuel recréé en 3.10 ; paquet installé avec pip install -e . ; vérification complète de la structure avant publication.
- **Résultats :** `import bouche_3d` fonctionne. Aucun code fonctionnel.
- **Ce qui n'a pas marché :** Le premier venv avait été créé avec le Python de MSYS2 (commande `python`) ; supprimé et recréé avec `py -3.10`.
- **Décisions prises :** D8 (dépôt temporaire). D9 (répartition), à valider avec la binôme dimanche. D10 (Python 3.10).
- **Prochaine étape :** créer le dépôt GitHub privé et y inviter la binôme ; répartition dimanche ; prévenir le responsable Heka et envoyer les questions à l'équipe ; détection de la bouche avec la webcam.

### 2026-10-07 : découpage du projet en cinq parties
- **Partie concernée :** général
- **Objectif de la session :** diviser le projet en parties distinctes, pour travailler sur chacune séparément lors des prochaines séances. Cette séance organise le travail et ne produit pas de code.
- **Ce qui a été fait :** création d'un fichier de code par partie (A à E) et d'un fichier d'interfaces. Chaque fichier commence par un en-tête qui décrit son rôle, ce qu'il reçoit, ce qu'il produit et de quoi il dépend. Création, sur le même principe, des fichiers de tests correspondants et de deux scripts. Mise à jour du README, du mandat et du registre des décisions.
- **Résultats :** aucun code écrit. Chaque fichier ne contient que son en-tête.
- **Ce qui n'a pas marché :** rien à signaler.
- **Décisions prises :** D7 dans `decisions.md`.
- **Prochaine étape :** partie A (détection de la bouche sur webcam). Si le temps manque, partie C avec des positions simulées, qui ne demande aucun matériel. Envoyer à l'équipe les questions ouvertes de `mandat.md`.

### 2026-10-07 : cadrage et mise en place du dossier
- **Partie concernée :** général
- **Objectif de la session :** comprendre le problème et choisir l'approche avant d'écrire du code.
- **Ce qui a été fait :** lecture de l'échéancier « BIRA LOG/IA », de la fiche produit de la ZED Mini et de son guide de démarrage. Définition du principe de fonctionnement et des quatre états du suivi. Création de la structure du dossier et rédaction des documents de suivi.
- **Résultats :** aucun code écrit. Structure et documents en place.
- **Ce qui n'a pas marché :** rien à signaler.
- **Décisions prises :** voir D1 à D6 dans `decisions.md`.
- **Prochaine étape :** étape A du plan (détection de la bouche sur une webcam). Envoyer à l'équipe les questions ouvertes de `mandat.md`.
