import heapq
from collections import defaultdict
import math



def solve(matrix):
    """
    TSP polynomial solver, average case of O(n^4),
    and in worst case O(n^9log(n)) time and O(n^5) space
    input:
        matrix - 2d symmetric matrix of non-negative integers
    outputs:
        min_cost - minimum cost for minimum tour
        min_tour - minimum tour
    """
    n = len(matrix)
    #Get initial path and initialize components
    p = list(range(n))

    dist = defaultdict(lambda : math.inf)
    tour = defaultdict(tuple)
    s = p[-1],p[0],p[1],p[2]
    tour[s] = p
    dist[s] = sum(matrix[p[i]][p[i-1]] for i in range(len(p)))
    q = []
    heapq.heappush(q,(0,s))
    visited = defaultdict(bool)
    min_cost = math.inf
    while q:

        height,u = heapq.heappop(q)
        
        path = tour[u]
        
        if height > n - 1:
            break
        cost = dist[u]
        if min_cost > dist[u]:
            min_cost = dist[u]
            min_path = path  
        if visited[u]:
            visited[u] = False
        for i in range(n-2):
            for j in range(i+1,n-1):
                a = path[i-1]
                b = path[i]
                c = path[j]
                d = path[j+1]
                old_edge_cost = matrix[a][b] + matrix[c][d]
                new_edge_cost = matrix[a][c] + matrix[b][d]
                alt_cost = cost - old_edge_cost + new_edge_cost
                if alt_cost < dist[a,b,c,d]:
                    new_path = []
                    for k in range(i):
                        new_path.append(path[k])
                    for k in range(j,i-1, -1):
                        new_path.append(path[k])
                    for k in range(j+1,n):
                        new_path.append(path[k])
                    tour[a,b,c,d] = new_path
                    dist[a,b,c,d] = alt_cost
                    if visited[a,b,c,d]:
                        continue
                    visited[a,b,c,d] = True
                    heapq.heappush(q,(height + 1, (a,b,c,d)))
                 
    return min_cost,min_path