# Solution to Part 1
def getDepthAndPos():
    file = open('input.txt', 'r')
    
    horizontalPos = 0
    depth = 0
    
    for line in file:
        [direction, val] = line.split(' ')
        val = int(val)
        
        if direction == 'forward':
            horizontalPos += val
        elif direction == 'down':
            depth += val
        elif direction == 'up':
            depth -= val
            
    file.close()
    return horizontalPos * depth

print(getDepthAndPos())


# Solution to part 2
def getDepthAndPosV2():
    file = open('input.txt', 'r')
    
    horizontalPos = 0
    depth = 0
    aim = 0
    
    for line in file:
        [direction, val] = line.split(' ')
        val = int(val)
        
        if direction == 'forward':
            horizontalPos += val
            depth += aim * val
        elif direction == 'down':
            aim += val
        elif direction == 'up':
            aim -= val
            
    file.close()
    return horizontalPos * depth

print(getDepthAndPosV2())
