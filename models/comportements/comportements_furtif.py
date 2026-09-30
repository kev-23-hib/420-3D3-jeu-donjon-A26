from comportement import comportements

class comportements_furtif(comportements):


    def __init__(self):
        self._tour_furtif = 0
        

    def agir(self):
        self._tour_furtif += 1
        if self._tour_furtif % 2 == 0:
            return "defend"
        else:
            return "attaque"