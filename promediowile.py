import os
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')
os.system('cls')


i = 0
suma = 0
cantidad = (input('cuantas notas son:' ))
pos = cantidad.find('.')
if pos != -1:
    print('chaooooo')
else:
    if cantidad.isnumeric() == 'false':
        print('chaooooo')
    else:
        cantidad = int(cantidad)

while i < cantidad:
    nota = float(input('Nota : '+str(i+1)+' : ' ))
    if nota >= 1 and nota <= 7 :
        suma = suma + nota
        i = i + 1
    else:
        print('Reingrese la nota')   
promedio = suma / cantidad
print('promedio: ', promedio)
if promedio >= 4:
    print('felicidade papito')
else:
    print('cagaste')