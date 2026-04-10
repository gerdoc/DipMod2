from typing import List, AnyStr, Optional

import pandas as pd
from sklearn.model_selection import train_test_split

from config.config import median_house_value, RANDOM_STATE


class LeerData2:
    def __init__(self, file_path: str, columnas: List[str], columna: AnyStr):
        self.__file_path = file_path
        self.__columnas = columnas
        self.__columna = columna
        self.__df: pd.DataFrame = None
        self.__x_train: pd.DataFrame = None
        self.__x_test: pd.DataFrame = None
        self.__y_train: pd.Series = None
        self.__y_test: pd.Series = None

    @property
    def file_path(self):
        return self.__file_path

    @property
    def df(self):
        return self.__df

    @property
    def columnas(self):
        return self.__columnas

    @property
    def columna(self):
        return self.__columna

    @property
    def x_train(self):
        return self.__x_train

    @property
    def x_test(self):
        return self.__x_test

    @property
    def y_train(self):
        return self.__y_train

    @property
    def y_test(self):
        return self.__y_test

    def load_data(self) -> bool:
        self.__df = pd.read_csv(self.__file_path).dropna()
        return self.__df is not None

    def load_data_frame_by_columnas( self ) \
            ->  tuple[Optional[pd.DataFrame], Optional[pd.DataFrame]]:
        if self.__df is None:
            if not self.load_data( ):
                return None, None
        if self.__columnas is None:
            return self.__df, self.__df[ self.__columna ]
        return self.__df[ self.__columnas ], self.__df[ self.__columna ]

    def load_train_test_data(self, test_size: float=0.2 ) -> bool:
        columnas, precio_casa = self.load_data_frame_by_columnas( )
        self.__x_train, self.__x_test, self.__y_train, self.__y_test = train_test_split(
    columnas, precio_casa, test_size=test_size, random_state=RANDOM_STATE )
        return (self.__x_train is not None and self.__x_test is not None and
                self.__y_train is not None and self.__y_test is not None)

    def __str__(self):
        if self.__df is None:
            return "No se ha cargado ninguna data"
        return self.__df.to_string( )