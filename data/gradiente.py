from data.house import House

class Gradiente( House ):

    def __init__( self ):
        super( ).__init__( )


    def update(self, house: House, n:int, error: float) -> bool:
        if n <= 0 or house is None or error is None:
            return False
        n_2 : float = 2 / n
        self.w_long += n_2 * house.w_long * error
        self.w_lat += n_2 * house.w_lat * error
        self.w_age += n_2 * house.w_age * error
        self.w_rooms += n_2 * house.w_rooms * error
        self.w_bedrooms += n_2 * house.w_bedrooms * error
        self.w_pop += n_2 * house.w_pop * error
        self.w_house += n_2 * house.w_house * error
        self.w_income += n_2 * house.w_income * error
        self.bias += n_2 * house.bias * error
        return True

    def __str__(self):
        return super( ).__str__( )