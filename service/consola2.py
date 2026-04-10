import logging
from datetime import datetime

from archivo.leer_data2 import LeerData2
from regresion.modelo import Modelo
from config.config import FILE_PATH, COLUMNS_FILE, median_house_value, get_pd_by_list


def consola2( modelo1: bool=False, graficar: bool=False ) -> None:
    logging.info('begin consola')
    logging.info(f'inicio={datetime.now( ).strftime("%d/%m/%Y %H:%M:%S")}')
    ld = LeerData2(FILE_PATH, COLUMNS_FILE, median_house_value)
    if not ld.load_train_test_data( ):
        logging.error('error loading data')
        return
    logging.info('data loaded')
    mo: Modelo = Modelo(ld, modelo1=modelo1, graficar=graficar )
    if not mo.procesa_regresion( ):
        logging.error('error evaluating regression')
        return
    logging.info('regression evaluated')
    mo.prediccion( get_pd_by_list( [-122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252] ) )
    logging.info('evaluation completed')
