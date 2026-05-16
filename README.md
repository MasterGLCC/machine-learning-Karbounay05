# Machine Learning Projects - GLCC

## Description

Ce repository contient plusieurs mini projets de Machine Learning réalisés en Python dans le cadre des travaux pratiques du Master GLCC.

Les projets sont développés :
- soit from scratch avec NumPy,
- soit avec des bibliothèques comme scikit-learn.

L’objectif principal est de comprendre le fonctionnement des algorithmes de Machine Learning, les méthodes de prédiction et les techniques d’analyse de données.

---

# Sujet du projet

Le sujet principal de plusieurs notebooks est l’analyse de la performance des étudiants à partir de différentes variables académiques et personnelles.

Le but est de construire des modèles capables :
- de prédire la note finale,
- de classifier les étudiants,
- d’analyser les facteurs influençant la réussite,
- d’appliquer différents algorithmes de Machine Learning sur les mêmes données.

---

# Objectifs pédagogiques

Ce projet permet de comprendre :

| Objectif | Description |
|---|---|
| Régression | Prédire une valeur numérique |
| Classification | Classer des données dans plusieurs catégories |
| Clustering | Regrouper automatiquement des données similaires |
| Réduction de dimension | Simplifier les données tout en gardant l’information importante |
| Reinforcement Learning | Apprendre automatiquement à partir des actions |

---

# Algorithmes étudiés

| Domaine | Algorithmes |
|---|---|
| Régression | Régression linéaire simple, multiple, polynomiale |
| Classification | KNN, SVM, Naive Bayes, Régression logistique |
| Arbres de décision | ID3, CART, C4.5, Random Forest |
| Clustering | DBSCAN |
| Réduction de dimension | PCA |
| Boosting | XGBoost |
| Reinforcement Learning | Q-Learning |

---

# Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Langage principal |
| NumPy | Calcul scientifique |
| Pandas | Manipulation des données |
| Matplotlib | Visualisation graphique |
| Scikit-learn | Algorithmes de Machine Learning |
| Jupyter Notebook | Exécution des notebooks |

---

# Dataset utilisé

Plusieurs projets utilisent un dataset représentant les performances des étudiants.

## Variables utilisées

| Variable | Description |
|---|---|
| Heures étude | Nombre d’heures d’étude par jour |
| Sommeil | Nombre d’heures de sommeil |
| Stress | Niveau de stress |
| Participation | Participation en classe |
| Sport | Activité sportive |
| Temps écran | Temps passé sur les écrans |
| Note finale | Résultat final de l’étudiant |

---

# Exemple de données

| Heures étude | Sommeil | Stress | Participation | Sport | Temps écran | Note finale |
|---|---|---|---|---|---|---|
| 2 | 5 | 8 | 20 | 0 | 6 | 10 |
| 4 | 6 | 6 | 40 | 2 | 5 | 13 |
| 6 | 7 | 5 | 60 | 3 | 4 | 15 |
| 8 | 7 | 4 | 80 | 4 | 3 | 17 |
| 10 | 8 | 3 | 90 | 5 | 2 | 18.5 |

---

# Modèles de régression étudiés

## Régression linéaire simple

Ce modèle étudie la relation entre une seule variable et la note finale.


::contentReference[oaicite:0]{index=0}


Exemple :
- x = heures d’étude
- y = note finale

---

## Régression linéaire multiple

Ce modèle utilise plusieurs variables explicatives.

:contentReference[oaicite:1]{index=1}

Exemple :
- heures d’étude,
- sommeil,
- stress,
- participation.

---

## Régression polynomiale

Ce modèle permet de représenter des relations non linéaires.

:contentReference[oaicite:2]{index=2}

---

# Structure du repository

```bash
.
├── regressionLineaireFromScratch.ipynb
├── regressionMultipleFromScratch.ipynb
├── regressionPolynomialWithLibrary.ipynb
├── svm_session_normale.ipynb
├── dbscan_session_normale.ipynb
├── xgboostFromScratchSessionNormale.ipynb
├── pcaFromScratchSessionNormale.ipynb
├── q_learning_fonction_approximation_session_normale.ipynb
├── README.md
```

---

# Approches utilisées

| Approche | Description |
|---|---|
| From Scratch | Implémentation manuelle des algorithmes |
| Avec bibliothèque | Utilisation de scikit-learn et autres bibliothèques |

---

# Étapes générales des projets

| Étape | Description |
|---|---|
| Prétraitement | Nettoyage et préparation des données |
| Entraînement | Construction du modèle |
| Test | Évaluation des performances |
| Visualisation | Affichage des résultats |
| Prédiction | Utilisation du modèle sur de nouvelles données |

---

# Installation

Cloner le repository :

```bash
git clone https://github.com/MasterGLCC/machine-learning-Karbounay05.git
```

Entrer dans le dossier :

```bash
cd machine-learning-Karbounay05
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

# Exécution

Lancer Jupyter Notebook :

```bash
jupyter notebook
```

Puis ouvrir le notebook souhaité.

---

# Exemple de notebooks disponibles

| Notebook | Sujet |
|---|---|
| regressionLineaireFromScratch.ipynb | Régression linéaire |
| regressionMultipleFromScratch.ipynb | Régression multiple |
| regressionPolynomialWithLibrary.ipynb | Régression polynomiale |
| svm_session_normale.ipynb | SVM |
| dbscan_session_normale.ipynb | DBSCAN |
| pcaFromScratchSessionNormale.ipynb | PCA |
| xgboostFromScratchSessionNormale.ipynb | XGBoost |
| q_learning_fonction_approximation_session_normale.ipynb | Q-Learning |

---

# Auteur

Projet réalisé dans le cadre du Master GLCC.

---

# Repository GitHub

:contentReference[oaicite:3]{index=3}
