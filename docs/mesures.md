# Mesures de performance

> **À propos de ce fichier**
> - **Rôle :** définir comment mesurer la qualité du module et conserver les résultats, version après version. Sans chiffres, « c'est mieux » reste une impression.
> - **Pour qui :** toute personne qui améliore le module ou doit juger sa performance.
> - **À mettre à jour :** à chaque nouvelle mesure, en ajoutant une ligne au tableau de la section 4.

## 1. Les trois mesures

| Mesure | Question à laquelle elle répond | Unité |
|---|---|---|
| Erreur de position | De combien la position trouvée s'écarte-t-elle de la position réelle ? | millimètres (mm) |
| Latence | Combien de temps faut-il pour traiter une image, de la capture à la position finale ? | millisecondes (ms) |
| Suivi perdu | Sur quelle part des images la bouche n'est-elle pas suivie alors que le visage est présent ? | pourcentage (%) |

## 2. Comment les mesurer

### Erreur de position

1. Placer une cible (un marqueur ou un visage de référence) à une position connue, mesurée à la règle.
2. Répéter à plusieurs distances et sous plusieurs angles.
3. Pour chaque position, comparer la position trouvée à la position réelle, axe par axe (X, Y, Z).
4. Résumer avec le **RMSE** (erreur quadratique moyenne) de chaque axe. C'est l'erreur typique, exprimée en mm.

Mesurer chaque étape séparément (détection sur image, profondeur, changement de repère). On sait ainsi laquelle domine l'erreur avant de chercher à l'améliorer.

### Latence

Mesurer le temps de traitement par image, sur le Jetson. Noter :
- la moyenne ;
- le **p95** (95 % des images sont traitées plus vite que cette valeur) ;
- le maximum.

Les chiffres obtenus sur un PC ne s'appliquent pas au Jetson, qui est moins rapide.

### Suivi perdu

Sur une séquence où un visage est présent du début à la fin, compter la part des images dont l'état est « perdu » ou « recherche ».

## 3. Règles

- Toujours indiquer la plateforme (PC ou Jetson) et les réglages utilisés.
- Ne changer qu'une seule chose entre deux versions, pour savoir ce qui a produit la différence.
- Ne jamais supprimer les anciennes lignes : elles montrent la progression.

## 4. Tableau des résultats

| Version | Date | Plateforme | Erreur X / Y / Z (mm) | Latence moyenne / p95 (ms) | Suivi perdu (%) | Réglages utilisés | Remarque |
|---|---|---|---|---|---|---|---|
| Aucune mesure pour l'instant | | | | | | | |

## 5. Objectifs à atteindre

À définir avec l'équipe : erreur maximale tolérée, latence maximale, part de suivi perdu tolérée. Valeurs à confirmer (voir « Critères d'acceptation » dans `mandat.md`).
