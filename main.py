"""
This is the main executable file of the system simulator.
"""

import logging

import coloredlogs
import model
import model_validator
import numpy
import simpy
import simulation
from replication_variables import ReplicationVariables, LittleLawVariables


def data_to_dict(data):
    """
    This function is used to convert a list
    into a dict.
    """
    new_dict = {}
    for i in data:
        try:
            for j in data[i]:
                if j not in new_dict:
                    new_dict[j] = []
                new_dict[j].append(data[i][j])
        except TypeError:
            pass
    return new_dict


# Main execution.
if __name__ == '__main__':
    # Setting up logger.
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  \
                                     %(message)s")
    logger = logging.getLogger()

    # Allow logger to output data to log file for ease of reading.
    # fileHandler = logging.FileHandler("code/logs/log.log")
    # fileHandler.setFormatter(logFormatter)
    # fileHandler.setLevel("INFO")
    # logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    coloredlogs.install(level=logging.INFO)

    model_validator.logger = logger

    # Simulation variables
    print("Enter nothing for default simulation values (1000, 30000)")
    REPLICATIONS = int(input("Enter Replications: ") or "1000")
    REPLICATION_DURATION = int(input("Enter time (sec): ") or "30000")
    INITILIZATION_PHASE = int(REPLICATION_DURATION*0.1)
    REPLICATION_OUTPUTS = {}

    SIMULATION_VARIABLES = []
    SIMULATION_LITTLE_LAW: list[LittleLawVariables] = []

    # Pregenerate Random Number Fields (using rn field size of 5000)
    inspector_1_random_numbers = model.inspect1_comp1(5000)
    inspector_2_comp_2_random_numbers = model.inspect2_comp2(5000)
    inspector_2_comp_3_random_numbers = model.inspect2_comp3(5000)
    workshop_1_random_numbers = model.workshop1(5000)
    workshop_2_random_numbers = model.workshop2(5000)
    workshop_3_random_numbers = model.workshop3(5000)

    #   Start Program
    logger.info("Creating simulation environment")

    #   Execution loop
    for iteration in range(1, REPLICATIONS+1):

        logger.info('Starting iteration %s', str(iteration))
        main_env = simpy.Environment()
        REPLICATION_VARIABLES = ReplicationVariables(logger)
        LITTLE_LAW_VARIABLES = LittleLawVariables(logger)

        workshop_1 = simulation.Workshop1(main_env, logger, REPLICATION_VARIABLES, LITTLE_LAW_VARIABLES,
                                          workshop_1_random_numbers)
        workshop_2 = simulation.Workshop2(main_env, logger, REPLICATION_VARIABLES, LITTLE_LAW_VARIABLES,
                                          workshop_2_random_numbers)
        workshop_3 = simulation.Workshop3(main_env, logger, REPLICATION_VARIABLES, LITTLE_LAW_VARIABLES,
                                          workshop_3_random_numbers)
        inspector_1 = simulation.Inspector1(main_env, logger, REPLICATION_VARIABLES, LITTLE_LAW_VARIABLES,
                                            workshop_1, workshop_2, workshop_3,
                                            inspector_1_random_numbers)
        inspector_2 = simulation.Inspector2(main_env, logger, REPLICATION_VARIABLES, LITTLE_LAW_VARIABLES,
                                            workshop_2, workshop_3, inspector_2_comp_2_random_numbers,
                                            inspector_2_comp_3_random_numbers)
        logger.info("Simulation classes created")

        # Run simulation
        logger.info("Running simulation...")
        main_env.run(until=REPLICATION_DURATION)  # 'until' is simulation duration

        #   Cull 10% from lists to remove initilization bias.
        REPLICATION_VARIABLES.cull_service_times()
        REPLICATION_VARIABLES.cull_idle_times()
        REPLICATION_VARIABLES.cull_block_times()
        REPLICATION_VARIABLES.cull_products()
        REPLICATION_VARIABLES.cull_occupancy()

        #   Save iteration variables to list
        SIMULATION_VARIABLES.append(REPLICATION_VARIABLES)
        SIMULATION_LITTLE_LAW.append(LITTLE_LAW_VARIABLES)
        #   Simulation End
        logger.info("Replication %s complete", str(iteration))

    #   Collect outputs
    logger.info('Simulation ended, collecting output\n')
    model_validator.calculate_statistics(SIMULATION_VARIABLES)
    service_time_means = {
        "inspector_1": [],
        "inspector_22": [],
        "inspector_23": [],
        "workstation_1": [],
        "workstation_2": [],
        "workstation_3": [],
    }
    for x in SIMULATION_VARIABLES:
        for key, value in x.service_times.items():
            service_time_means[key].extend(value)
    for key, value in service_time_means.items():
        print("Average service time for %s: %s", key, str(numpy.mean(value)))

    # I am calculating the time delay for each component by finding the entry and exit times for each component
    # as it passes through the system, then finding the differnace to get each individual time delay, the values
    # are then averaged once per replecation then once more overall, to get a value in seconds.

    # The arrival rate is calcualted by taking the size of the list of a component times to get number of components
    # which gives the number that passed through the system, then divided by the simulation time to get the rate that
    # components arrived.

    # The avrage items in the system should be equal to the avrage buffer occupancy for that componant.

    c1_time_means = []
    c2_time_means = []
    c3_time_means = []
    arrival_rate = 0

    for x in SIMULATION_LITTLE_LAW:

        c1_arrival_times_w1 = x.c1_arrival_times['workstation_1']
        c1_arrival_times_w2 = x.c1_arrival_times['workstation_2']
        c1_arrival_times_w3 = x.c1_arrival_times['workstation_3']
        c1_exit_times_w1 = x.c1_exit_times['workstation_1']
        c1_exit_times_w2 = x.c1_exit_times['workstation_2']
        c1_exit_times_w3 = x.c1_exit_times['workstation_3']
        c2_arrival_times_w2 = x.c2_arrival_times['workstation_2']
        c2_exit_times_w2 = x.c2_exit_times['workstation_2']
        c3_arrival_times_w2 = x.c3_arrival_times['workstation_3']
        c3_exit_times_w3 = x.c3_exit_times['workstation_3']

        for count, time in enumerate(c1_exit_times_w1):
            time_difference = time - c1_arrival_times_w1[count]
            c1_time_means.append(time_difference)

        for count, time in enumerate(c1_exit_times_w2):
            time_difference = time - c1_arrival_times_w2[count]
            c1_time_means.append(time_difference)

        for count, time in enumerate(c1_exit_times_w3):
            time_difference = time - c1_arrival_times_w3[count]
            c1_time_means.append(time_difference)

        for count, time in enumerate(c2_exit_times_w2):
            time_difference = time - c1_arrival_times_w1[count]
            c2_time_means.append(time_difference)

        for count, time in enumerate(c3_exit_times_w3):
            time_difference = time - c1_arrival_times_w1[count]
            c3_time_means.append(time_difference)
        arrival_rate += len(c1_arrival_times_w1)+len(c1_arrival_times_w2)+len(c1_arrival_times_w3)

    arrival_rate = arrival_rate/REPLICATIONS
    arrival_rate = arrival_rate/REPLICATION_DURATION
    print("Arrival rate for C1 ", str(arrival_rate), "arrivals/second")
    print("Time Delay for C1 " + str(numpy.mean(c1_time_means)))
    print("Arrival rate for C2 ", str((len(c2_time_means)/REPLICATIONS)/REPLICATION_DURATION), "arrivals/second")
    print("Time Delay for C2 " + str(numpy.mean(c2_time_means)))
    print("Arrival rate for C3 ", str((len(c3_time_means)/REPLICATIONS)/REPLICATION_DURATION), "arrivals/second")
    print("Time Delay for C3 " + str(numpy.mean(c3_time_means)))
