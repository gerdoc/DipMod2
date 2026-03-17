class House:
    def __init__(self):
        self._w_long: float = 0.0
        self._w_lat: float = 0.0
        self._w_age: float = 0.0
        self._w_rooms: float = 0.0
        self._w_bedrooms: float = 0.0
        self._w_pop: float = 0.0
        self._w_house: float = 0.0
        self._w_income: float = 0.0
        self._w_real_price: float = 0.0
        self._bias: float = 0.0

    @property
    def w_long(self) -> float:
        return self._w_long

    @w_long.setter
    def w_long(self, w_long:  float):
        self._w_long = w_long

    @property
    def w_lat(self)-> float:
        return self._w_lat

    @w_lat.setter
    def w_lat(self, w_lat :  float):
        self._w_lat = w_lat

    @property
    def w_age(self)-> float:
        return self._w_age

    @w_age.setter
    def w_age(self, w_age :  float):
        self._w_age = w_age

    @property
    def w_rooms(self)-> float:
        return self._w_rooms

    @w_rooms.setter
    def w_rooms(self, w_rooms :  float):
        self._w_rooms = w_rooms

    @property
    def w_bedrooms(self)-> float:
        return self._w_bedrooms

    @w_bedrooms.setter
    def w_bedrooms(self, w_bedrooms:  float):
        self._w_bedrooms = w_bedrooms

    @property
    def w_pop(self)-> float:
        return self._w_pop

    @w_pop.setter
    def w_pop(self, w_pop:  float):
        self._w_pop = w_pop

    @property
    def w_house(self)-> float:
        return self._w_house

    @w_house.setter
    def w_house(self, w_house:  float):
        self._w_house = w_house

    @property
    def w_income(self)-> float:
        return self._w_income

    @w_income.setter
    def w_income(self, w_income:  float):
        self._w_income = w_income

    @property
    def w_real_price(self)-> float:
        return self._w_real_price

    @w_real_price.setter
    def w_real_price(self, w_real_price:  float):
        self._w_real_price = w_real_price

    @property
    def bias(self)-> float:
        return self._bias

    @bias.setter
    def bias(self, bias:  float):
        self._bias = bias

    def __str__(self):
        return (f"House(w_long={self._w_long}, w_lat={self._w_lat}, w_age={self._w_age}, w_rooms={self._w_rooms}, " +
                f"w_bedrooms={self._w_bedrooms}, w_pop={self._w_pop}, w_house={self._w_house}, " +
                f"w_income={self._w_income}, _w_real_price={self._w_real_price}, bias={self._bias})")