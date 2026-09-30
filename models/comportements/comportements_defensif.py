
from comportement import comportements
class comportements_defensif(comportements):
    def agir(self):
        if self.hp < self.hp_max * 0.5:
            return "defend"
        else:
            return "attaque"