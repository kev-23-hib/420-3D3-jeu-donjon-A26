from comportement import comportements
from random import random

class comportements_aleatoire(comportements):
    def agir(self):
        return random.choice(["attaque", "defend"])

