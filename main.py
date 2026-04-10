import argparse
import logging
from datetime import datetime
from service.consola import consola
from config.config import get_now_mexico as now_mx
from service.consola2 import consola2
from service.web import web

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S',
                        level=logging.INFO)
    logging.info('begin')
    fecha_hora: datetime = now_mx()
    logging.info(f'inicio={fecha_hora.strftime("%d/%m/%Y %H:%M:%S")}')
    parser = argparse.ArgumentParser(description='módulo dos.')
    parser.add_argument('--program', required=True, choices=[ 'consola', 'web', 'consola2' ],
                        help='Programa (consola, web, consola2)')
    parser.add_argument('--modelo', type=lambda x: str(x).lower() == 'true', default=False,
                        help='Modelo 1 (Regresión)= True, Modelo 2 (XGBoost)= False')
    parser.add_argument('--graficar', type=lambda x: str(x).lower() == 'true', default=False,
                        help='Graficar= True, No Graficar= False')
    args = parser.parse_args()
    if isinstance( args.modelo, bool ):
        modelo1: bool = args.modelo
    if isinstance( args.graficar, bool ):
        graficar: bool = args.graficar
    if args.program == 'consola':
        consola( )
    if args.program == 'consola2':
        consola2( modelo1, graficar )
    if args.program == 'web':
        web( )
    logging.info('ok')
    logging.info(f'fin={fecha_hora.now().strftime("%d/%m/%Y %H:%M:%S")}')
    logging.info('end')





