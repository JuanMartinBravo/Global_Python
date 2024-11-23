class Detector:
    def __init__(self):     #Deja inicializado  el metodo para usarlo mas adelante.
        pass

    def detectar_mutantes(self, matriz):    # Combina tres métodos específicos para detectar mutantes horizontal, vertical y diagonal.
        return any([
            self._detectar_horizontal(matriz),
            self._detectar_vertical(matriz),
            self._detectar_diagonal(matriz)
        ])

    def _detectar_horizontal(self, matriz):
        for fila in matriz:
            if self._tiene_secuencia(fila):      # Verifica si hay 4 bases consecutivas.
                return True
        return False

    def _detectar_vertical(self, matriz):
        for col in range(len(matriz[0])):
            columna = ''.join(fila[col] for fila in matriz)   # Construye la columna como una cadena.
            if self._tiene_secuencia(columna): #Verifica si hay 4 bases consecutivas
                return True
        return False

    def _detectar_diagonal(self, matriz):
        def diagonales(matriz):
            diagonales = []
            for diag in range(-len(matriz) + 1, len(matriz[0])):  # Obtiene todas las diagonales principales y secundarias de la matriz.
                diagonales.append(''.join([matriz[i][i + diag] for i in range(len(matriz)) if 0 <= i + diag < len(matriz[0])]))
            return diagonales

        for diagonal in diagonales(matriz):
            if self._tiene_secuencia(diagonal):
                return True
        return False

    @staticmethod    # Revisa si hay alguna base repetida 4 veces consecutivamente.
    def _tiene_secuencia(cadena):   
        for base in "ATCG":
            if base * 4 in cadena:
                return True
        return False


class Mutador:
    def __init__(self, base_nitrogenada):
        self.base_nitrogenada = base_nitrogenada   # Define la base que se usará para mutar.

    def crear_mutante(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class Radiacion(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)     # Llama al constructor de la clase padre.

    def crear_mutante(self, matriz, posicion_inicial, orientacion):
        try:
            fila, columna = posicion_inicial
            if orientacion == "H":
                matriz[fila] = (
                    matriz[fila][columna] +
                    self.base_nitrogenada * 4 +
                    matriz[fila][columna + 4]
                )
            elif orientacion == "V":
                for i in range(4):
                    matriz[fila + i] = (
                        matriz[fila + i][columna] +
                        self.base_nitrogenada +
                        matriz[fila + i][columna + 1]
                    )
            else:
                raise ValueError("Orientación no válida. Use 'H' o 'V'.")
        except (IndexError, ValueError) as e:
            print(f"Error al crear mutante: {e}")
        return matriz


class Virus(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)    # Llama al constructor de la clase padre.

    def crear_mutante(self, matriz, posicion_inicial):
        try:
            fila, columna = posicion_inicial
            for i in range(4):
                matriz[fila + i] = (
                    matriz[fila + i][columna + i] +
                    self.base_nitrogenada +
                    matriz[fila + i][columna + i + 1]
                )
        except IndexError as e:
            print(f"Error al crear mutante: {e}")
        return matriz


class Sanador:
    def __init__(self):
        self.detector = Detector()   # Usa la clase Detector para verificar mutaciones.
  
    def sanar_mutantes(self, matriz):
        import random
        if self.detector.detectar_mutantes(matriz):
            bases = "ATCG"
            return [''.join(random.choices(bases, k=len(matriz[0]))) for _ in range(len(matriz))]
        return matriz   # Devuelve la matriz original si no hay mutaciones.