import random as ra

from data.gradiente import Gradiente
from data.house import House
from config.config import COLUMNS, SEED

class Coeficiente( House ):

    def __init__(self, mu: float = 0.0, sigma: float = 0.0, seed: int = SEED ):
        super( ).__init__( )
        self._mu = mu
        self._sigma = sigma
        self.__cambios = COLUMNS
        self.__seed = seed

    @property
    def mu(self):
        return self._mu

    @mu.setter
    def mu(self, mu):
        self._mu = mu

    @property
    def sigma(self):
        return self._sigma

    @sigma.setter
    def sigma(self, sigma):
        self._sigma = sigma

    def load_normal_variante(self):
        ra.seed( self.__seed )
        for atributo in super( ).__dict__:
            if atributo in self.__cambios:
                setattr(self, atributo, ra.normalvariate(mu=self._mu, sigma=self.sigma ) )


    def update(self, learning_rate: float, gradiente: Gradiente) -> bool:
        if learning_rate is None or gradiente is None:
            return False
        self._w_long -= learning_rate * gradiente.w_long
        self._w_lat -= learning_rate * gradiente.w_lat
        self._w_age -= learning_rate * gradiente.w_age
        self._w_rooms -= learning_rate * gradiente.w_rooms
        self._w_bedrooms -= learning_rate * gradiente.w_bedrooms
        self._w_pop -= learning_rate * gradiente.w_pop
        self._w_house -= learning_rate * gradiente.w_house
        self._w_income -= learning_rate * gradiente.w_income
        self._bias -= learning_rate * gradiente.bias
        return True

    def __str__(self):
        return f"{super( ).__str__( ) },\nCoeficiente(mu={self._mu}, sigma={self._sigma}, seed={self.__seed})"

