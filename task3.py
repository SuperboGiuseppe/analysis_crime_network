import task1 as t1
import task2 as t2
import networkx as nx


"""Task 3"""




def filter_edges(net_A, net_B):
    edges_A = list(net_A.edges(data=True))
    edges_B = list(net_B.edges(data=True))
    ## select common edges
    filtered_edges_A = [(a,b,c) for (a,b,c) in edges_A for (d,e,f) in edges_B if ((a == d) and (b == e))]
    ## weight is result of the difference between the two weights (absolute value)
    edges_C = [(edges_B[i][0],edges_B[i][1], abs(edges_B[i][2]["weight"] - filtered_edges_A[i][2]["weight"])) for i in range(len(edges_B))]
    print(edges_C)
    return edges_C

def main():
    net_A = t2.rand_weight_graph("./DataSets/netWR.csv")[0]
    net_B = t2.rand_weight_graph("./DataSets/netAW.csv")[0]
    net_result = filter_edges(net_A, net_B)

if __name__ == '__main__':
    main()
