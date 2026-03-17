from typing import List, Any
from config.config import SEED, PORCENTAGE_TRAIN
import pandas as pd
import random as ra

class LeerData:
    def __init__(self, file_path: str, por_train: float = PORCENTAGE_TRAIN):
        self.__file_path = file_path
        self.__por_train = por_train
        self.__train_data = None
        self.__test_data = None
        self.__data = None
        self.__list_of_tuples = None
        self.__split_index: int = 0


    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path

    @property
    def train_data(self):
        return self.__train_data

    @property
    def test_data(self):
        return self.__test_data

    @property
    def data(self):
        return self.__data

    @property
    def len_train(self):
        return self.__len_train

    def __is_leer_data( self ) -> bool:
        self.__data = pd.read_csv( self.__file_path).dropna( )
        return self.__data is not None

    def __is_load_list_of_tuples(self) -> bool:
        if not self.__is_leer_data( ):
            return False
        self.__list_of_tuples: List[ Any ] = list( self.__data.itertuples(index=False, name=None) )
        return self.__list_of_tuples is not None and len( self.__list_of_tuples ) > 0

    def is_load_data( self ) -> bool:
        if not self.__is_load_list_of_tuples( ):
            return False
        ra.seed( SEED )
        ra.shuffle( self.__list_of_tuples )
        self.__split_index: int = int( len( self.__list_of_tuples) * self.__por_train )
        self.__train_data = self.__list_of_tuples[ : self.__split_index ]
        self.__test_data = self.__list_of_tuples[ self.__split_index : ]
        return self.__train_data is not None and self.__test_data is not None


    def get_train_data_n(self) -> int:
        return len(self.__train_data)

    def get_test_data_n(self) -> int:
        return len(self.__test_data)

    def __str__(self):
        if self.__train_data is None or self.__test_data is None:
            return "No se ha cargado ninguna data"
        return f"Total de datos:{len(self.__list_of_tuples)} Datos de entrenamiento:{len(self.__train_data)},Datos de prueba: {len(self.__test_data)}"
