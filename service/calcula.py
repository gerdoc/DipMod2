from archivo.leer_data import LeerData
from data.coeficiente import Coeficiente
from data.gradiente import Gradiente
from data.house import House
from config.config import FLAGS

class Calcula:
    def __init__(self, coeficiente: Coeficiente, leer_data: LeerData, learning_rate: float = 0.0, epochs: int = 1000,
                 flag: list = FLAGS, f_lambda: float = 0.0 ):
        self.__coeficiente = coeficiente
        self.__leer_data = leer_data
        self.__learning_rate = learning_rate
        self.__epochs = epochs
        self.__flag = flag
        self.__f_lambda = f_lambda

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


    def get_w_power_2( self, house: House) -> float:
        return (( house.w_long ** 2  ) +
                 ( house.w_lat ** 2  ) +
                 ( house.w_age ** 2  ) +
                 ( house.w_rooms ** 2  ) +
                 ( house.w_bedrooms ** 2  ) +
                 ( house.w_pop ** 2  ) +
                 ( house.w_house ** 2  ) +
                 ( house.w_income ** 2  ) )

    def entrena( self ) -> bool:
        co : Coeficiente = self.__coeficiente
        n: int = self.__leer_data.get_train_data_n( )
        for epoch in range( self.__epochs ):
            gr: Gradiente = Gradiente()
            total_error_cuadratico: float = 0.0
            total_error_bias: float = 0.0
            total_w_cuadrado: float = 0.0
            for data in self.__leer_data.train_data:
                h : House = self.get_House_from_data( data )
                total_error_cuadratico += self.get_error_cuadratico( h )
                total_error_bias += self.get_error_perdida_bias( h )
                total_w_cuadrado += self.get_w_power_2( h )
                if not gr.update( h, n, self.get_error( h ) ):
                    return False
            if not co.update( self.__learning_rate, gr ):
                return False
            if epoch % 100 == 0:
                mse: float = total_error_cuadratico / n
                fpr: float = (total_error_bias / ( 2*n ) ) + ( ( total_w_cuadrado * self.__f_lambda )/ ( 2*n ) )
                print( f"Época:, {epoch}, Error Medio Cuadrático:, {mse}, Raiz Error Medio Cuadrático:,{mse ** (1 / 2)}"+
                       f" , Función de pérdida con regularización: {fpr}" )
        return True

    def prueba(self):
        total_error_cuadratico: float = 0.0
        total_error_bias: float = 0.0
        total_w_cuadrado: float = 0.0
        n: int = len( self.__leer_data.test_data )
        for data in self.__leer_data.test_data:
            h : House = self.get_House_from_data( data )
            total_error_cuadratico += self.get_error_cuadratico( h )
            total_error_bias += self.get_error_perdida_bias( h )
            total_w_cuadrado += self.get_w_power_2( h )

        mse: float = total_error_cuadratico / n
        fpr: float = (total_error_bias / (2 * n)) + ((total_w_cuadrado * self.__f_lambda) / (2 * n))
        print("\n--- Resultados en el conjunto de TEST ---")
        print( f"Error Medio Cuadrático: {mse}, Raiz Error Medio Cuadrático:{mse ** (1 / 2)}" +
               f" , Función de pérdida con regularización: {fpr}" )

    def get_error(self, h: House ) -> float:
        return self.get_prediction( h ) - h.w_real_price

    def get_error_cuadratico(self, h: House ) -> float:
        return self.get_error( h ) ** 2

    def get_error_perdida_bias(self, h: House ) -> float:
        return ( self.__coeficiente.bias + self.get_error( h ) ) ** 2

    def __str__(self):
        if self.__epochs <= 0:
            return  ''
        return ( ("=" * 90) + "\n Entrenamiento Finalizado\n" +
                 ("=" * 90 ) + "\nCoeficientes finales\n" +
                 f"\n{str(self.__coeficiente)}" +
                 f"\nlearning_rate: {self.__learning_rate}, epochs: {self.__epochs} \n"
                 )








