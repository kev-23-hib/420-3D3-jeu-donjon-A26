class Ennemi:
    def __init__(self, nom, hp, attaque, comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self.comportement = comportement  # "agressif", "defensif", "aleatoire", "furtif"



        def agir(self):
            return comportement.agir(self)

        def set_comportements(self):
            self.comportement = comportement

        def recevoir_degats(self, degats):
            self.hp = max(0, self.hp - degats)
        
        def est_vivant(self):
            return self.hp > 0