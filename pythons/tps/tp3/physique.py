import math


CONSTANTE_GRAVITATIONNELLE = 9.80665 # meters per second squared
RAYON_TERRE = 6371e3

# TODO from http://curious.astro.cornell.edu/about-us/42-our-solar-system/the-earth/gravity/93-does-gravity-vary-across-the-surface-of-the-earth-intermediate
# retourne une fonction numpy qui va vers le bas ou F = masse * g
def forceDeGravite(altitude, masse, x):
    # retourne le vecteur en z
    return (0, 0, -gravitePour(altitude) * masse * x)


def gravitePour(altitude):
  # Calcul de la force de gravité en fonction de l'altitude
  gravity = CONSTANTE_GRAVITATIONNELLE * (RAYON_TERRE / (RAYON_TERRE + altitude))**2
  return gravity

# Thank you openai
def pressionAtmoPourAltitude(altitude):
    PRESSURE_AT_SEA_LEVEL = 101325                  # Constante de la pression atmosphérique en niveau de la mer
    MOLAR_MASS_OF_AIR = 0.0289644                   # Masse molaire de l'air
    TEMPERATURE_AT_SEA_LEVEL = 288.15               # Température de l'air à niveau de la mer en kelvin
    TROPOPAUSE_ALTITUDE = 11000                     # Altitude de la tropopause en mètres
    R = 8.31447                                     # Constante des gaz parfaits
    LAPSE_RATE = 0.0065                             # déclivité de la température de l'air en fonction de l'altitude
    # Constantes pour le calcul de la pression en fonction de l'altitude
    PRESSURE_EXPONENT = -CONSTANTE_GRAVITATIONNELLE * MOLAR_MASS_OF_AIR / (R * TEMPERATURE_AT_SEA_LEVEL)
    PRESSURE_ALTITUDE_SCALING = PRESSURE_AT_SEA_LEVEL * math.exp(PRESSURE_EXPONENT * altitude)
    # Calcul de la pression en fonction de l'altitude
    if altitude <= TROPOPAUSE_ALTITUDE:
        pressure = PRESSURE_ALTITUDE_SCALING
    else:
        pressure = PRESSURE_ALTITUDE_SCALING * math.pow(
            TEMPERATURE_AT_SEA_LEVEL / (TEMPERATURE_AT_SEA_LEVEL - LAPSE_RATE * (altitude - TROPOPAUSE_ALTITUDE)),
            PRESSURE_EXPONENT)

    return pressure

def calculate_air_resistance(densiteAir, vitesse, aireFrontale):
  # Constante de résistance de l'air
  AIR_RESISTANCE_CONSTANT = 0.5
  air_resistance = AIR_RESISTANCE_CONSTANT * densiteAir * vitesse**2 * aireFrontale

  return air_resistance