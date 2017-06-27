def multiplesOfThreeAndFive(number):
    sumOfMultiples = 0
    for num in range(0, number):
        if num % 3 == 0 or num % 5 == 0:
            sumOfMultiples += num
    print(sumOfMultiples)
    
multiplesOfThreeAndFive(1000)
