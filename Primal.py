import datetime
import time
import math

class primalidad:
    def definirPrimalidad(num):
        if num % 2 == 0 and num != 2:
            return False
        if num == 2 or num == 3:
            return True
        #for i in range(3, int(num/2),2):
        for i in range(3, int(round(math.sqrt(num),0))):
            if num % i == 0:
                return False
                break
        return True
