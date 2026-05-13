import numpy as np
from XGBoostNode import XGBoostNode


# C'est ici qu'on construit l'arbre de décision pour les résidus
class XGBoostTree:
    def __init__(self, max_depth=3, min_samples_split=2):
        # On définit les limites de l'arbre pour pas qu'il devienne trop grand (overfitting)
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, residuals):
        # On lance la création récursive de l'arbre
        self.root = self._grow_tree(X, residuals)

    def _grow_tree(self, X, residuals, depth=0):
        n_samples, n_features = X.shape

        # Conditions d'arrêt : si c'est trop profond ou s'il n'y a plus assez de données
        if depth >= self.max_depth or n_samples < self.min_samples_split:
            # On crée une feuille qui contient la moyenne des erreurs à ce stade
            return XGBoostNode(value=np.mean(residuals))

        # On cherche la meilleure séparation possible
        best_feat, best_thresh = self._find_best_split(X, residuals)

        # Si on ne trouve pas de split intéressant, on s'arrête là
        if best_feat is None:
            return XGBoostNode(value=np.mean(residuals))

        # On sépare les données en deux groupes selon le seuil trouvé
        left_idx = X[:, best_feat] <= best_thresh
        right_idx = ~left_idx

        # Petit check pour éviter d'avoir des branches vides (ça ferait bugger l'algo)
        if np.sum(left_idx) == 0 or np.sum(right_idx) == 0:
            return XGBoostNode(value=np.mean(residuals))

        # On continue de creuser récursivement à gauche et à droite
        left = self._grow_tree(X[left_idx], residuals[left_idx], depth + 1)
        right = self._grow_tree(X[right_idx], residuals[right_idx], depth + 1)

        return XGBoostNode(feature=best_feat, threshold=best_thresh, left=left, right=right)

    def _find_best_split(self, X, residuals):
        # Fonction pour tester toutes les colonnes et tous les seuils
        best_gain = -1
        best_feat, best_thresh = None, None

        for f_idx in range(X.shape[1]):
            # On récupère toutes les valeurs uniques pour tester les coupures
            thresholds = np.unique(X[:, f_idx])
            for t in thresholds:
                mask = X[:, f_idx] <= t
                # On calcule si ce split réduit bien l'erreur (le gain)
                gain = self._variance_reduction(residuals, mask)
                if gain > best_gain:
                    best_gain = gain
                    best_feat = f_idx
                    best_thresh = t
        return best_feat, best_thresh

    def _variance_reduction(self, residuals, mask):
        # Ici on utilise la variance pour mesurer la pureté du split
        # Moins il y a de variance dans les fils, meilleur est le split
        n = len(residuals)
        n_l, n_r = np.sum(mask), np.sum(~mask)

        if n_l == 0 or n_r == 0:
            return 0

        parent_var = np.var(residuals)
        # Moyenne pondérée de la variance des deux groupes enfants
        child_var = (n_l / n) * np.var(residuals[mask]) + (n_r / n) * np.var(residuals[~mask])

        # Le but est de maximiser cette différence
        return parent_var - child_var

    def predict_row(self, x, node):
        # Fonction récursive pour parcourir l'arbre jusqu'à une feuille
        if node.value is not None:
            return node.value

        # On compare la valeur de l'étudiant avec le seuil du nœud
        if x[node.feature] <= node.threshold:
            return self.predict_row(x, node.left)
        return self.predict_row(x, node.right)