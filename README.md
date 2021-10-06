# set-cover-problem-solver
Set-cover-problem-solver-using-2-methods-greedy-algorithm-excel-solver

This repo presents the implementation of a simple greedy algorithm applied to the set cover problem, as well as an example of application using excel. The algorithm was proposed here : https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/. In order to execute te solver you will either need to follow through the execution of the .py file, or add these 4 lines of code at the end: 
U = [..] the set of encoded zones to cover 
S = [[],[],[]] the set of subset of U,each subset shows the zones that the possibility covers 
cost = [,,,] 
print(solver(U,cost,S)) 
Example :
U = [1,2,3,4,5] 
S = [[1,5],[3,5],[1,2]] 
cost = [10,12,11]
print(solver(U,cost,S))


