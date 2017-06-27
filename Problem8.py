import fileinput
digit = []
for line in fileinput.input():
    for char in line:
        line.strip().split(' ')
        if char != '\n':
            digit.append(int(char))


maxi = []
val = 1
maxVal = 3
for i in range(0, len(digit) - 12):
    maxi = digit[i : i + 13]
    print(maxi)
    val = 1
    for num in maxi:
        val *= num 
        print(val)
    
    if maxVal < val:
        maxVal = val


print(maxVal)

