from collections import defaultdict

# Part 1 solution
def binaryDiagnostic():
    file = open('input.txt', 'r')
    
    gammaRate = ''
    epsilonRate = ''
    
    # Count the frequency of ones and zeroes at each bit position
    zeroesCount = defaultdict(int)
    onesCount = defaultdict(int)
    lineLength = 0
    
    for line in file:
        lineLength = len(line) - 1
        for i in range(lineLength):
            bit = line[i]
            if bit == '0':
                zeroesCount[i] += 1
            elif bit == '1':
                onesCount[i] += 1
                
    # Iterate over the dictionaries to determine the gamma and epsilon rates in binary
    for i in range(lineLength):
        if zeroesCount[i] > onesCount[i]:
            gammaRate += '0'
            epsilonRate += '1'
        else:
            gammaRate += '1'
            epsilonRate += '0'
            
    # Convert the gamma and epsilon rates to decimal and multiply for the answer
    return int(gammaRate, 2) * int(epsilonRate, 2)
    

print(binaryDiagnostic())
