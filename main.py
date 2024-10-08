from Tren import Tren
from Vagon  import Vagon
from pasajero import Pasajero
from boleto import Boleto
import time

menu = str(input("desea ver las opciones? "))


def main():
    tren = Tren(paradas=["Estación 1", "Estación 2", "Estación 3"])
    
    
    for i in range(1, 4):  
        tren.agregar_vagon(Vagon(i))
    
    while menu.lower() == "si":
        print("Menú de opciones:")
        print("1. Subir pasajero")
        print("2. Bajar pasajero")
        print("3. Listar pasajeros")
        print("4. Contar pasajeros por género")
        print("5. Buscar pasajero")
        print("6. Ordenar pasajeros por edad")
        print("7. Calcular total pagado")
        print("8. Mostrar estadísticas")
        
        
        opcion = input("Selecciona una opción con el numero:  ")
        
        if opcion == "1":

            nombre = str(input("Ingrese el nombre: "))
            edad = int(input("Ingrese la edad: "))
            if edad < 18:
                print("usted es un adolecente y el valor del boleto sera de $4000")
            elif edad < 9:
                print("usted es un infante y el valor del boleto sera de $2000")  
            else:
                print("usted es un adulto y el valor de su boleto sera de $6000")      
            genero = str(input("Ingrese su genero: "))
            numero_vagon = int(input("Numero de vagon: "))
            numero_silla = int(input("Numero de su silla: "))
            tipo_boleto =  print("sutipo es su boleto es: ")
            boleto = Boleto(numero_vagon, numero_silla, tipo_boleto)
            pasajero = Pasajero(nombre, edad, genero, boleto)
            print("espere....")
            time.sleep(2)
            print("el pasajero subio con exito")
            time.sleep(2)
            Tren.subir_pasajero
           
        
        elif opcion == "2":
            numero_silla = int(input("cual es la silla?: "))
            pasar = str(input("cual es el nombre del pasajero?: "))
            time.sleep(2)
            Tren.bajar_pasajero
            time.sleep(2)
            print("por favor espere....")
            time.sleep(2)
            print("el pasajero a bajado con exito")
            time.sleep(2)
            print("la silla quedo libre....")
        
        elif opcion == "3":
            pasajeros = tren.listar_pasajeros()
            for pasajero in pasajeros:
                print(f"Nombre: {pasajero.nombre}, Edad: {pasajero.edad}, Género: {pasajero.genero}, Asiento: {pasajero.boleto.get_numero_asiento()}")
        
        elif opcion == "4":
            conteo = tren.contar_pasajeros_por_genero()
            print(f"Hombres: {conteo['M']}, Mujeres: {conteo['F']}")
        
        elif opcion == "5":
            nombre = input("Nombre del pasajero a buscar: ")
            pasajero = tren.buscar_pasajero(nombre)
            if pasajero:
                print(f"Nombre: {pasajero.nombre}, Edad: {pasajero.edad}, Género: {pasajero.genero}, Asiento: {pasajero.boleto.get_numero_asiento()}")
            else:
                print("Pasajero no encontrado.")
        
        elif opcion == "6":
            pasajeros = tren.ordenar_pasajeros_por_edad()
            for pasajero in pasajeros:
                print(f"Nombre: {pasajero.nombre}, Edad: {pasajero.edad}, Género: {pasajero.genero}, Asiento: {pasajero.boleto.get_numero_asiento()}")
        
        elif opcion == "7":
            total = tren.calcular_total_pagado()
            print(f"Total pagado: {total}")
        
        elif opcion == "8":
            tren.mostrar_estadisticas()
        
        
        else:
            print("Opcion no válida, intenta de nuevo.")
        break
# if __name__ == "__main__":
#     main()
