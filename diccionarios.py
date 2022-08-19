def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
   # print(mi_diccionario['llave1'])
   # print(mi_diccionario['llave2'])
   # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'argentina': 44938712,
        'brasil': 210147125,
        'colombia': 5037
    }

    for pais, poblacion in poblacion_paises.items():
        print( pais + ' tiene ' + str(poblacion) + ' habitantes' )
        #value es para datos
        #keys llaves o nombres 
    #for pais in poblacion_paises.values():
     #   print(pais)
if __name__ =='__main__':
    run()
