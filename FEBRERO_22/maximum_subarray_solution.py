class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Inicio ambas variables con el primer número del arreglo
        max_actual = nums[0]
        max_global = nums[0]

        # Recorro el arreglo desde el segundo elemento
        for i in range(1, len(nums)):

            # Decido:
            # continuar el subarray actual
            # o comenzar uno nuevo
            max_actual = max(nums[i], max_actual + nums[i])

            # Guardo el máximo encontrado hasta ahora
            max_global = max(max_global, max_actual)

        # Retorno la suma máxima encontrada
        return max_global
