class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Ordeno los intervalos por su tiempo de finalización
        intervals.sort(key=lambda x: x[1])

        # Contador de intervalos eliminados
        eliminados = 0

        # Guardo el final del primer intervalo
        fin_actual = intervals[0][1]

        # Recorro desde el segundo intervalo
        for i in range(1, len(intervals)):

            # Inicio del intervalo actual
            inicio = intervals[i][0]

            # Fin del intervalo actual
            fin = intervals[i][1]

            # Si hay solapamiento
            if inicio < fin_actual:

                # elimino un intervalo
                eliminados += 1

            else:
                # Si no hay solapamiento actualizo el fin actual
                fin_actual = fin

        # Retorno la cantidad eliminada
        return eliminados
