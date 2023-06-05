"""
This file is responsible for the generation of random values to be used in the simulation.
"""
#pylint:disable=C0200,C0103,W0621

import math
import matplotlib.pyplot as plt
import pandas

class LCMclass():
    """
    Defines a LCM for use in the CLCG.
    """
    def __init__(self, Xo, m, a, c, noOfRandomNums=500):
        self.Xo = Xo
        self.m = m
        self.a = a
        self.c = c
        self.noOfRandomNums = noOfRandomNums

    def LCM(self):
        """
        Function to generate random numbers
        """
        # Initialize the seed state
        randomInts = [0] * (self.noOfRandomNums)
        randomInts[0] = self.Xo
        # Traverse to generate required
        # numbers of random numbers
        for i in range(1, self.noOfRandomNums):
            # Follow the linear congruential method
            randomInts[i] = ((randomInts[i - 1] * self.a) + self.c) % self.m
        return randomInts

def CLCG(LCM_list, noOfRandomNums):
    """
    This simulates a CLCG.
    """
    LCM_output1 = LCM_list[0].LCM()
    LCM_output2 = LCM_list[0].LCM()
    LCM_output3 = LCM_list[0].LCM()
    output_list = [0] * noOfRandomNums
    for i in range(len(LCM_output1)):
        output_list[i] = (LCM_output1[i] - LCM_output2[i] + LCM_output3[i]) % LCM_list[0].m - 1
    return output_list

def rn_generator_insp1(input_list, m1):
    """
    This generates a RN field for inspector 1.
    """
    cdf_conversion = [0] * noOfRandomNums
    randomNums = input_list
    for i in range(len(randomNums)):
        randomNums[i] = randomNums[i]/m1
    for i in range(len(randomNums)):
        cdf_conversion[i] = -((math.log(1 - randomNums[i])/(1/10.35791)))
    return cdf_conversion

# Driver Code
if __name__ == '__main__':
    # Seed value
    Xo = 1234
    # Modulus parameter
    m1 = 65536
    m2 = 32768
    m3 = 16384
    # Multiplier term
    a = 101427
    # Increment term
    c = 321
    # Number of Random numbers
    # to be generated
    noOfRandomNums = 1000
    # Function Call
    LCM1 = LCMclass(Xo,m1,a,c,noOfRandomNums)
    LCM2 = LCMclass(Xo,m2,a,c,noOfRandomNums)
    LCM3 = LCMclass(Xo,m3,a,c,noOfRandomNums)
    LCM_list = [LCM1, LCM2, LCM3]
    CLCG_list = CLCG(LCM_list, noOfRandomNums)
    output = rn_generator_insp1(CLCG_list, m1)
    # Print the generated random numbers
    for i in CLCG_list:
        x = i/m1
        print(x, end = " \n")
    df = pandas.DataFrame(output)
    ax = df.plot.hist(bins=18)
    plt.show()
