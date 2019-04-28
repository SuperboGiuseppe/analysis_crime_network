import task1 as t1
import task2 as t2
import networkx as nx
import matplotlib.pyplot as plt


"""Task 3, 4 ,5"""


def calculate_weight(net_A, net_B):
    edges_A = list(net_A.edges(data=True))
    edges_B = list(net_B.edges(data=True))
    ## select common edges:
    filtered_edges_A = [(a,b,c) for (a,b,c) in edges_A for (d,e,f) in edges_B if ((a == d) and (b == e))]
    filtered_edges_B = [(a, b, c) for (a, b, c) in edges_B for (d, e, f) in edges_A if ((a == d) and (b == e))]
    edges_C = filtered_edges_A.copy()
    ## weight is result of the absolute-difference between the two weights:
    for i in range(len(filtered_edges_B)):
        edges_C[i][2]["weight"] = abs(filtered_edges_B[i][2]["weight"] - filtered_edges_A[i][2]["weight"])
    return edges_C

def filter_edges(edges_list):
    #As threshold we decided to pick the average weight of every edge in the graph as it is an optimal value
    #in order to show "important changes" inside the network

    #Calculate threshold
    temp_sum = 0
    for i in range(len(edges_list)):
        temp_sum += edges_list[i][2]["weight"]
    average_weight = temp_sum/len(edges_list)

    #Remove edges with lower weight then k from the list
    result_list = []
    for i in range(len(edges_list)):
        if(edges_list[i][2]["weight"] > average_weight):
            result_list.append(edges_list[i])
    return result_list


def main(csv_A, csv_B):
    net_A = t2.rand_weight_graph(csv_A)[0]
    net_B = t2.rand_weight_graph(csv_B)[0]
    net_B_A = calculate_weight(net_A, net_B)
    net_result = filter_edges(net_B_A)
    net_graph = nx.Graph()
    net_graph.add_edges_from(net_result)
    nx.draw(net_graph, pos=nx.spring_layout(net_graph), with_labels=True, node_color="skyblue")
    attributes = t1.get_graph_attributes(net_graph)
    community = t1.community_detection(net_graph)
    return attributes, community

if __name__ == '__main__':
    main()
