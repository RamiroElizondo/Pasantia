"""lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))

if lado1 < 0 or lado2 < 0 or lado3 < 0:
    print('valores invalidos')
else:
    hipotenusa = 0
    cateto1 = 0
    cateto2 = 0
    if lado1 > hipotenusa:
        hipotenusa = lado1
        cateto1 = lado2
        cateto2 = lado3
    if lado2 > hipotenusa:
        hipotenusa = lado2
        cateto1 = lado1
        cateto2= lado3
    if lado3 > hipotenusa:
        hipotenusa = lado3
        cateto1= lado1
        cateto2 = lado2

    print(hipotenusa)
    hipotenusa = hipotenusa ** 2
    suma = cateto1 ** 2 + cateto2 ** 2

    print(hipotenusa)
    print(suma)lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))

if lado1 < 0 or lado2 < 0 or lado3 < 0:
    print('valores invalidos')
else:
    hipotenusa = 0
    cateto1 = 0
    cateto2 = 0
    if lado1 > hipotenusa:
        hipotenusa = lado1
        cateto1 = lado2
        cateto2 = lado3
    if lado2 > hipotenusa:
        hipotenusa = lado2
        cateto1 = lado1
        cateto2= lado3
    if lado3 > hipotenusa:
        hipotenusa = lado3
        cateto1= lado1
        cateto2 = lado2

    print(hipotenusa)
    hipotenusa = hipotenusa ** 2
    suma = cateto1 ** 2 + cateto2 ** 2

    print(hipotenusa)
    print(suma)


    if hipotenusa == suma:
        print('El triangulo es Rectangulo')
    else:
        print('NO ES RECTANGULO')


    if hipotenusa == suma:
        print('El triangulo es Rectangulo')
    else:
        print('NO ES RECTANGULO')"""



colores = {
'az':"Verde",
'zr':"Violeta",
'ar':"Naranja",
'za':"Verde",
'rz':"Violeta",
'ra':"Naranja",
}

valor = input("Ingrese colores: ")

if valor in colores:
    print(colores[valor])