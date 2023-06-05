"""
This file contains all the definitions for the inspectors and the workshops.
"""
#library imports
import random
from simpy.resources import container
from replication_variables import ReplicationVariables, LittleLawVariables

class Workshop1(object):
    """
    The Workshop 1 object takes C1 components and outputs P1 products.

    This def uses the mean of the supplied data as the service time.
    """

    def __init__(self, env, logger, simulation_variables: ReplicationVariables,
                little_law_variables: LittleLawVariables, rn_field):
        self.env = env
        self.logger = logger
        self.simulation_variables = simulation_variables
        self.little_law_variables = little_law_variables
        self.c1_queue = container.Container(self.env, 2)
        self.action = env.process(self.run())
        self.rn_field = rn_field

    def run(self):
        """
        The main loop of the workshop.
        """
        self.logger.debug('workshop 1 starting')

        while True:
            # Waits until there are components available to use
            idle_start = self.env.now
            yield self.c1_queue.get(1)
            self.simulation_variables.add_occupacy_c1_buf_w1(self.c1_queue.level)
            self.simulation_variables.add_ws_1_it(self.env.now - idle_start)
            # Use a randomly pulled datam from the rn field as the inspection time.
            service_time = random.choice(self.rn_field)
            self.simulation_variables.add_ws_1_st(service_time)
            yield self.env.timeout(service_time)
            self.simulation_variables.add_product_1()

            # Get component 1 exit time.
            exit_time = self.env.now
            self.little_law_variables.add_c1_exit_times("workstation_1", exit_time)

            self.logger.debug('Product 1 assembled')


class Workshop2(object):
    """
    The Workshop 2 object takes C1 and C2 components and outputs P2 products.

    This def uses the mean of the supplied data as the service time.
    """

    def __init__(self, env, logger, simulation_variables: ReplicationVariables,
                little_law_variables: LittleLawVariables, rn_field):
        self.env = env
        self.logger = logger
        self.simulation_variables = simulation_variables
        self.little_law_variables = little_law_variables
        self.c1_queue = container.Container(self.env, 2)
        self.c2_queue = container.Container(self.env, 2)
        self.action = env.process(self.run())
        self.rn_field = rn_field

    def run(self):
        """
        The main loop of the workshop.
        """

        self.logger.debug('workshop 2 starting')
        while True:
            # Waits until there are components available to use
            idle_start = self.env.now
            yield self.c1_queue.get(1) & self.c2_queue.get(1)
            self.simulation_variables.add_occupacy_c1_buf_w2(self.c1_queue.level)
            self.simulation_variables.add_occupacy_c2_buf_w2(self.c2_queue.level)
            self.simulation_variables.add_ws_2_it(self.env.now - idle_start)
            # Use a randomly pulled datam from the rn field as the inspection time.
            service_time = random.choice(self.rn_field)
            self.simulation_variables.add_ws_2_st(service_time)
            yield self.env.timeout(service_time)
            self.simulation_variables.add_product_2()

            # Get component 1/2 exit time.
            exit_time = self.env.now
            self.little_law_variables.add_c1_exit_times("workstation_2", exit_time)
            self.little_law_variables.add_c2_exit_times(exit_time)

            self.logger.debug('Product 2 assembled')


class Workshop3(object):
    """
    The Workshop 3 object takes C1 and C3 components and outputs P3 products.

    This def uses the mean of the supplied data as the service time.
    """

    def __init__(self, env, logger, simulation_variables: ReplicationVariables,
                 little_law_variables: LittleLawVariables, rn_field):
        self.env = env
        self.logger = logger
        self.simulation_variables = simulation_variables
        self.little_law_variables = little_law_variables
        self.c1_queue = container.Container(self.env, 2)
        self.c3_queue = container.Container(self.env, 2)
        self.action = env.process(self.run())
        self.rn_field = rn_field

    def run(self):
        """
        The main loop of the workshop.
        """

        self.logger.debug('workshop 3 starting')
        while True:
            # Waits until there are components available to use
            idle_start = self.env.now
            yield self.c1_queue.get(1) & self.c3_queue.get(1)
            self.simulation_variables.add_occupacy_c1_buf_w3(self.c1_queue.level)
            self.simulation_variables.add_occupacy_c3_buf_w3(self.c3_queue.level)
            self.simulation_variables.add_ws_3_it(self.env.now - idle_start)
            # Use a randomly pulled datam from the rn field as the inspection time.
            service_time = random.choice(self.rn_field)
            self.simulation_variables.add_ws_3_st(service_time)
            yield self.env.timeout(service_time)
            self.simulation_variables.add_product_3()

            # Get component 1/3 exit time.
            exit_time = self.env.now
            self.little_law_variables.add_c1_exit_times("workstation_3", exit_time)
            self.little_law_variables.add_c3_exit_times(exit_time)

            self.logger.debug('Product 3 assembled')

