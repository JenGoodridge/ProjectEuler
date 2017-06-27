np = set()
mp = set()
pr = set()
for i in range(0, 200000):
    if i % 2 == 0:
        np.add(i)
    elif i % 5 == 0:
        np.add(i)
        
    elif i % 19 == 0:
        np.add(i)
    
    elif i % 7 == 0:
        np.add(i)
    
    elif i % 9 == 0:
        np.add(i)
    
    elif i % 3 == 0:
        np.add(i)

for i in range(0, 200000):
    if i not in np:
        mp.add(i)
        
for x in mp:
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            break
        
        elif i == int(x**.5) and x % i != 0:
            pr.add(x)
           
            
primes = []
for p in pr:
    primes.append(p)

primes.append(2)
primes.append(3)
primes.append(5)
primes.append(7)
primes = sorted(primes)
print(primes[9999])
print(primes)
