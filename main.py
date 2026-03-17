from data.house import House
from data.coeficiente import Coeficiente
from data.gradiente import Gradiente
from archivo.leer_data import LeerData
from service.calcula import Calcula
from config.config import SIGMA, MU, FILE_PATH, LEARNING_RATE

if __name__ == '__main__':
    c = Coeficiente( MU, SIGMA )
    ld = LeerData( FILE_PATH )
    c.load_normal_variante( )
    if not ld.is_load_data( ):
        print( 'No se pudo cargar la data' )
    print( "c=\n" + str(c) + "\n" )
    print( "ld=\n" + str(ld) + "\n" )
    cal = Calcula( c, ld, learning_rate=LEARNING_RATE, epochs=1000 )
    cal.entrena( )
    print( cal )
    cal.prueba( )



