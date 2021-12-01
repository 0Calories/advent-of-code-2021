from collections import deque

# Solution for part 1
def getDepthIncreases():
    file = open('input.txt', 'r')
    
    prevDepth = -1
    numIncreases = -1
    
    for line in file:
        depth = int(line)
        if depth > prevDepth:
            numIncreases += 1
            
        prevDepth = depth
        
    file.close()
    return numIncreases

print(getDepthIncreases())

# Solution for part 2
def getDepthWindowIncreases():
    MAX_WINDOW_SIZE = 3
    
    file = open('input.txt', 'r')

    window = deque([])
    windowSum = 0
    prevSum = 0
    numIncreases = 0
    
    for line in file:
        depth = int(line)
        
        window.append(depth)
        windowSum += depth
        
        if len(window) == MAX_WINDOW_SIZE:
            prevSum = windowSum
        elif len(window) > MAX_WINDOW_SIZE:
            windowSum -= window.popleft()
            if windowSum > prevSum: numIncreases +=1
            
            prevSum = windowSum
            
    file.close()
    return numIncreases

print(getDepthWindowIncreases())

