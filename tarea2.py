def lectura_datos(nombre):
   ent = open(nombre)
   datos = []
   for linea in ent:
        linea = linea.rstrip('\n') 
        lista = linea.split()
        datos.append(lista)
        ent.close()
        return datos
 

def generador_usuarios(datos):
    for nombre in datos:
        nombre = [0][0], [1]
        
    return nombre


  
  
  








if __name__ == '__main__':
   datos = lectura_datos('nombres.txt')
   usu = generador_usuarios(datos)
   grabacion_usuarios(usu)
   print(datos)
   print(usu)
