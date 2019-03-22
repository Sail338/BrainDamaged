from LIFStdpLineDetect import LIF
#10x10 grid
weights = .38
#flattened array of neruons
neurons  = [LIF(0) for i in range(100)]
neuronGens = [i.doEulers() for i in neurons]

def test(inpurArr):
    for i in range(len(inpurArr)):
        for j in range(len(inpurArr[i])):
            if(inpurArr[i][j] == 0):
                neurons[i*len(inpurArr) + j].I = 0
            else:
                neurons[i*len(inpurArr) + j].I = 9.8e-2
    outputNeurons = [LIF(0) for i in range(len(inpurArr))]
    outputNeuronGens = [i.doEulers() for i in outputNeurons]
    outputCurrent = 0
    
    neuronFiringRates = [0 for i  in range(len(outputNeurons))]
    for i in range(5000):
        for k in range(len(neuronGens)):
            outputCurrent += weights * next(neuronGens[k])[1]
            outputNeurons[k//len(outputNeurons)].I += outputCurrent
        for k in range(len(outputNeurons)):
            a = next(outputNeuronGens[k])
            neuronFiringRates[k] += a[0]
    return neuronFiringRates
 
matix = [[1 if j==2 or j==0 else 0 for i in range(10) ] for j in range(10)]
print(matix)
print(test(matix))




                

