
from collections import defaultdict
import math
import random
import heapq
def solve(matrix):
    """
    TSP polynomial solver, average case of O(n^3log(n)),
    and in worst case O(n^5log(n)) time and O(n^3) space
    input:
        matrix - 2d array of non-negative integers
    outputs:
        min_cost - minimum cost for minimum tour
        min_tour - minimum tour
    """
    n = len(matrix)
    #Get initial path and initialize components
    p = list(range(n))

    dist = defaultdict(lambda : math.inf)
    tour = defaultdict(tuple)
    s = p[0], p[-1]
    tour[s] = p
    dist[s] = sum(matrix[p[i]][p[i-1]] for i in range(1,len(p)))
    q = []
    heapq.heappush(q,(dist[s],s))
    visited = defaultdict(bool)
    min_cost = math.inf
    while q:

        _,u = heapq.heappop(q)
        
        path = tour[u]
        cost = dist[u]
        
        visited[u] = False
        
        for i in range(1,n):
            a = path[i-1]
            b = path[i]
            old_edge_cost = matrix[a][b] 
            new_edge_cost = matrix[a][u[1]]
            alt_cost = cost - old_edge_cost + new_edge_cost
            v= u[0],b
            if alt_cost < dist[v]:
                new_path = path[:i] + path[i:][::-1]
                tour[v] = new_path
                dist[v] = alt_cost
                if visited[v]:
                    continue
                visited[v] = True
                
                heapq.heappush(q,(dist[v], (v)))
            
            old_edge_cost = matrix[a][b] 
            new_edge_cost = matrix[b][u[0]]
            alt_cost = cost - old_edge_cost + new_edge_cost
            v= a,u[1]
            if alt_cost < dist[v]:
                new_path = path[:i][::-1] + path[i:]
                tour[v] = new_path
                dist[v] = alt_cost
                if visited[v]:
                    continue
                visited[v] = True
                
                heapq.heappush(q,(dist[v], (v)))
    for u in dist:
        if min_cost > dist[u] + matrix[u[0]][u[1]]:
            min_cost = dist[u] + matrix[u[0]][u[1]]
            min_path = tour[u]  
    return min_cost,min_path


def generate_symmetric_matrix(size, max_value):
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(i, size):
            value = random.randint(1, max_value)
            matrix[i][j] = value
            matrix[j][i] = value  # ensure symmetry

    return matrix

if __name__ == "__main__":
    import time
    for i in range(3, 1000):
        
        matrix = generate_symmetric_matrix(i, 100)
        s = time.time()
        cp = solve(matrix)
        print(time.time()-s, file = open('time.txt', "a"))
        print(cp[0], file = open("result.txt", "a"))
        print(matrix, file = open("matrix.txt", "a"))

    