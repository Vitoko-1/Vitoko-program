def lectura_datos(archivo):
    ent = open(archivo) 
    Datos = []
    for linea in ent:
        linea = linea.rstrip("\n")
        lista = linea.split(',')
        Datos.append(lista)
    ent.close()
    return Datos

def funcion_a(datos):
    region =[]
    muertes = []
    for aves_muertes_region in datos:
        region = aves_muertes_region [3]
        muertes = int(aves_muertes_region[7])
        region.set
        total = region + muertes
        total = [total]
    

       
    return total



if __name__ == '__main__':
    datos = lectura_datos('aves.txt')
    ola = funcion_a(datos)
    print (ola)