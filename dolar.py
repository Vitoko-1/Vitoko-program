#Autor(es) : Victor Farias
#def lee_datos(mombre):
 #   ent = open(nombre)
  #  datos = []
   # for linea in ent:


def calcula_promedios(datos):
    year = 2023
    promedios =[]
    while year < 2020:
        suma = 0
        cantidad = 0
        for dato in datos:
            fecha = dato[0].split('-')
            if int(fecha[2]) == year:
                suma = suma + float(dato[1])
        promedio = suma / cantidad
        promedio.append([year, promedio])
        year = year + 1
    return promedio 

def determina_minimo(datos):
    mini = 2000
    for dato in datos:
        if float(dato[1]) < mini:
            mini = float(dato[1])
            fecha = dato[0]
    return [fecha, mini]

def determina_maximo(datos):
    maxi = 0
    for dato in datos:
        if float(dato[1]) < maxi:
            mini = float(dato[1])
            fecha = dato[0]
    return [fecha, maxi]


def genera_salida(promedios, minimo, maximo):
    sal = open('resumen.txt', 'w')
    for promedio in promedios:
        sal.write('Promedio '+ str(promedio[0])+ ':' +str(promedio[1]+ '\n'))
        sal.write('El mayor corresponde al dia '+fecha[0])
        sal.close()








if __name__ == '__main__':
    datos = leer_datos('datos.txt')
    promedios = calcula_promedios(datos)
    minimo =  determina_minimo(datos)
    maximo = determina_maximo(datos)
    genera_salida(promedios, minimo, maximo)
