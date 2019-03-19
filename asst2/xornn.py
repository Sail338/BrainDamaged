from LIF import LIF
import numpy as np
import math

weights = np.random.random(6)
wieght_sum = sum(map(lambda x:x*x,weights))

for i in range(len(weights)):
    weights[i] = weights[i]/math.sqrt(wieght_sum)



inputs = [(1, 0), (0, 1), (0, 0), (1, 1)]
inputNeuronOneGen = LIF(0)
inputNeuronTwoGen = LIF(0)
inputneuron = inputNeuronOneGen.doEulers()
inputneuro2 = inputNeuronTwoGen.doEulers()
hiInput = 9.8e-2
lowInput = 3.8e-2

xor = LIF(0)
and1 = LIF(0)
andOut = LIF(0)
xorGen = xor.doEulers()
and1gen = and1.doEulers()
andOutGen = andOut.doEulers()




def train():
    
    for k in range(3000):
        for i in inputs:
            if (i == (1, 0)):
                inputNeuronOneGen.I = hiInput
                inputNeuronTwoGen.I = lowInput
                trainingNueron = 9e-2
                trainingNueronNAND = -20e-2
                trainingNueronNAND2 = -20e-2
            elif (i == (0, 0)):
                inputNeuronOneGen.I = lowInput
                inputNeuronTwoGen.I = lowInput
                trainingNueron = -9e-2
                trainingNueronNAND = -20e-2
                trainingNueronNAND2 = -20e-2
            elif (i == (0, 1)):
                inputNeuronOneGen.I = lowInput
                inputNeuronTwoGen.I = hiInput
                trainingNueron = 9e-2
                trainingNueronNAND = -29e-2
                trainingNueronNAND2 = -20e-2
            elif (i == (1, 1)):
                inputNeuronOneGen.I = hiInput
                inputNeuronTwoGen.I = hiInput
                trainingNueron =  10e-2
                trainingNueronNAND = 30e-2
                trainingNueronNAND2 = 30e-2

            spikeTrainInputOne = 0
            spikeTrainInputTwo = 0
            spikeTrainOr = 0
            spikeTrainNand = 0
            spikeTrainOutputAnd = 0

            for k in range(500):
                    inputneuronGenResult = next(inputneuron)
           
                    didFireInputNeuronOne = inputneuronGenResult[0]
                    currentInputNeuronOne = inputneuronGenResult[1]

                    spikeTrainInputOne += didFireInputNeuronOne
                    inputneuron2GenResult = next(inputneuro2)
                    didFireInputNeuronTwo = inputneuron2GenResult[0]
                    spikeTrainInputTwo += didFireInputNeuronTwo
                    currentInputNeuronTwo = inputneuron2GenResult[1]
                    xor.I = currentInputNeuronOne * \
                       weights[0] + currentInputNeuronTwo * \
                            weights[1] + trainingNueron

                    and1.I = ((currentInputNeuronOne * \
                        weights[2]) + (currentInputNeuronTwo * \
                            weights[3])) + trainingNueronNAND
                    
                    a = next(xorGen)
                    b = next(and1gen)

                    #get cirrent for output neuron
                    andOut.I = a[1] * weights[4] + b[1] * weights[5] + trainingNueronNAND2 
                    c = next(andOutGen)
                    spikeTrainOr += a[0]
                    spikeTrainNand += b[0]
                    spikeTrainOutputAnd += c[0]


            scale = 500*.0002
            spikeTrainInputOne = scale * spikeTrainInputOne
            spikeTrainInputTwo = scale * spikeTrainInputTwo
            spikeTrainOr = scale * spikeTrainOr
            spikeTrainNand = scale * spikeTrainNand
            spikeTrainOutputAnd = scale*spikeTrainOutputAnd
            # adjust weights
    
            #dw/dt = (hebb*(ratepost*pre -w*(post))
            weights[0] += .001*(spikeTrainOr*spikeTrainInputOne - weights[0]*spikeTrainOr**2)
            weights[1] += .001*(spikeTrainOr*spikeTrainInputTwo - weights[1]*spikeTrainOr**2)
            weights[2] += .001*(spikeTrainNand*spikeTrainInputOne - weights[2]*spikeTrainNand**2)
            weights[3] += .001*(spikeTrainNand*spikeTrainInputTwo - weights[3]*spikeTrainNand**2)
            weights[4] += .001*(spikeTrainOutputAnd*spikeTrainOr - weights[4]*spikeTrainOutputAnd**2) 
            weights[5] += .001*(spikeTrainOutputAnd*spikeTrainNand - weights[5]*spikeTrainOutputAnd**2) 
         



def testOR(x, y):
    maxCurrent = 0.3
    if(x == 1 and y ==1):
        inputNeuronOne = LIF(hiInput).doEulers()
        inputNeuronTwo = LIF(hiInput).doEulers()
    if(x ==0 and y == 0):
        inputNeuronOne = LIF(lowInput).doEulers()
        inputNeuronTwo = LIF(lowInput).doEulers()
    if(x ==1 and y == 0):
        inputNeuronOne = LIF(hiInput).doEulers()
        inputNeuronTwo = LIF(lowInput).doEulers()
    if(x ==0 and y == 1):
        inputNeuronOne = LIF(lowInput).doEulers()
        inputNeuronTwo = LIF(hiInput).doEulers()
    spikeRateOr = 0
    spikeRateNand =0
    spikeRateAndFinal = 0
    orGate = LIF(0)
    nandGate = LIF(0)
    andGate = LIF(0)
    orGateGen = orGate.doEulers()
    nandGateGen = nandGate.doEulers()
    andGateGen = andGate.doEulers()
    for i in range(5000):
        currentNueronOne = next(inputNeuronOne)[1]
        currentNueronTwo = next(inputNeuronTwo)[1]
        orGate.I = currentNueronOne* weights[0] + currentNueronTwo * weights[1]
        nandGate.I = maxCurrent - (currentNueronOne * weights[2] + currentNueronTwo* weights[3])
        result = next(orGateGen)
        result2 = next(nandGateGen)
        andGate.I = weights[4] * result[1] + weights[5] * result2[1]
        result3 = next(andGateGen)
        spikeRateOr += result[0]
        spikeRateNand += result2[0]
        spikeRateAndFinal += result3[0]
    

    return spikeRateOr,spikeRateNand,spikeRateAndFinal
train()
print(testOR(0, 0))
print(testOR(1, 0))
print(testOR(0, 1))
print(testOR(1, 1))
