class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # creo el costo mínimo de los dos pasos anteriores
        paso1 = 0
        paso2 = 0

        for i in range(len(cost)):

            # Calculo costo mínimo para llegar al paso actual
            actual = cost[i] + min(paso1, paso2)

            # Actualizo variables
            paso1 = paso2
            paso2 = actual

        # Para llegar al top es posible venir desde el último o penúltimo
        # escalon
        return min(paso1, paso2)
