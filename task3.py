import task1 as t1
import task2 as t2
import networkx as nx


"""Task 3"""

## Teacher didn't show up yet...
## given two edges: E1(D1,A1,W1) and E2(D2,A2,W2):
## exapmle of 'important changes' = absolute difference between W1 and W2 is > k.
## we define the threshhold k as:   -- average weight of every edge in the graph?
##                                  -- maybe reuse a value from task 1 <- NO! None of them use the weights.
##                                  -- I'm going to read the paper this is based on and see if they talk about this.
## ^ These are just my ideas after reading the task description. The teacher didn't come and I got tired of waiting! ^



def filter_edges(net_A, net_B):
    edges_A = list(net_A.edges(data=True))
    edges_B = list(net_B.edges(data=True))
    ## select common edges:
    filtered_edges_A = [(a,b,c) for (a,b,c) in edges_A for (d,e,f) in edges_B if ((a == d) and (b == e))]
    ## weight is result of the absolute-difference between the two weights:
    edges_C = [(edges_B[i][0],edges_B[i][1], abs(edges_B[i][2]["weight"] - filtered_edges_A[i][2]["weight"])) for i in range(len(edges_B))]
    ## TO DO:
    ## define the threshhold k (get it from task 1 ?)
    ## remove edges bellow the threshhold!
    print(edges_C)
    return edges_C

def main():
    net_A = t2.rand_weight_graph("./DataSets/netWR.csv")[0]
    net_B = t2.rand_weight_graph("./DataSets/netAW.csv")[0]
    net_result = filter_edges(net_A, net_B)

if __name__ == '__main__':
    main()
