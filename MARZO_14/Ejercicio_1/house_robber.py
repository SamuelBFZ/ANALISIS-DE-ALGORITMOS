class Solution:
    def rob(self, nums: list[int]) -> int:
        
        # Si solo existe una casa retorno su valor
        if len(nums) == 1:
            return nums[0]

        #defino máximo dinero hasta la casa anterior
        dinero_anterior = 0

        #defino máximo dinero actual calculado
        dinero_actual = 0

        # Recorro todas las casas
        for dinero in nums:

            #calculo robar esta casa o no robarla
            nuevo_total = max(dinero_actual, dinero_anterior + dinero)

            # Actualizp variables
            dinero_anterior = dinero_actual
            dinero_actual = nuevo_total

        # Retorno el máximo dinero posible
        return dinero_actual
