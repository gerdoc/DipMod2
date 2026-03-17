from archivo.leer_data import LeerData
from data.coeficiente import Coeficiente
from data.gradiente import Gradiente
from data.house import House
from config.config import FLAGS

class Calcula:
    def __init__(self, coeficiente: Coeficiente, leer_data: LeerData, learning_rate: float = 0.0, epochs: int = 1000,
                 flag: list = FLAGS ):
        self.__coeficiente = coeficiente
        self.__leer_data = leer_data
        self.__learning_rate = learning_rate
        self.__epochs = epochs
        self.__flag = flag

    @property
    def coeficiente(self):
        return self.__coeficiente

    @property
    def leer_data(self):
        return self.__leer_data

    @property
    def learning_rate(self):
        return self.__learning_rate

    @property
    def epochs( self ):
        return self.__epochs

    def get_House_from_data( self, data ):
        h = House()
        i: int = 0
        h.w_long = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_lat = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_age = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_rooms = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_bedrooms = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_pop = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_house = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_income = data[ i ] * self.__flag[ i ]
        i += 1
        h.w_real_price = data[ i ]
        return h

    def get_prediction( self, house: House) -> float:
        return (( house.w_long * self.__coeficiente.w_long )  +
                 ( house.w_lat * self.__coeficiente.w_lat ) +
                 ( house.w_age * self.__coeficiente.w_age ) +
                 ( house.w_rooms * self.__coeficiente.w_rooms ) +
                 ( house.w_bedrooms * self.__coeficiente.w_bedrooms ) +
                 ( house.w_pop * self.__coeficiente.w_pop ) +
                 ( house.w_house * self.__coeficiente.w_house ) +
                 ( house.w_income * self.__coeficiente.w_income ) +
                 self.__coeficiente.bias)

    def entrena( self ) -> bool:
        co : Coeficiente = self.__coeficiente
        n: int = self.__leer_data.get_train_data_n( )
        gr: Gradiente = None
        h: House = None
        total_error_cuadratico: float = 0.0
        for epoch in range( self.__epochs ):
            gr: Gradiente = Gradiente()
            total_error_cuadratico = 0.0
            for data in self.__leer_data.train_data:
                h : House = self.get_House_from_data( data )
                prediction: float = self.get_prediction( h )
                error: float = prediction - h.w_real_price
                total_error_cuadratico += error ** 2
                if not gr.update( h, n, error ):
                    return False
            if not co.update( self.__learning_rate, gr ):
                return False
            if epoch % 100 == 0:
                mse = total_error_cuadratico / n
                print( f"Época:, {epoch}, | Error Medio Cuadrático:, {mse}, | Raiz Error Medio Cuadrático:,{mse ** (1 / 2)}" )

    def prueba(self):
        total_error_cuadratico: float = 0.0
        n: int = len( self.__leer_data.test_data )
        for data in self.__leer_data.test_data:
            h : House = self.get_House_from_data( data )
            prediction: float = self.get_prediction( h )
            error: float = prediction - h.w_real_price
            total_error_cuadratico += error ** 2
        mse = total_error_cuadratico / n
        print("\n--- Resultados en el conjunto de TEST ---")
        print( f"Error Medio Cuadrático: {mse}, Raiz Error Medio Cuadrático:{mse ** (1 / 2)}" )

    def __str__(self):
        if self.__epochs <= 0:
            return  ''
        return ( ("=" * 90) + "\n Entrenamiento Finalizado\n" +
                 ("=" * 90 ) + "\nCoeficientes finales\n" +
                 f"\n{str(self.__coeficiente)}" +
                 f"\nlearning_rate: {self.__learning_rate}, epochs: {self.__epochs} \n"
                 )








