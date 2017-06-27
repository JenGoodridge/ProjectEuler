# Smallest positive integer that is divisble by the numbers from 1- 20 
def divisible():
    ints = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = 19 
    index = 1
    div = False
    while div == False:
        if (index * n) % 2 == 0 and (index * n) % 7 == 0 and (index * n) % 11 == 0:
            
            for i in ints:
                if (index * n) % i != 0:
                    break
                
                elif (index * n) % i == 0 and i == 20:
                    return index * n
                    
                  
        
        index += 1
    
    return n * index
    
print(divisible())