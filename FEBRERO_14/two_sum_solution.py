class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        # Creo un diccionario vacío       
        numeros_vistos = {}
        
        for i, num in enumerate(nums):

            # calculo  numero que necesito pra llegar a target
            complemento = target - num
            
            if complemento in numeros_vistos:

                #si existe complemtento retorno indice completento y actual
                return [numeros_vistos[complemento], i]

            # Guardo el número actual y su índice
            numeros_vistos[num] = i
