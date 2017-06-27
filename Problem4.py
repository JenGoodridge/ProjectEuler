# so the least product of 2 3 digit numbers is 10,000 and the largest is 998,001
import math 
def largestPalindrome():
    for n in range(998001, 10000, -1):
        if str(n) == str(n)[::-1] and Factors(n) == True:
            return n

def Factors(x):
    factors = []
    for num in range(2, int(math.sqrt(x)) + 1):
        
        if x % num == 0:
            factors.append(num)
            factors.append(x // num) 
    
    for index in range(1, len(factors), 2):
        if len(str(factors[index - 1])) == 3 and len(str(factors[index])) == 3:
            return True  
    
    return False

    
print(largestPalindrome())
print(Factors(largestPalindrome()))