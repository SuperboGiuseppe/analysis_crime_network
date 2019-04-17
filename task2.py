"""
Question 2
"""

import task1 as Q1
import numpy as np
import networkx as nx
from numpy.random import randint

def rand_weight_graph(csvfile):
    """
    """
    net_array = Q1.parse(csvfile)
    ## add weight attribute to existing edges.
    with np.nditer(net_array, op_flags=['readwrite']) as it:
        for x in it:
            if x>0:
                x[...] = randint(1,41)
    ## create nx graph from matrix
    net_G = nx.from_numpy_matrix(net_array)
    net_G = nx.convert_node_labels_to_integers(net_G, first_label=1)
    return net_G


netWR_csv = "./DataSets/netWR.csv"
r = rand_weight_graph(netWR_csv)
