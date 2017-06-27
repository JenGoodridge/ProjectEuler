beginningFib = [1, 1]
def iterativeFib():
    index = 1
    x = 0
    while x < 4000000 :
        x = beginningFib[index - 1] + beginningFib[index]
        beginningFib.append(x)
        print(x)
        index += 1
    
    summ = 0
    for integer in beginningFib:
        if integer % 2 == 0 and integer < 4000000:
            summ += integer
    print(summ)

iterativeFib()
        
