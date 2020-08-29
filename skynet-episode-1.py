import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
adj_dic = {}
gateways = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if n1 not in adj_dic:
        adj_dic[n1] = []
    if n2 not int adj_dic:
        adj_dic[n2] = []
    adj_dic[n1].append(n2)
    adj_dic[n2].append(n1)

for i in range(e):
    gateways.append(int(input()))  # the index of a gateway node

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Find shortest path to each gateway 
    # Store the path, it's lenght 


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print("0 1")
