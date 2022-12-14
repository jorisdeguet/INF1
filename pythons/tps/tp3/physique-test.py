import unittest

import numpy

import physique
from pythons.tps.tp3.objet import Objet


class MesTests(unittest.TestCase):

    def test_gravitePour(self):
        self.assertAlmostEqual(9.80357, physique.gravitePour(1000), delta=0.001)
        self.assertAlmostEqual(9.77593, physique.gravitePour(10000), delta=0.001)

    def test_calculate_pressure(self):
        # Test pressure at sea level
        self.assertAlmostEqual(101325, physique.pressionAtmoPourAltitude(0))
        # Test pressure at higher altitude
        self.assertTrue(physique.pressionAtmoPourAltitude(10000) > 101325)

        # Test pressure at lower altitude
        self.assertTrue(physique.pressionAtmoPourAltitude(-1000) < 101325)

        # Test pressure at tropopause altitude
        self.assertTrue(physique.pressionAtmoPourAltitude(11000) == physique.pressionAtmoPourAltitude(11000))

        # Test pressure at higher altitude above tropopause0
        self.assertTrue(physique.pressionAtmoPourAltitude(12000) < physique.pressionAtmoPourAltitude(11000))
        self.assertTrue(physique.pressionAtmoPourAltitude(9000) > physique.pressionAtmoPourAltitude(11000))



    def test_objet_bouge_no_force(self):
        o = Objet()
        o.position = numpy.array([10.0, 10.0, 10.0])
        o.vitesse = numpy.array([0.0, 0.0, 1.0])
        deltaT = 0.01
        # on boucle jusqu'à ce que l'objet se pose
        while True:
            # deltaT est 1 millisecond, vitesse vers le haut, pas de force
            o.bouge( numpy.array([1.0, 0.2, -9.0]), deltaT)
            print(o.position)
            if o.position[2] < 0.0:
                break
        print(o.position)
