from datetime import datetime
from typing import List, AnyStr, Dict

import pandas as pd
import pytz

FLAGS: List[int] = [1, 1, 1, 1, 1, 1, 1, 1]
EPOCHS: int = 1000
LEARNING_RATE: float = 0.0000000001
PORCENTAGE_TRAIN: float = 0.8
FILE_PATH: str = "csv/housing.csv"
COLUMNS: List[str] = ['_w_long', '_w_lat', '_w_age', '_w_rooms', '_w_bedrooms', '_w_pop', '_w_house', '_w_income',
                      '_bias']
longitude: AnyStr = 'longitude'
latitude: AnyStr = 'latitude'
housing_median_age: AnyStr = 'housing_median_age'
total_rooms: AnyStr =  'total_rooms'
total_bedrooms: AnyStr =  'total_bedrooms'
population: AnyStr =  'population'
households: AnyStr = 'households'
median_income: AnyStr =  'median_income'
median_house_value: AnyStr =  'median_house_value'
COLUMNS_FILE_ALL: List[str] = [longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, median_house_value ]
COLUMNS_FILE: List[str] = [longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income ]
SEED: int = 12345
MU: float = 0.0
SIGMA: float = 0.001
F_LAMBDA: float = 0.000001
RANDOM_STATE = 42

options: Dict[int, AnyStr] = {0: "Longitud", 1: "Latitud", 2: "Edad promedio", 3: "Total de cuartos",
                              4: "Total de recamaras", 5: "Población", 6: "Hogares",
                              7: "Ingreso promedio", 8: "Valor promedio de la vivienda"}


modelos:List[AnyStr] = ["Modelo 1 (Regresión)", "Modelo 2 (XGBoost)"]

def get_now_mexico() -> datetime:
    return datetime.now(tz=pytz.timezone('America/Mexico_City'))


def get_pd_by_list( lista:List[float]) -> pd.DataFrame:
    if lista is None or len(lista) != len(COLUMNS_FILE):
        return None
    return pd.DataFrame( [{
        COLUMNS_FILE[0]: lista[0],
        COLUMNS_FILE[1]: lista[1],
        COLUMNS_FILE[2]: lista[2],
        COLUMNS_FILE[3]: lista[3],
        COLUMNS_FILE[4]: lista[4],
        COLUMNS_FILE[5]: lista[5],
        COLUMNS_FILE[6]: lista[6],
        COLUMNS_FILE[7]: lista[7]
    }])


def get_nombre_modelo( modelo: bool ) -> AnyStr:
    return modelos[0] if modelo else modelos[1]