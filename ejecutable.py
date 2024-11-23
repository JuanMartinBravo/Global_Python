from clases import Detector, Radiacion, Virus, Sanador

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

def main():
    matriz = [
        "AGATCA",
        "GATTCA",
        "CAACAT",
        "GAGCTA",
        "ATTGCG",
        "CTGTTC"
    ]

    while True:
        print("ADN actual:")
        imprimir_matriz(matriz) #Llama a al metodo imprimir_matriz, para mostrarlo por pantalla.
        print("Opciones:")
        print("1. Detectar mutaciones")
        print("2. Crear mutación (Radiación o Virus)")
        print("3. Sanar ADN")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")   #Eleccion de opciones

        if opcion == "1":     
            detector = Detector()
            if detector.detectar_mutantes(matriz):
                print("Se detectaron mutaciones.")
            else:
                print("No se detectaron mutaciones.")
        elif opcion == "2":
            tipo = input("Tipo de mutación (R para Radiación, V para Virus): ").upper()
            base = input("Base nitrogenada para la mutación (A, T, C, G): ").upper()
            fila = int(input("Fila inicial: "))
            columna = int(input("Columna inicial: "))

            if tipo == "R":
                orientacion = input("Orientación (H para Horizontal, V para Vertical): ").upper()
                radiacion = Radiacion(base)
                matriz = radiacion.crear_mutante(matriz, (fila, columna), orientacion)
            elif tipo == "V":
                virus = Virus(base)
                matriz = virus.crear_mutante(matriz, (fila, columna))
        elif opcion == "3":
            sanador = Sanador()
            matriz = sanador.sanar_mutantes(matriz)
            print("El ADN ha sido sanado.")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()                              #Es un constructo especial en Python que se utiliza para definir el punto de entrada de un programa.
                                        #Este bloque asegura que cierto código solo se ejecutará si el archivo se ejecuta directamente, 
                                        #no cuando es importado como módulo por otro archivo