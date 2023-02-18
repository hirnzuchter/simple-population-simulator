import numpy as np

def simulator(arguments):
    reproductive = 0
    for i in range(len(arguments[1])):
        arguments[1][i] -= 1
        if arguments[1][i] == 3 :
            reproductive += 1
    for i in range(reproductive//2*arguments[2]//arguments[3]):
        arguments[1].append(5)
    return [arguments[0]+1, list(filter(lambda num: num != 0, arguments[1])), arguments[2], arguments[3]]