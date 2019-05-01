"""
Task 2
"""
import matplotlib.pyplot as plt
import task1 as Q1
import numpy as np
import community
import networkx as nx
import networkx.algorithms.community as cm
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
    return net_G, net_array

def subdivise(adjacencyMatrix,k):
    """
    k: threshhold weight.
    """
    adjacencyMatrix[adjacencyMatrix<k] = 0
    newGraph = nx.from_numpy_matrix(adjacencyMatrix)
    newGraph = nx.convert_node_labels_to_integers(newGraph, first_label=1)
    return newGraph

def graph_attributes(graph):
    """
    """
    ## calculations:
    nbNodes = graph.number_of_nodes()
    nodes_betweeness = nx.betweenness_centrality(graph)
    nodes_centrality = nx.degree_centrality(graph)
    community_properties = Q1.community_detection(graph)
##    try:
##        communities = community.best_partition(graph)
##        #communities = cm.greedy_modularity_communities(graph)
##        nbCommun = len(list(communities))
##        perfCommun = cm.performance(graph,communities)
##    except(ZeroDivisionError):
##        nbCommun = 0
##        perfCommun = 0
    ## ...global clustering coefficient copied from task 1
    nodes_triangles = nx.triangles(graph)
    num_of_triangles = sum(nodes_triangles.values())
    pairs_path_length = dict(nx.all_pairs_shortest_path_length(graph))
    n = 0 
    for node in pairs_path_length.keys():  
        for item in pairs_path_length[node].values():
            if item == 2:
                n = n + 1
    ## create return dictionary:
    res = {}
    if n == 0:
        res['globacCc'] = 0
    else:
        res['globacCc']= (num_of_triangles * 6) / n
    res['Centrality'] = abs(max(nodes_centrality.values()) -
                            sum(nodes_centrality.values())/nbNodes)
    res['BetweenCentrality'] = abs(max(nodes_betweeness.values()) -
                                   sum(nodes_betweeness.values())/nbNodes)
    res['nbDetectCommunities'] = community_properties[0][1]
    res['qlDetectCommunities'] = community_properties[1][1]
    return res
    
def task2doer(csv_file_path):
    ## initialize variables:
    globacCc = []
    Centrality = []
    BetweenCentrality = []
    nbDetectCommunities = []
    qlDetectCommunities = []
    ## create graph and adjacency matrix:
    G,adjM = rand_weight_graph(csv_file_path)
    ## create subgraphs with threshholds k from 1 to n
    n = int(np.max(adjM))
    k = 1
    while k <= n:
        tmpGraph = subdivise(adjM,k)
        ## measure attributes
        x = graph_attributes(tmpGraph)
        globacCc.append(x['globacCc'])
        Centrality.append(x['Centrality'])
        BetweenCentrality.append(x['BetweenCentrality'])
        nbDetectCommunities.append(x['nbDetectCommunities'])
        qlDetectCommunities.append(x['qlDetectCommunities'])
        k+=1
    ## plot results:
    xaxis = list(range(1, n+1))
    plt.subplot(321)
    plt.plot(xaxis,globacCc)
    plt.xlabel('threshold k')
    plt.title("Global clustering coefficient")
    plt.subplot(322)
    plt.plot(xaxis,Centrality)
    plt.xlabel('threshold k')
    plt.title("difference between max centrality \n and avg centrality")
    plt.subplot(323)
    plt.plot(xaxis,BetweenCentrality)
    plt.xlabel('threshold k')
    plt.title("difference between max betweeness centrality \n and avg betweeness centrality")
    plt.subplot(324)
    plt.plot(xaxis,nbDetectCommunities)
    plt.xlabel('threshold k')
    plt.title("number of detected comunities")
    plt.subplot(325)
    plt.plot(xaxis,qlDetectCommunities)
    plt.xlabel('threshold k')
    plt.title("quality of detected communities")
    #plt.suptitle("Evolution of graph attributes")
    plt.tight_layout()
    #plt.show()

def main():
    #csvWR = "./DataSets/netWR.csv"
    #csvAW = "./DataSets/netAW.csv"
    csvJU = "./DataSets/netJU.csv"
    
    #task2doer(csvWR)
    #task2doer(csvAW)
    task2doer(csvJU)

if __name__ == '__main__':
    main()
