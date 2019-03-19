from LIFStdp import LIF
import numpy as np
import math


def preSynapticWeightDec(wIndex, pre, post):
    if(pre[-1] == 1):
        ptr2 = len(post)-1
        while(ptr2 > 0):
            if(post[ptr2] == 1):
                decay = -1*(len(post)-1-ptr2)*.0002
         
                weights[wIndex] -= 0.005*math.exp(decay/10e-3)
                np.clip(weights,0,1)
                break
            ptr2 -= 1


def postSynapticWeightInc(wIndex, pre, post):
    if(post[-1] == 1):
        ptr2 = len(post)-1
        while(ptr2 > 0):
            if(pre[ptr2] == 1):
                decay = -1*(len(post)-1-ptr2)*.0002
           
                weights[wIndex] += 0.0044*math.exp(decay/10e-3)
           
                    
                break
            ptr2 -= 1


weights = [0.5,0.39,0.5,0.5,0.5,0.5]
w_sum = sum(weights)
print(weights)


inputs = [(1, 0), (0, 1), (0, 0), (1, 1)]
inputNeuronOneGen = LIF(0)
inputNeuronTwoGen = LIF(0)
inputneuron = inputNeuronOneGen.doEulers()
inputneuro2 = inputNeuronTwoGen.doEulers()
hiInput = 9.8e-2
lowInput = 4.8e-2

xor = LIF(0)
and1 = LIF(0)
andOut = LIF(0)
xorGen = xor.doEulers()
and1gen = and1.doEulers()
andOutGen = andOut.doEulers()


def train():
    for z in range(10):
        for i in inputs:
            if (i == (1, 0)):
                
                inputNeuronOneGen.I = hiInput
                inputNeuronTwoGen.I = lowInput
                trainingNueron = 10e-2
                trainingNueronNAND = -14.2e-2
                trainingNueronNAND2 = -14.2e-2
            elif (i == (0, 0)):
                inputNeuronOneGen.I = lowInput
                inputNeuronTwoGen.I = lowInput
                trainingNueron = -1.1e-2
                trainingNueronNAND = -9e-2
                trainingNueronNAND2 = -9e-2
            elif (i == (0, 1)):
                inputNeuronOneGen.I = lowInput
                inputNeuronTwoGen.I = hiInput
                trainingNueron = 10e-2
                trainingNueronNAND = -14.2e-2
                trainingNueronNAND2 = -16e-2
            elif (i == (1, 1)):
                inputNeuronOneGen.I = hiInput
                inputNeuronTwoGen.I = hiInput
                trainingNueron = 1.1e-2
                trainingNueronNAND = 10e-2
                trainingNueronNAND2 = 30e-2

            spikeTrainInputOne = []
            spikeTrainInputTwo = []
            spikeTrainOr = []
            spikeTrainNand = []
            spikeTrainOutputAnd = []

            for k in range(5000):
                inputneuronGenResult = next(inputneuron)
                didFireInputNeuronOne = inputneuronGenResult[0]
                currentInputNeuronOne = inputneuronGenResult[1]
                spikeTrainInputOne.append(didFireInputNeuronOne)
                inputneuron2GenResult = next(inputneuro2)
                didFireInputNeuronTwo = inputneuron2GenResult[0]
                spikeTrainInputTwo.append(didFireInputNeuronTwo)
                currentInputNeuronTwo = inputneuron2GenResult[1]
                xor.I = currentInputNeuronOne * \
                    weights[0] + currentInputNeuronTwo * \
                    weights[1] + trainingNueron

                and1.I = ((currentInputNeuronOne *
                        weights[2]) + (currentInputNeuronTwo *
                                        weights[3])) + trainingNueronNAND
                

                a = next(xorGen)
                b = next(and1gen)

                # get cirrent for output neuron
                andOut.I = a[1] * weights[4] + b[1] * \
                    weights[5] + trainingNueronNAND2
               
                c = next(andOutGen)
                spikeTrainOr.append(a[0])
                spikeTrainNand.append(b[0])
                spikeTrainOutputAnd.append(c[0])

                preSynapticWeightDec(0, spikeTrainInputOne, spikeTrainOr)
                preSynapticWeightDec(1, spikeTrainInputTwo, spikeTrainOr)
                preSynapticWeightDec(2, spikeTrainInputOne, spikeTrainNand)
                preSynapticWeightDec(3, spikeTrainInputTwo, spikeTrainNand)
                preSynapticWeightDec(4, spikeTrainOr, spikeTrainOutputAnd)
                preSynapticWeightDec(5, spikeTrainNand, spikeTrainOutputAnd)

                postSynapticWeightInc(0, spikeTrainInputOne, spikeTrainOr)
                postSynapticWeightInc(1, spikeTrainInputTwo, spikeTrainOr)
                postSynapticWeightInc(2, spikeTrainInputOne, spikeTrainNand)
                postSynapticWeightInc(3, spikeTrainInputTwo, spikeTrainNand)
                postSynapticWeightInc(4, spikeTrainOr, spikeTrainOutputAnd)
                postSynapticWeightInc(5, spikeTrainNand, spikeTrainOutputAnd)

            # adjust weights

        # dw/dt = (hebb*(ratepost*pre -w*(post))
        # first look at first weight pair


def testOR(x, y):
    maxCurrent = 0.3
    if(x == 1 and y == 1):
        inputNeuronOne = LIF(hiInput).doEulers()
        inputNeuronTwo = LIF(hiInput).doEulers()
    if(x == 0 and y == 0):
        inputNeuronOne = LIF(lowInput).doEulers()
        inputNeuronTwo = LIF(lowInput).doEulers()
    if(x == 1 and y == 0):
        inputNeuronOne = LIF(hiInput).doEulers()
        inputNeuronTwo = LIF(lowInput).doEulers()
    if(x == 0 and y == 1):
        inputNeuronOne = LIF(lowInput).doEulers()
        inputNeuronTwo = LIF(hiInput).doEulers()
    spikeRateOr = 0
    spikeRateNand = 0
    spikeRateAndFinal = 0
    orGate = LIF(0)
    nandGate = LIF(0)
    andGate = LIF(0)
    orGateGen = orGate.doEulers()
    nandGateGen = nandGate.doEulers()
    andGateGen = andGate.doEulers()
    maxCurrent = -199
    for i in range(5000):
        currentNueronOne = next(inputNeuronOne)[1]
        currentNueronTwo = next(inputNeuronTwo)[1]
        orGate.I = currentNueronOne * \
            weights[0] + currentNueronTwo * weights[1]

        nandGate.I =  .23- (currentNueronOne *
                      weights[2] + currentNueronTwo * weights[3])
        if(nandGate.I > maxCurrent):
            maxCurrent = nandGate.I
        result = next(orGateGen)
        result2 = next(nandGateGen)
        andGate.I = weights[4] * result[1] + weights[5] * result2[1]
        result3 = next(andGateGen)
        spikeRateOr += result[0]
        spikeRateNand += result2[0]
        spikeRateAndFinal += result3[0]
    print(maxCurrent)

    return spikeRateOr, spikeRateNand, spikeRateAndFinal


train()

print(weights)
print(testOR(0, 0))
print(testOR(1, 0))
print(testOR(0, 1))
print(testOR(1, 1))
