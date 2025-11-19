class Asset:
    """
    Représente un actif financier avec son prix unitaire et la quantité en stock.
    """
    def __init__(self, price: float, stock: int):
        """
        Initialise un nouvel actif.

        :param price: Le prix unitaire de l'actif (doit être un flottant).
        :param stock: La quantité en stock de cet actif (doit être un entier).
        """
        if price < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        if stock < 0:
            raise ValueError("Le stock ne peut pas être négatif.")

        self.price = price  # Attribut pour le prix unitaire
        self.stock = stock  # Attribut pour la quantité en stock

    def calculate_total_value(self) -> float:
        """
        Calcule la valeur totale de l'actif (prix * stock).
        """
        return self.price * self.stock

    def __str__(self):
        """
        Représentation textuelle de l'objet, utile pour l'affichage.
        """
        return f"Asset(Prix: {self.price:.2f}€, Stock: {self.stock}, Valeur Totale: {self.calculate_total_value():.2f}€)"