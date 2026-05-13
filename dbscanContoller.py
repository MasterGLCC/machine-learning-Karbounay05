import numpy as np


class DBSCAN:
    def __init__(self, eps=2.0, min_samples=3):
        # Epsilon : c'est la distance max pour dire que deux points sont potes
        self.eps = eps
        # Min_samples : combien de voisins il faut pour créer un groupe sérieux
        self.min_samples = min_samples
        self.labels = None

    def _compute_distance(self, p1, p2):
        # Calcul classique de la distance à vol d'oiseau (Euclidienne)
        return np.sqrt(np.sum((p1 - p2) ** 2))

    def _get_neighbors(self, X, target_idx):
        # On cherche tous ceux qui sont dans le cercle de rayon 'eps'
        neighbors = []
        for i in range(len(X)):
            if self._compute_distance(X[target_idx], X[i]) <= self.eps:
                neighbors.append(i)
        return neighbors

    def fit(self, X):
        n_samples = len(X)
        # -2 veut dire "pas encore visité", -1 c'est le "bruit"
        self.labels = np.full(n_samples, -2)
        cluster_id = 0

        for i in range(n_samples):
            if self.labels[i] != -2:
                continue

            neighbors = self._get_neighbors(X, i)

            if len(neighbors) < self.min_samples:
                # Trop tout seul pour l'instant, on met en "Bruit"
                self.labels[i] = -1
            else:
                # C'est un Core Point ! On lance la propagation du cluster
                self._expand_cluster(X, i, neighbors, cluster_id)
                cluster_id += 1

        return self.labels

    def _expand_cluster(self, X, core_idx, neighbors, cluster_id):
        self.labels[core_idx] = cluster_id
        queue = list(neighbors)

        idx = 0
        while idx < len(queue):
            point_idx = queue[idx]

            # Si c'était du bruit, ça devient une bordure du cluster
            if self.labels[point_idx] == -1:
                self.labels[point_idx] = cluster_id

            # Si jamais visité, on l'ajoute et on regarde ses voisins à lui
            elif self.labels[point_idx] == -2:
                self.labels[point_idx] = cluster_id
                new_neighbors = self._get_neighbors(X, point_idx)

                # Si lui aussi est dense, il aide à agrandir le groupe
                if len(new_neighbors) >= self.min_samples:
                    queue.extend(new_neighbors)
            idx += 1