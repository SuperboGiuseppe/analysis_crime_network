import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
import task1 as Q1


def graphAttribute_check(rand_net):
    """
    Input - networkx graph object with labels
    output - graph attributes including 
            number of nodes, 
            number of edges,
            global clustering coefficient, 
            maximum degree, 
            average degree,
            diameter of giant component.
    """
    # check maximum and average degree
    num_of_nodes = nx.number_of_nodes(rand_net)
    num_of_edges = nx.number_of_edges(rand_net)
    nodes_degree = nx.degree(rand_net)
    degree_dict = {}
    for node in range(1,num_of_nodes + 1):
        degree_dict[node] = nodes_degree[node]
    maximum_degree = max(degree_dict.values())
    average_degree = sum(degree_dict.values())/num_of_nodes
    # check diameter
    giant_component = max(nx.connected_component_subgraphs(rand_net),key=len)
    #size_of_giant = nx.Graph.size(giant_component)
    diameter_of_giant = nx.algorithms.diameter(giant_component)
    # check global clustering coefficient 
    nodes_triangles = nx.triangles(rand_net)
    num_of_triangles = sum(nodes_triangles.values())
    pairs_path_length = dict(nx.all_pairs_shortest_path_length(rand_net))
    n = 0 
    for node in pairs_path_length.keys():  
        for item in pairs_path_length[node].values():
            if item == 2:
                n = n + 1
    global_clustering_coefficient = (num_of_triangles * 6) / n
    # summarize graph attributes
    graph_attributes = [["number of nodes", num_of_nodes], \
    ["number of edges", num_of_edges], \
    ["global clustering coefficient", global_clustering_coefficient], \
    ["maximum degree", maximum_degree], \
    ["average degree", average_degree], \
    ["diameter of giant component", diameter_of_giant]]
    return graph_attributes

def gcc_check(rand_net):
    """
    Input - networkx graph object with labels
    output - global clustering coefficient

    """
    nodes_triangles = nx.triangles(rand_net)
    num_of_triangles = sum(nodes_triangles.values())
    pairs_path_length = dict(nx.all_pairs_shortest_path_length(rand_net))
    n = 0 
    for node in pairs_path_length.keys():  
        for item in pairs_path_length[node].values():
            if item == 2:
                n = n + 1
    global_clustering_coefficient = (num_of_triangles * 6) / n
    return global_clustering_coefficient 

def giant_check(rand_net):
    """
    Input - networkx graph object with labels
    output - diameter of giant component
    
    """
    giant_component = max(nx.connected_component_subgraphs(rand_net),key=len)
    #size_of_giant = nx.Graph.size(giant_component)
    diameter_of_giant = nx.algorithms.diameter(giant_component)
    return diameter_of_giant 

##----------------------------------------Notes----------------------------------------------------------#
# 1. The following simulated network is built upon "powerlaw_cluster_graph" random graph generator
# 2. Among all graph attributes required, global clustering coefficient and diameter of giant component
# are more important metrics for the interest.
# 3. Graph similarity measurement...

def attributes_from_powerlaw(n,m,p_low,p_high,step_size,seed_num):
    """
    Input: n (int) - numbers of nodes
           m (int) – the number of random edges to add for each new node
           p_low (float) – Probability for edge creation in lower range
           p_high (float) – Probability for edge creation in higher range
           step_size - define the size of step
           seed_num (integer, random_state, or None (default)) – Indicator of random number generation state

    Output:
           graph attributes dictionary - p vs global clustering coefficient
                                       - p vs diameter of giant component
    """
    gcc = {}
    giant = {}
    for p in np.arange(p_low,p_high,step=step_size):
        rand_net = nx.powerlaw_cluster_graph(n,m,p, seed=seed_num)
        rand_net = nx.convert_node_labels_to_integers(rand_net, first_label=1)
        gcc[p] = gcc_check(rand_net)
        giant[p] = giant_check(rand_net)
    return gcc, giant

