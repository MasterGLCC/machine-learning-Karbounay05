import numpy as np
from XGBoostTree import XGBoostTree


# Classe principale pour gérer notre modèle XGBoost
class XGBoostClassifier:
    def __init__(self, n_estimators=20, learning_rate=0.1, max_depth=3):
        # On définit les hyperparamètres ici
        self.n_estimators = n_estimators  # Nombre d'arbres qu'on va créer
        self.lr = learning_rate  # Pas d'apprentissage pour pas aller trop vite
        self.max_depth = max_depth  # Profondeur max de chaque arbre
        self.trees = []  # Liste pour stocker nos futurs arbres
        self.base_pred = None  # Sera la moyenne des notes au début

    def fit(self, X, y):
        # Pour commencer, on prédit juste la moyenne de toutes les notes
        self.base_pred = np.mean(y)
        # On remplit un tableau avec cette moyenne pour démarrer
        current_preds = np.full(y.shape, self.base_pred, dtype=float)

        # Boucle pour construire les arbres un par un
        for _ in range(self.n_estimators):
            # Le coeur de l'algo : on calcule l'erreur (résidu) entre le réel et le prédit
            residuals = y - current_preds

            # On crée un nouvel arbre et on l'entraîne sur ces erreurs
            tree = XGBoostTree(max_depth=self.max_depth)
            tree.fit(X, residuals)

            # Ici on récupère les prédictions de l'arbre pour mettre à jour le score global
            # J'utilise une boucle pour chaque ligne de X
            tree_preds = np.array([tree.predict_row(x, tree.root) for x in X])

            # On ajoute la correction de l'arbre au score actuel (avec le learning rate)
            current_preds += self.lr * tree_preds

            # On n'oublie pas de garder l'arbre en mémoire
            self.trees.append(tree)

    def predict_note(self, X):
        # On repart de la prédiction de base (la moyenne du début)
        preds = np.full(X.shape[0], self.base_pred, dtype=float)

        # On passe par tous les arbres qu'on a entraînés
        for tree in self.trees:
            # On ajoute la contribution de chaque arbre pour affiner la note finale
            tree_preds = np.array([tree.predict_row(x, tree.root) for x in X])
            preds += self.lr * tree_preds

        return preds

    def get_status(self, notes):
        # Simple fonction pour décider si l'étudiant passe ou pas
        # On a fixé la barre à 10/20 comme pour nous
        return ["Réussite" if n >= 10 else "Échec" for n in notes]