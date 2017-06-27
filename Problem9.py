pythagoreanTriples = []

for a in range(3, 50):
    for b in range(3, 50):
        for c in range(3, 50):
            if a**2 + b**2 == c**2:
                pythagoreanTriples.append([a, b, c])


gold = []

for tri in pythagoreanTriples:
    x = 0
    m = 1
    while x < 1001:
        x = (m * tri[0]) + (m * tri[1]) + (m * tri[2])
        
        if x == 1000:
            gold = tri
            break
        m += 1
    
    
    if gold != [] : 
        break
ans = m * gold[0] * m * gold[1] * m * gold[2]
print(ans)

