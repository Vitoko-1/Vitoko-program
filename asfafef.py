def entrada():
    fecha = input('INGRESE LA FECHA EN FORMATO DDMMAAAA: ')
    return fecha
def proceso(fecha):
    fecha = fecha[0:2]+'/'+fecha[2:4]+'/'+fecha[4:]
    return fecha
def salida(fecha):
    print(fecha)
if __name__ == '__main__':
    fecha = entrada()
    fecha = proceso(fecha)
    salida(fecha)
