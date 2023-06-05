"""
This file is used to test the random number generators to ensure that
they produce input values that are equivilant in range and mean to
the real data.
"""

import model
from model import calc_mean


def validate_inspector1_component1(n):
    """
    This calculates the real mean, the mean of the random number field,
    and prints them and the % difference between them.
    """
    realdata = open('code/servinsp1.dat', encoding='utf-8').read().splitlines()
    real_mean = 0
    l = len(realdata)
    for x in range(0, l):
        real_mean += float(realdata[x])
    real_mean = real_mean / l

    random_mean = calc_mean(model.inspect1_comp1(n))

    print('Inspector 1 Component 1')
    print_mean(real_mean, random_mean)


def validate_inspector2_component2(n):
    """
    This calculates the real mean, the mean of the random number field,
    and prints them and the % difference between them.
    """
    realdata = open('code/servinsp22.dat', encoding='utf-8').read().splitlines()
    real_mean = 0
    l = len(realdata)
    for x in range(0, l):
        real_mean += float(realdata[x])
    real_mean = real_mean / l

    random_mean = calc_mean(model.inspect2_comp2(n))

    print('Inspector 2 Component 2')
    print_mean(real_mean, random_mean)


def validate_inspector2_component3(n):
    """
    This calculates the real mean, the mean of the random number field,
    and prints them and the % difference between them.
    """
    realdata = open('code/servinsp23.dat', encoding='utf-8').read().splitlines()
    real_mean = 0
    l = len(realdata)
    for x in range(0, l):
        real_mean += float(realdata[x])
    real_mean = real_mean / l

    random_mean = calc_mean(model.inspect2_comp3(n))

    print('Inspector 2 Component 3')
    print_mean(real_mean, random_mean)


def validate_workstation1(n):
    """
    This calculates the real mean, the mean of the random number field,
    and prints them and the % difference between them.
    """
    realdata = open('code/ws1.dat', encoding='utf-8').read().splitlines()
    real_mean = 0
    l = len(realdata)
    for x in range(0, l):
        real_mean += float(realdata[x])
    real_mean = real_mean / l

    random_mean = calc_mean(model.workshop1(n))

    print('Workstation 1')
    print_mean(real_mean, random_mean)


def validate_workstation2(n):
    """
    This calculates the real mean, the mean of the random number field,
    and prints them and the % difference between them.
    """
    realdata = open('code/ws2.dat', encoding='utf-8').read().splitlines()
    real_mean = 0
    l = len(realdata)
    for x in range(0, l):
        real_mean += float(realdata[x])
    real_mean = real_mean / l

    random_mean = calc_mean(model.workshop2(n))

    print('Workstation 2')
    print_mean(real_mean, random_mean)


def validate_workstation3(n):
    """
    This calculates the real mean, the mean of the random number field,
    and prints them and the % difference between them.
    """
    realdata = open('code/ws3.dat', encoding='utf-8').read().splitlines()
    real_mean = 0
    l = len(realdata)
    for x in range(0, l):
        real_mean += float(realdata[x])
    real_mean = real_mean / l

    random_mean = calc_mean(model.workshop3(n))

    print('Workstation 3')
    print_mean(real_mean, random_mean)


def print_mean(real_mean, random_mean):
    """
    Prints the formatted actual and random mean.
    And the % difference.
    """
    print('Actual Mean: ', real_mean)
    print('Random Mean:', random_mean)
    print('Difference(%): ', (abs(real_mean-random_mean)/real_mean) * 100, '\n')


if __name__ == '__main__':
    validate_inspector1_component1(2000)
    validate_inspector2_component2(2000)
    validate_inspector2_component3(2000)
    validate_workstation1(2000)
    validate_workstation2(2000)
    validate_workstation3(2000)
