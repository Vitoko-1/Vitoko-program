#Un hombre desea saber cuanto dinero se genera por concepto de intereses
#sobre la cantidad que tiene en inversión en el banco. El decidirá reinvertir
#los intereses siempre y cuando estos excedan a $7.000, y en ese caso
#desea saber cuanto dinero tendrá finalmente en su cuenta.
cap_invertir= int(input('cuanto es tu capital a inertir'))
interes= int(input('cuanto es tu interes?:'))/100
resultado= cap_invertir * interes 
ganancia= resultado - 7000
final= cap_invertir + resultado 
if resultado > 7000:
    print('tu resultado es de',resultado)
    print('tu ganancia es de', ganancia)
    print('tu cuenta esta con',final)
else:
    print('no alcanzo wei', resultado)
    print('tu ganancia es de', ganancia)
    print('tu cuenta esta con',final)


