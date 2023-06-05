"""
This file is used to calculate the performance of the main features of the system,
namely the idle times, the blocked times, and the products produced.
"""

from scipy import stats
import numpy

# we init the logger to none here, so that we can set it to the main
# logger in the main file.
logger = None

def littles_law_validation(data):
    """
    This function is used to check the model using little's law.
    """
    print(data)

def calculate_confidance_interval(data, confidence=0.95):
    """
    This function takes in data and uses it to calculate the confidance
    interval of the given dataset.
    """
    if not isinstance(data, list):
        return data, 0
    data_length = len(data)
    if data_length is 0:
        return 0, 0
    mean, std_dev = numpy.mean(data), stats.sem(data)

    logger.debug("Numpy mean " + str(mean))
    logger.debug("Scipy standard deviation " + str(std_dev))

    error = std_dev * stats.t.ppf((1 + confidence) / 2., data_length - 1)
    return mean, error


def calculate_statistics(data):
    """
    This function is used to create the datasets used in the performance analysis
    when calculating the confidance intervals.
    """

    block_times_1 = []
    block_times_2 = []
    block_times_3 = []
    idle_times_1 = []
    idle_times_2 = []
    idle_times_3 = []
    products_produced_1 = []
    products_produced_2 = []
    products_produced_3 = []
    C1_buf_w1 = []
    C1_buf_w2 = []
    C1_buf_w3 = []
    C2_buf_w2 = []
    C3_buf_w3 = []


    for variable in data:
        block_times_1.extend(variable.block_times[1])
        block_times_2.extend(variable.block_times[2])
        block_times_3.extend(variable.block_times[3])
        idle_times_1.extend(variable.idle_times[1])
        idle_times_2.extend(variable.idle_times[2])
        idle_times_3.extend(variable.idle_times[3])
        products_produced_1.append(variable.products[1])
        products_produced_2.append(variable.products[2])
        products_produced_3.append(variable.products[3])
        C1_buf_w1.extend(variable.queue_occupancy["C1_buf_w1"])
        C1_buf_w2.extend(variable.queue_occupancy["C1_buf_w2"])
        C1_buf_w3.extend(variable.queue_occupancy["C1_buf_w3"])
        C2_buf_w2.extend(variable.queue_occupancy["C2_buf_w2"])
        C3_buf_w3.extend(variable.queue_occupancy["C3_buf_w3"])




    # This block calculates the confidance interval for all statistics of interest
    # then outputs the results to the logger.
    mean, error = calculate_confidance_interval(block_times_1)
    print("The confidence interval for inspector 1 block times is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(block_times_2)
    print("The confidence interval for inspector 2 block times is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(block_times_3)
    print("The confidence interval for inspector 3 block times is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(idle_times_1)
    print("The confidence interval for workstation 1 idle times is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(idle_times_2)
    print("The confidence interval for workstation 2 idle times is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(idle_times_3)
    print("The confidence interval for workstation 3 idle times is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(products_produced_1)
    print("The confidence interval for product 1 produced in 8 hrs is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(products_produced_2)
    print("The confidence interval for product 2 produced in 8 hrs is "\
                +str(mean)+" ±"+str(error)+"\n")
    mean, error = calculate_confidance_interval(products_produced_3)
    print("The confidence interval for product 3 produced in 8 hrs is "\
                +str(mean)+" ±"+str(error)+"\n")

    mean, error = calculate_confidance_interval(C1_buf_w1)
    print("The buffer occupancy for workshop 1 component 1 is "\
                +str(mean)+" ±"+str(error)+", the real value is 0.28\n")
    mean, error = calculate_confidance_interval(C1_buf_w2)
    print("The buffer occupancy for workshop 2 component 1 is "\
                +str(mean)+" ±"+str(error)+", the real value is 0.41\n")
    mean, error = calculate_confidance_interval(C1_buf_w3)
    print("The buffer occupancy for workshop 3 component 1 is "\
                +str(mean)+" ±"+str(error)+", the real value is 0.60\n")
    mean, error = calculate_confidance_interval(C2_buf_w2)
    print("The buffer occupancy for workshop 2 component 2 is "\
                +str(mean)+" ±"+str(error)+", the real value is 0.32\n")
    mean, error = calculate_confidance_interval(C3_buf_w3)
    print("The buffer occupancy for workshop 3 component 3 is "\
                +str(mean)+" ±"+str(error)+", the real value is 1.75\n")
