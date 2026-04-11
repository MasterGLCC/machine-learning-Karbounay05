[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jyj5d-5u)

Code Python de régression linéaire simple, multiple et polynomiale (from scratch et avec bibliothèque scikit-learn).

-------------------------------------------------------------------------------------------

# Dataset : Performance des étudiants

## Objectif

Dans ce travail, on cherche à prédire la note finale d’un étudiant sur 20 en fonction de plusieurs facteurs liés à ses habitudes (étude, sommeil, stress, etc.).

---

## Description des variables

- Heures d’étude : nombre d’heures d’étude par jour  
- Sommeil : nombre d’heures de sommeil par nuit  
- Stress : niveau de stress (entre 1 et 10)  
- Participation : participation en classe (en %)  
- Activité sportive : nombre d’heures de sport par semaine  
- Temps écran : temps passé sur les écrans (heures par jour)  
- Note finale : note obtenue par l’étudiant (/20)

---

## Données

| Heures étude | Sommeil | Stress | Participation | Sport | Temps écran | Note |
|--------------|---------|--------|--------------|-------|-------------|------|
| 2            | 5       | 8      | 20           | 0     | 6           | 10   |
| 4            | 6       | 6      | 40           | 2     | 5           | 13   |
| 6            | 7       | 5      | 60           | 3     | 4           | 15   |
| 8            | 7       | 4      | 80           | 4     | 3           | 17   |
| 10           | 8       | 3      | 90           | 5     | 2           | 18.5 |
| 3            | 4       | 9      | 30           | 0     | 7           | 11   |
| 7            | 6       | 5      | 70           | 3     | 4           | 16   |

---

# Modèles utilisés

## 1. Régression linéaire simple

On modélise la relation entre une seule variable et la note :

Note = a · Heures + b

Ce modèle permet d’étudier uniquement l’impact des heures d’étude sur la performance.

---

## 2. Régression linéaire multiple

On généralise le modèle en utilisant toutes les variables explicatives :

Note =
a₁·Heures +
a₂·Sommeil +
a₃·Stress +
a₄·Participation +
a₅·Sport +
a₆·Ecran +
b

Ce modèle suppose que chaque variable contribue de manière indépendante et linéaire à la note finale.

---

## 3. Régression polynomiale

On introduit des transformations non linéaires des variables pour capturer des relations plus complexes :

Note =
a₁·Heures +
a₂·Sommeil² +
a₃·Stress³ +
a₄·Participation⁴ +
a₅·Sport⁵ +
a₆·Ecran⁶ +
b

Ce modèle permet de représenter des effets non linéaires et des interactions plus complexes entre les variables.

---

# Implémentation

Le projet contient deux approches :

## 1. From scratch
- Utilisation de l’équation normale
- Calcul manuel des coefficients W
- Manipulation directe de NumPy

## 2. Avec scikit-learn
- Utilisation de LinearRegression
- Utilisation de PolynomialFeatures
- Optimisation automatique des paramètres

---

# Objectif pédagogique

Ce projet permet de comprendre :

- Le fonctionnement de la régression linéaire
- L’impact des variables sur une prédiction
- La différence entre modèle linéaire et non linéaire
- L’utilisation des outils de machine learning modernes
