op=-1

suma_c_q=0
suma_c_g=0
suma_s_q=0
suma_s_g=0
suma_s_l=0

consumo_energia = {
 'Coca Codo Sinclair': {
 'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
 'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
 },
 'Sopladora': {
 'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
 'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
 'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}

def menu():
    print('<1> Total de Megavatios en Planta y Ciudad' )
    print('<2> Total de Energia por Ciudad')
    print('<3> Dinero Recaudado por Region')
    print('<4> salir')

menu ()
while op != 0:
    op = int(input("ingrese una opcion: "))
    if op==4:
        break
    elif op==1:
        nombre_planta=(input("Ingrese una planta (Coca Codo Sinclair/Sopladora): "))
        nombre_ciudad=(input("Ingrese una ciudad (Guayaquil/Quito/Loja): "))
        if nombre_planta=="Coca Codo Sinclair":
            if nombre_ciudad=="Quito":
                for i in range(12):
                    suma_c_q+=consumo_energia['Coca Codo Sinclair']['Quito']['consumos'][i]
                print("Total de consumo: ", suma_c_q)
            elif nombre_ciudad=="Guayaquil":
                for i in range(12):
                    suma_c_g+=consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'][i]
                print("Total de consumo: ", suma_c_g)
            else:
                print("Error de digitación")
        elif nombre_planta=="Sopladora":
            if nombre_ciudad=="Guayaquil":
                for i in range(12):
                    suma_s_g+=consumo_energia['Sopladora']['Guayaquil']['consumos'][i]
                print("Total de consumo: ", suma_s_g)   
            elif nombre_ciudad=="Quito":
                for i in range(12):
                    suma_s_q+=consumo_energia['Sopladora']['Quito']['consumos'][i]
                print("Total de consumo: ", suma_s_q)
            elif nombre_ciudad=="Loja":
                for i in range(12):
                    suma_s_l+=consumo_energia['Sopladora']['Loja']['consumos'][i]
                print("Total de consumo: ", suma_s_l)
            else:
                print("Error de digitación")
        else:
            print("Error de digitación")
        menu()
    elif op==2:
        nombre_ciudad=(input("Ingrese una ciudad (Guayaquil/Quito/Loja/Tena/Nueva loja): "))
        if nombre_ciudad=="Guayaquil":
            for i in range(12):
                suma_c_g+=consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'][i]
            print("Cantidad total de megavatios recibidos por Coca Codo Sinclair: ", suma_c_g)
            for i in range(12):
                suma_s_g+=consumo_energia['Sopladora']['Guayaquil']['consumos'][i]
            print("Cantidad total de megavatios recibidos por Sopladora: ", suma_s_g)
        elif nombre_ciudad=="Quito":
            for i in range(12):
                suma_c_q+=consumo_energia['Coca Codo Sinclair']['Quito']['consumos'][i]
            print("Cantidad total de megavatios recibidos por Coca Codo Sinclair: ", suma_c_q)
            for i in range(12):
                suma_s_q+=consumo_energia['Sopladora']['Quito']['consumos'][i]
            print("Cantidad total de megavatios recibidos por Sopladora: ", suma_s_q)
        elif nombre_ciudad=="Loja":
            for i in range(12):
                suma_s_l+=consumo_energia['Sopladora']['Loja']['consumos'][i]
            print("Cantidad total de megavatios recibidos por Sopladora: ", suma_s_l)
        else:
            print("Esta ciudad no es alimentada energéticamente por ninguna de las dos plantas")
        menu()
    elif op==3:
        región=(input("Ingrese una región (Costa/Sierra/Oriente): "))
        if región=="Costa":
            print"Total Recaudado en la Región: $", (consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'] * sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'])) + (consumo_energia['Sopladora']['Guayaquil']['tarifa']* sum(consumo_energia['Sopladora']['Guayaquil']['consumos'])))
        elif región=="Sierra":
            print("Total Recaudado en la Región: $", (consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']*sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos'])) + (consumo_energia['Sopladora']['Quito']['tarifa']*sum(consumo_energia['Sopladora']['Quito']['consumos']))+(consumo_energia['Sopladora']['Loja']['tarifa']*sum(consumo_energia['Sopladora']['Loja']['consumos'])))
        elif región=="Oriente":
            print("Ambas plantas no recaudan dinero en esta región")
        else:
            print("Escriba de forma correcta el enunciado")
        menu()
