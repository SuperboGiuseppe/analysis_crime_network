import task1 as t1
import task2 as t2
import networkx as nx
import matplotlib.pyplot as plt


"""Task 3, 4 ,5"""

## Teacher didn't show up yet...
## given two edges: E1(D1,A1,W1) and E2(D2,A2,W2):
## exapmle of 'important changes' = absolute difference between W1 and W2 is > k.
## we define the threshhold k as:   -- average weight of every edge in the graph?
##                                  -- maybe reuse a value from task 1 <- NO! None of them use the weights.
##                                  -- I'm going to read the paper this is based on and see if they talk about this.
## ^ These are just my ideas after reading the task description. The teacher didn't come and I got tired of waiting! ^



def calculate_weight(net_A, net_B):
    edges_A = list(net_A.edges(data=True))
    #print(edges_A)
    edges_B = list(net_B.edges(data=True))
    ## select common edges:
    filtered_edges_A = [(a,b,c) for (a,b,c) in edges_A for (d,e,f) in edges_B if ((a == d) and (b == e))]
    edges_C = filtered_edges_A.copy()
    ## weight is result of the absolute-difference between the two weights:
    for i in range(len(edges_B)):
        edges_C[i][2]["weight"] = abs(edges_B[i][2]["weight"] - filtered_edges_A[i][2]["weight"])
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


def main():
    net_A = t2.rand_weight_graph("./DataSets/netWR.csv")[0]
    net_B = t2.rand_weight_graph("./DataSets/netAW.csv")[0]
    net_B_A = calculate_weight(net_A, net_B)
    net_result = filter_edges(net_B_A)
    net_graph = nx.Graph()
    net_graph.add_edges_from(net_result)
    #t1.get_graph_attributes(net_graph)
    plt.figure(1)
    plt.title("Network built upon difference between WR and AW")
    nx.draw(net_graph, with_labels=True, node_color="skyblue")

if __name__ == '__main__':
    main()