class Inspector1(object):
    """
    The object Inspector1 takes component 1 items and inspects them
    before handing them off to the least empty queue.
    
    This def uses the mean of the supplied data as the service time.
    """

    def __init__(self, env, logger, simulation_variables: ReplicationVariables,
                 little_law_variables: LittleLawVariables, workshop_1, workshop_2,
                 workshop_3, inspector1_rn_field):
        self.env = env
        self.logger = logger
        self.simulation_variables = simulation_variables
        self.little_law_variables = little_law_variables
        self.action = env.process(self.run())
        self.workshop_1 = workshop_1
        self.workshop_2 = workshop_2
        self.workshop_3 = workshop_3
        self.inspector1_rn_field = inspector1_rn_field

    def run(self):
        """
        The execution loop of the inspector.
        """
        self.logger.debug('Inspector 1 starting')
        while True:

            # Get component 1 arrival time.
            arrival_time = self.env.now

            # Use a randomly pulled datam from the rn field as the inspection time.
            service_time = random.choice(self.inspector1_rn_field)
            self.simulation_variables.add_insp_1_st(service_time)

            # Finds the queue with the least C1.
            yield self.env.timeout(service_time)
            block_time = self.env.now

            if self.workshop_1.c1_queue.level <= self.workshop_2.c1_queue.level or \
                    self.workshop_1.c1_queue.level <= self.workshop_3.c1_queue.level:
                yield self.workshop_1.c1_queue.put(1)
                self.simulation_variables.add_occupacy_c1_buf_w1(self.workshop_1.c1_queue.level)
                self.logger.debug('Added component 1 to workshop 1')
                self.little_law_variables.add_c1_arrival_times("workstation_1", arrival_time)
            elif self.workshop_2.c1_queue.level <= self.workshop_3.c1_queue.level:
                yield self.workshop_2.c1_queue.put(1)
                self.simulation_variables.add_occupacy_c1_buf_w2(self.workshop_2.c1_queue.level)
                self.logger.debug('Added component 1 to workshop 2')
                self.little_law_variables.add_c1_arrival_times("workstation_2", arrival_time)
            else:
                yield self.workshop_3.c1_queue.put(1)
                self.simulation_variables.add_occupacy_c1_buf_w3(self.workshop_3.c1_queue.level)
                self.logger.debug('Added component 1 to workshop 3')
                self.little_law_variables.add_c1_arrival_times("workstation_3", arrival_time)
            self.simulation_variables.add_insp_1_bt(self.env.now - block_time)

class Inspector2(object):
    """
    The object Inspector1 takes component 1 items and inspects them
    before handing them off to the least empty queue.
    
    This def uses the mean of the supplied data as the service time.
    """

    def __init__(self, env, logger, simulation_variables: ReplicationVariables,
                 little_law_variables: LittleLawVariables, workshop_2, workshop_3,
                 inspector2_comp2_rn_field, inspector2_comp3_rn_field):
        self.env = env
        self.logger = logger
        self.simulation_variables = simulation_variables
        self.little_law_variables = little_law_variables
        self.action = env.process(self.run())
        self.workshop_2 = workshop_2
        self.workshop_3 = workshop_3
        self.inspector2_comp2_rn_field = inspector2_comp2_rn_field
        self.inspector2_comp3_rn_field = inspector2_comp3_rn_field

    def run(self):
        """
        The execution loop of the inspector.
        """

        self.logger.debug('Inspector 2 starting')
        while True:
            if bool(random.getrandbits(1)):  # Randomly decides which component to make
                # Use a randomly pulled datam from the rn field as the inspection time.
                service_time = random.choice(self.inspector2_comp2_rn_field)
                self.simulation_variables.add_insp_22_st(service_time)

                # Get component 2 arrival time.
                arrival_time = self.env.now
                self.little_law_variables.add_c2_arrival_times(arrival_time)

                yield self.env.timeout(service_time)
                block_time = self.env.now
                yield self.workshop_2.c2_queue.put(1)
                self.simulation_variables.add_occupacy_c1_buf_w1(self.workshop_2.c2_queue.level)
                self.simulation_variables.add_insp_22_bt(self.env.now - block_time)
                self.logger.debug('Added component 2 to workshop 2')
            else:
                # Use a randomly pulled datam from the rn field as the inspection time.
                service_time = random.choice(self.inspector2_comp3_rn_field)
                self.simulation_variables.add_insp_23_st(service_time)

                # Get component 2 arrival time.
                arrival_time = self.env.now
                self.little_law_variables.add_c3_arrival_times(arrival_time)

                yield self.env.timeout(service_time)
                block_time = self.env.now
                yield self.workshop_3.c3_queue.put(1)
                self.simulation_variables.add_occupacy_c3_buf_w3(self.workshop_3.c3_queue.level)
                self.simulation_variables.add_insp_23_bt(self.env.now - block_time)
                self.logger.debug('Added component 3 to workshop 3')