def main():
    #----------------------------------simulate a random network for netWR-----------------------------------#
    netWR_csv = "./DataSets/netWR.csv"
    netWR_G = Q1.csv_to_graph(netWR_csv)
    netWR_attributes = graphAttribute_check(netWR_G)

    # check graph attributes with different p in range(0.0, 1.0)
    gcc = attributes_from_powerlaw(182,2,0.0,1.0,0.1,1)[0]
    giant = attributes_from_powerlaw(182,2,0.0,1.0,0.1,1)[1]

    plt.figure(1)
    plt.subplot(121)
    plt.plot(gcc.keys(), gcc.values())
    plt.title("Simulated network - global clustering coefficient")
    plt.xlabel('p')

    plt.subplot(122)
    plt.plot(giant.keys(), giant.values())
    plt.title("Simulated network - diameter of giant")
    plt.xlabel('p')

    # check graph attributes with different p in range(0.3, 0.5)
    gcc = attributes_from_powerlaw(182,2,0.3,0.5,0.001,1)[0]
    giant = attributes_from_powerlaw(182,2,0.3,0.5,0.001,1)[1]

    plt.figure(2)
    plt.subplot(121)
    plt.plot(gcc.keys(), gcc.values())
    plt.title("Simulated network - global clustering coefficient")
    plt.xlabel('p')

    plt.subplot(122)
    plt.plot(giant.keys(), giant.values())
    plt.title("Simulated network - diameter of giant")
    plt.xlabel('p')

    # choose p = 0.32
    rand_net = nx.powerlaw_cluster_graph(182,2,0.32,seed=1)
    rand_net = nx.convert_node_labels_to_integers(rand_net, first_label=1)
    randnet_attributes = graphAttribute_check(rand_net)
    plt.figure(3)
    plt.title("Simulated netWR")
    nx.draw(rand_net, with_labels=True, pos=nx.spring_layout(rand_net), node_color="skyblue", node_size=180, font_size=8)

    #-----------------------------------simulate a random network for netAW---------------------------------------------#
    netAW_csv = "./DataSets/netAW.csv"
    netAW_G = Q1.csv_to_graph(netAW_csv)
    netAW_attributes = graphAttribute_check(netAW_G)

    # based on the plot from previous network, choose p = 0.33 for simulated netAW_G
    rand_net = nx.powerlaw_cluster_graph(182,2,0.33,seed=1)
    rand_net = nx.convert_node_labels_to_integers(rand_net, first_label=1)
    randnet_attributes = graphAttribute_check(rand_net)
    plt.figure(4)
    plt.title("Simulated netAW")
    nx.draw(rand_net, with_labels=True, pos=nx.spring_layout(rand_net), node_color="orange", node_size=180, font_size=8)
    #-----------------------------------simulate a random network for netJU--------------------------------------------#
    netJU_csv = "./DataSets/netJU.csv"
    netJU_G = Q1.csv_to_graph(netJU_csv)
    netJU_attributes = graphAttribute_check(netJU_G)

    # cannot find the suitale p after checking graph attributes with different p in range(0.6, 0.7) with seed=1
    # The seed was changed to some other random number (9 was chosen in this case)

    gcc = attributes_from_powerlaw(182,2,0.6,0.7,0.001,9)[0]
    giant = attributes_from_powerlaw(182,2,0.6,0.7,0.001,9)[1]

    plt.figure(5)
    plt.subplot(121)
    plt.plot(gcc.keys(), gcc.values())
    plt.title("Simulated network - global clustering coefficient")
    plt.xlabel('p')

    plt.subplot(122)
    plt.plot(giant.keys(), giant.values())
    plt.title("Simulated network - diameter of giant")
    plt.xlabel('p')

    # p = 0.64
    rand_net = nx.powerlaw_cluster_graph(182,2,0.64, seed=9)
    rand_net = nx.convert_node_labels_to_integers(rand_net, first_label=1)
    randnet_attributes = graphAttribute_check(rand_net)
    plt.figure(6)
    plt.title("Simulated netJU")
    nx.draw(rand_net, with_labels=True, pos=nx.spring_layout(rand_net), node_color="green", node_size=180, font_size=8)

    #plt.show()

if __name__ == '__main__':
    main()

#G_similarity = nx.algorithms.similarity.graph_edit_distance(rand_net, netWR_G)
#G_similarity = nx.algorithms.similarity.optimize_graph_edit_distance(rand_net, netWR_G)
