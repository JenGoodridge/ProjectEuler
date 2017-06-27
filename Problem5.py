import math 
sumOfSq = 0
sqOfSums = 0

for i in range(0, 101):
    sqOfSums += i
  

sqOfSums *= sqOfSums 

for i in range(0, 101):
    sumOfSq += (i * i)
    
print(sqOfSums - sumOfSq)