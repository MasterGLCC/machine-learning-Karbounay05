class XGBoostNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature      # Index de la caractéristique
        self.threshold = threshold  # Valeur de coupure
        self.left = left            # Enfant gauche
        self.right = right          # Enfant droit
        self.value = value          # Valeur de la feuille (prédiction)