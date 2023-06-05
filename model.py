"""
This file contains the configurations that generate random inputs for all the 
inspectors and workshops.
"""
import math
from random_input_generator import LCMclass, CLCG

#pylint:disable=C0103,W0621,C0200

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
#output = rn_generator_insp1(CLCG_list, m1)



def rn_generator_insp1(input_list, m1, noOfRandomNums):
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

def rn_generator_insp2_comp2(input_list, m1, noOfRandomNums):
    """
    This generates a RN field for inspector 1.
    """
    cdf_conversion = [0] * noOfRandomNums
    randomNums = input_list
    for i in range(len(randomNums)):
        randomNums[i] = randomNums[i]/m1
    for i in range(len(randomNums)):
        cdf_conversion[i] = -((math.log(1 - randomNums[i])/(1/15.53690)))
    return cdf_conversion

def rn_generator_insp2_comp3(input_list, m1, noOfRandomNums):
    """
    This generates a RN field for inspector 1.
    """
    cdf_conversion = [0] * noOfRandomNums
    randomNums = input_list
    for i in range(len(randomNums)):
        randomNums[i] = randomNums[i]/m1
    for i in range(len(randomNums)):
        cdf_conversion[i] = -((math.log(1 - randomNums[i])/(1/20.63276)))
    return cdf_conversion

def rn_generator_workshop1(input_list, m1, noOfRandomNums):
    """
    This generates a RN field for workshop 1.
    """
    cdf_conversion = [0] * noOfRandomNums
    randomNums = input_list
    for i in range(len(randomNums)):
        randomNums[i] = randomNums[i]/m1
    for i in range(len(randomNums)):
        cdf_conversion[i] = -((math.log(1 - randomNums[i])/(1/4.60441)))
    return cdf_conversion

def rn_generator_workshop2(input_list, m1, noOfRandomNums):
    """
    This generates a RN field for workshop 2.
    """
    cdf_conversion = [0] * noOfRandomNums
    randomNums = input_list
    for i in range(len(randomNums)):
        randomNums[i] = randomNums[i]/m1
    for i in range(len(randomNums)):
        cdf_conversion[i] = -((math.log(1 - randomNums[i])/(1/11.09260)))
    return cdf_conversion

def rn_generator_workshop3(input_list, m1, noOfRandomNums):
    """
    This generates a RN field for workshop 3.
    """
    cdf_conversion = [0] * noOfRandomNums
    randomNums = input_list
    for i in range(len(randomNums)):
        randomNums[i] = randomNums[i]/m1
    for i in range(len(randomNums)):
        cdf_conversion[i] = -((math.log(1 - randomNums[i])/(1/8.79558)))
    return cdf_conversion

def inspect1_comp1(noOfRandomNums):
    """
    Returns the RN field of the random Inspector 1 comp 1 work times.
    """
    LCM1 = LCMclass(Xo,m1,a,c,noOfRandomNums)
    LCM2 = LCMclass(Xo,m2,a,c,noOfRandomNums)
    LCM3 = LCMclass(Xo,m3,a,c,noOfRandomNums)
    LCM_list = [LCM1, LCM2, LCM3]
    CLCG_list = CLCG(LCM_list, noOfRandomNums)

    return rn_generator_insp1(CLCG_list, m1, noOfRandomNums)


def inspect2_comp2(noOfRandomNums):
    """
    Returns the RN field of the random Inspector 2 comp 2 work times.
    """
    LCM1 = LCMclass(Xo,m1,a,c,noOfRandomNums)
    LCM2 = LCMclass(Xo,m2,a,c,noOfRandomNums)
    LCM3 = LCMclass(Xo,m3,a,c,noOfRandomNums)
    LCM_list = [LCM1, LCM2, LCM3]
    CLCG_list = CLCG(LCM_list, noOfRandomNums)

    return rn_generator_insp2_comp2(CLCG_list, m1, noOfRandomNums)


def inspect2_comp3(noOfRandomNums):
    """
    Returns the RN field of the random Inspector 2 comp 3 work times.
    """
    LCM1 = LCMclass(Xo,m1,a,c,noOfRandomNums)
    LCM2 = LCMclass(Xo,m2,a,c,noOfRandomNums)
    LCM3 = LCMclass(Xo,m3,a,c,noOfRandomNums)
    LCM_list = [LCM1, LCM2, LCM3]
    CLCG_list = CLCG(LCM_list, noOfRandomNums)

    return rn_generator_insp2_comp3(CLCG_list, m1, noOfRandomNums)


def workshop1(noOfRandomNums):
    """
    Returns the RN field of the random Workshop 1 work times.
    """
    LCM1 = LCMclass(Xo,m1,a,c,noOfRandomNums)
    LCM2 = LCMclass(Xo,m2,a,c,noOfRandomNums)
    LCM3 = LCMclass(Xo,m3,a,c,noOfRandomNums)
    LCM_list = [LCM1, LCM2, LCM3]
    CLCG_list = CLCG(LCM_list, noOfRandomNums)

    return rn_generator_workshop1(CLCG_list, m1, noOfRandomNums)


def workshop2(noOfRandomNums):
    """
    Returns the RN field of the random Workshop 2 work times.
    """
    LCM1 = LCMclass(Xo,m1,a,c,noOfRandomNums)
    LCM2 = LCMclass(Xo,m2,a,c,noOfRandomNums)
    LCM3 = LCMclass(Xo,m3,a,c,noOfRandomNums)
    LCM_list = [LCM1, LCM2, LCM3]
    CLCG_list = CLCG(LCM_list, noOfRandomNums)

    return rn_generator_workshop2(CLCG_list, m1, noOfRandomNums)


def workshop3(noOfRandomNums):
    """
    Returns the RN field of the random Workshop 3 work times.
    """
    LCM1 = LCMclass(Xo,m1,a,c,noOfRandomNums)
    LCM2 = LCMclass(Xo,m2,a,c,noOfRandomNums)
    LCM3 = LCMclass(Xo,m3,a,c,noOfRandomNums)
    LCM_list = [LCM1, LCM2, LCM3]
    CLCG_list = CLCG(LCM_list, noOfRandomNums)

    return rn_generator_workshop3(CLCG_list, m1, noOfRandomNums)


def calc_mean(datalist):
    """
    Returns a random mean based on the passed datalist,
    adjusted to seconds as smallest measure.
    """
    datatotal = 0
    for x in range(0, 300):
        datatotal += float(datalist[x])
    mean = datatotal / 300
    #   Return number, adjust to seconds
    return mean
