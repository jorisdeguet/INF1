

class Objet:
    position: (float, float, float)     # coordonnées 3D de l'objet en mètre
    vitesse: (float, float, float)      # composantes du vecteur vitesse en mètre par seconde
    masse: float                        # masse en kilogramme
    aireFrontale: float                 # en mètre carré

    def bouge(self, forces=(float, float, float), deltaT=float):
        # change position base sur la vitesse et le bilan de force
        print("TODO")
        # forces changent le vecteur vitesse
        self.vitesse = self.vitesse + forces*deltaT
        # vecteur vitesse change la position
        self.position = self.position + self.vitesse/deltaT