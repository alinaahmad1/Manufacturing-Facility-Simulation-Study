"""
This file is used to define the varible set that is used in each replication,
I placed it here because it was cluttering the main file.
"""

#pylint:disable=C0206

class ReplicationVariables(object):
    """
    This is the class based dict that store variables over replications.
    """

    def __init__(self, logger):
        self.logger = logger
        self.service_times = {
            "inspector_1": [],
            "inspector_22": [],
            "inspector_23": [],
            "workstation_1": [],
            "workstation_2": [],
            "workstation_3": [],
        }
        self.idle_times = {
            1: [],
            2: [],
            3: [],
        }
        self.block_times = {
            1: [],
            2: [],
            3: []
        }
        self.products = {
            1: 0,
            2: 0,
            3: 0,
        }
        self.queue_occupancy = {
            "C1_buf_w1": [],
            "C1_buf_w2": [],
            "C1_buf_w3": [],
            "C2_buf_w2": [],
            "C3_buf_w3": [],
        }

    # There is almost certainly a better way of formatting this then
    # what I have here, but this is working consistantly so it stays.

    def add_insp_1_st(self, value):
        """Adds used random service time to the list."""
        self.service_times["inspector_1"].append(value)

    def add_insp_22_st(self, value):
        """Adds used random service time to the list."""
        self.service_times["inspector_22"].append(value)

    def add_insp_23_st(self, value):
        """Adds used random service time to the list."""
        self.service_times["inspector_23"].append(value)

    def add_ws_1_st(self, value):
        """Adds used random service time to the list."""
        self.service_times["workstation_1"].append(value)

    def add_ws_2_st(self, value):
        """Adds used random service time to the list."""
        self.service_times["workstation_2"].append(value)

    def add_ws_3_st(self, value):
        """Adds used random service time to the list."""
        self.service_times["workstation_3"].append(value)

    def add_insp_1_bt(self, value):
        """Adds block time to the list."""
        self.block_times[1].append(value)

    def add_insp_22_bt(self, value):
        """Adds block time to the list."""
        self.block_times[2].append(value)

    def add_insp_23_bt(self, value):
        """Adds block time to the list."""
        self.block_times[3].append(value)

    def add_ws_1_it(self, value):
        """Adds idle time to the list."""
        self.idle_times[1].append(value)

    def add_ws_2_it(self, value):
        """Adds idle time to the list."""
        self.idle_times[2].append(value)

    def add_ws_3_it(self, value):
        """Adds idle time to the list."""
        self.idle_times[3].append(value)

    def add_product_1(self):
        """Adds a created product to the list."""
        self.products[1] += 1

    def add_product_2(self):
        """Adds a created product to the list."""
        self.products[2] += 1

    def add_product_3(self):
        """Adds a created product to the list."""
        self.products[3] += 1

    def add_occupacy_c1_buf_w1(self, value):
        """adds the queue occupancy to the list."""
        self.queue_occupancy["C1_buf_w1"].append(value)

    def add_occupacy_c1_buf_w2(self, value):
        """adds the queue occupancy to the list."""
        self.queue_occupancy["C1_buf_w2"].append(value)

    def add_occupacy_c1_buf_w3(self, value):
        """adds the queue occupancy to the list."""
        self.queue_occupancy["C1_buf_w3"].append(value)

    def add_occupacy_c2_buf_w2(self, value):
        """adds the queue occupancy to the list."""
        self.queue_occupancy["C2_buf_w2"].append(value)

    def add_occupacy_c3_buf_w3(self, value):
        """adds the queue occupancy to the list."""
        self.queue_occupancy["C3_buf_w3"].append(value)

    def cull_service_times(self):
        """Culls 10% of total data."""
        for key in self.service_times:
            for i in range(int(len(self.service_times[key])*0.1)):
                temp_list = self.service_times[key]
                del temp_list[0]
            self.service_times[key] = temp_list

    def cull_idle_times(self):
        """Culls 10% of total data."""
        for key in self.idle_times:
            for i in range(int(len(self.idle_times[key])*0.1)):
                temp_list = self.idle_times[key]
                del temp_list[0]
            self.idle_times[key] = temp_list

    def cull_block_times(self):
        """Culls 10% of total data."""
        for key in self.block_times:
            for i in range(int(len(self.block_times[key])*0.1)):
                temp_list = self.block_times[key]
                del temp_list[0]
            self.block_times[key] = temp_list

    def cull_products(self):
        """Culls 10% of total data."""
        for key in self.products:
            temp_value = self.products[key]
            temp_value = temp_value - temp_value * 0.1
            self.products[key] = int(temp_value)

    def cull_occupancy(self):
        """Culls 10% of total data."""
        for key in self.queue_occupancy:
            for i in range(int(len(self.queue_occupancy[key])*0.1)):
                temp_list = self.queue_occupancy[key]
                del temp_list[0]
            self.queue_occupancy[key] = temp_list

class LittleLawVariables(object):
    """
    This is the class based dict that store little law variables over replications.
    """

    def __init__(self, logger):
        self.logger = logger
        self.c1_arrival_times = {
            "workstation_1": [],
            "workstation_2": [],
            "workstation_3": [],
        }
        self.c2_arrival_times = {
            "workstation_2": [],
        }
        self.c3_arrival_times = {
            "workstation_3": [],
        }
        self.c1_exit_times = {
            "workstation_1": [],
            "workstation_2": [],
            "workstation_3": [],
        }
        self.c2_exit_times = {
            "workstation_2": [],
        }
        self.c3_exit_times = {
            "workstation_3": [],
        }

    # There is almost certainly a better way of formatting this then
    # what I have here, but this is working consistantly so it stays.

    def add_c1_arrival_times(self, queue, value):
        """Adds used random service time to the list."""
        self.c1_arrival_times[queue].append(value)

    def add_c2_arrival_times(self, value):
        """Adds used random service time to the list."""
        self.c2_arrival_times["workstation_2"].append(value)

    def add_c3_arrival_times(self, value):
        """Adds used random service time to the list."""
        self.c3_arrival_times["workstation_3"].append(value)

    def add_c1_exit_times(self, queue, value):
        """Adds used random service time to the list."""
        self.c1_exit_times[queue].append(value)

    def add_c2_exit_times(self, value):
        """Adds used random service time to the list."""
        self.c2_exit_times["workstation_2"].append(value)

    def add_c3_exit_times(self, value):
        """Adds used random service time to the list."""
        self.c3_exit_times["workstation_3"].append(value)

    def print(self):
        """
        Prints all dict values
        """
        print("C1 Arrival Times\n")
        print(self.c1_arrival_times)
        print('\n')
        print("C1 Exit Times\n")
        print(self.c1_exit_times)
        print('\n')
        print("C2 Arrival Times\n")
        print(self.c2_arrival_times)
        print('\n')
        print("C2 Exit Times\n")
        print(self.c2_exit_times)
        print('\n')
        print("C3 Arrival Times\n")
        print(self.c3_arrival_times)
        print('\n')
        print("C3 Exit Times\n")
        print(self.c3_exit_times)
        print('\n')
