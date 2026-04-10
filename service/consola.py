import logging
from datetime import datetime

from archivo.leer_data import LeerData
from config.config import MU, SIGMA, FILE_PATH, LEARNING_RATE, F_LAMBDA
from data.coeficiente import Coeficiente
from service.calcula import Calcula


def consola( ) -> None:
    logging.info('begin consola')
    logging.info(f'inicio={datetime.now( ).strftime("%d/%m/%Y %H:%M:%S")}')
    c = Coeficiente(MU, SIGMA)
    ld = LeerData(FILE_PATH)
    c.load_normal_variante()
    if not ld.is_load_data():
        print('No se pudo cargar la data')
    # print( "c=\n" + str(c) + "\n" )
    # print( "ld=\n" + str(ld) + "\n" )
    cal = Calcula(c, ld, learning_rate=LEARNING_RATE, epochs=1000, f_lambda=F_LAMBDA)
    cal.entrena( )
    print( cal )
    cal.prueba( )