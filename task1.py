import networkx as nx
from networkx.algorithms import community 
import numpy as np
import csv
import matplotlib.pyplot as plt
import itertools


def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as numpy array.
    """
    with open(csvfilename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        #reader = csv.reader(f, delimiter=';', quotechar="'")
        data = list(reader)
        # transform data into numpy array
        data = np.array(data).astype(float)
    return data


def csv_to_graph(csvfile):
    """
    Input - csvfile
    Output - graph with nodes labeled
    """
    net_array = parse(csvfile)
    # Return a graph from numpy matrix
    net_G = nx.from_numpy_matrix(net_array)
    net_G = nx.convert_node_labels_to_integers(net_G, first_label=1)
    return net_G


def get_graph_attributes(net_G):
    """
    Input - networkx graph object
    output - graph attributes including 
            number of nodes, number of edges,
            global clustering coefficient, 
            maximum degree, average degree,
            size of giant component, average path length, 
            maximum centrality, average centrality,
            maximum betweenness centrality,
            maximum closeness centrality, average closeness centrality.
    """
    # number of nodes
    num_of_nodes = net_G.number_of_nodes()
    # number of nodes
    num_of_edges = net_G.number_of_edges()
    # density of net
    net_density = nx.density(net_G)
    # maximum degree and average degree
    nodes_degree = nx.degree(net_G)
    degree_dict = {}
    for node in range(1,num_of_nodes + 1):
        degree_dict[node] = nodes_degree[node]
    maximum_degree = max(degree_dict.values())
    average_degree = sum(degree_dict.values())/num_of_nodes
    # global clustering coefficient: n - count numbers of paths of length two
    nodes_triangles = nx.triangles(net_G)
    num_of_triangles = sum(nodes_triangles.values())
    pairs_path_length = dict(nx.all_pairs_shortest_path_length(net_G))
    n = 0 
    for node in pairs_path_length.keys():  
        for item in pairs_path_length[node].values():
            if item == 2:
                n = n + 1
    global_clustering_coefficient = (num_of_triangles * 6) / n
    # size of giant component
    giant_component = max(nx.connected_component_subgraphs(net_G),key=len)
    # return number of edges in graph=graph size
    size_of_giant = nx.Graph.size(giant_component)
    # calculate the average path length of giant component
    average_shortest_path_length = nx.average_shortest_path_length(giant_component)
    # maximum centrality and average centrality
    nodes_centrality = nx.degree_centrality(net_G)
    maximum_of_centrality = max(nodes_centrality.values())
    average_of_centrality = sum(nodes_centrality.values())/num_of_nodes
    # maximum betweenness centrality
    nodes_betweenness_centrality = nx.betweenness_centrality(net_G)
    maximum_betweenness_centrality = max(nodes_betweenness_centrality.values())
    # maximum closeness centrality
    nodes_closeness_centrality = nx.closeness_centrality(net_G)
    maximum_closeness_centrality = max(nodes_closeness_centrality.values())
    average_closeness_centrality = sum(nodes_closeness_centrality.values())/num_of_nodes
    # summarize graph attributes
    graph_attributes = [["number of nodes", num_of_nodes], \
    ["number of edges", num_of_edges], \
    ["global clustering coefficient", global_clustering_coefficient], \
    ["maximum degree", maximum_degree], \
    ["average degree", average_degree], \
    ["size of giant component", size_of_giant], \
    ["average path length", average_shortest_path_length],\
    ["maximum centrality", maximum_of_centrality], \
    ["average centrality", average_of_centrality],\
    ["maximum betweenness centrality", maximum_betweenness_centrality],\
    ["maximum closeness centrality", maximum_closeness_centrality], \
    ["average closeness centrality", average_closeness_centrality], \
    ["net density", net_density]]
    return graph_attributes


def main():

    ##------------------------------------------------------------------------------------------##
    # GET netWR data
    # Display the graph
    netWR_csv = "./DataSets/netWR.csv"
    netWR_G = csv_to_graph(netWR_csv)
    plt.figure(1)
    plt.title("Network built upon WireTap Records")
    netWR_graphAttribute = get_graph_attributes(netWR_G)
    netWR_G.remove_nodes_from(list(nx.isolates(netWR_G)))
    nx.draw(netWR_G, with_labels=True, node_color="skyblue")

    ##------------------------------------------------------------------------------------------##
    # get netAW data
    netAW_csv = "./DataSets/netAW.csv"
    netAW_G = csv_to_graph(netAW_csv)
    # Display the graph
    plt.figure(2)
    plt.title("Network built upon Arrest warrants")
    netAW_graphAttribute = get_graph_attributes(netAW_G)
    netAW_G.remove_nodes_from(list(nx.isolates(netAW_G)))
    nx.draw(netAW_G, with_labels=True, node_color="orange")


    ##------------------------------------------------------------------------------------------##
    # get netJU data
    netJU_csv = "./DataSets/netJU.csv"
    netJU_G = csv_to_graph(netJU_csv)
    # Display the graph
    plt.figure(3)
    plt.title("Network built upon judgment")
    netJU_graphAttribute = get_graph_attributes(netJU_G)
    netJU_G.remove_nodes_from(list(nx.isolates(netJU_G)))
    nx.draw(netJU_G, with_labels=True, node_color="green")

    plt.show()

if __name__ == '__main__':
    main()