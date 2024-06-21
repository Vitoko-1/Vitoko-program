milisegundo = 0
segundo = 0
minuto = 0
hora = 0

while hora < 24:
    milinas = milisegundo + 1
    milisegundo = milinas
    if milisegundo > 5000:
        milmas = segundo + 1
        segundo = milmas
        milisegundo = 0
    if segundo >= 60:
        segmas = minuto + 1
        minuto = segmas
        segundo = 0
    if minuto >= 60:
        hormas = hora + 1
        hora = hormas
        minuto = 0
    print('hor',hora,':','min',minuto,':','seg',segundo,':','miliseg', milisegundo)


