import sys

# Graph representing distances between 4 cities
V = 4
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

def tsp(graph, visited, curr_pos, n, count, cost, ans):
    # If all cities visited and there is a path back to start
    if (count == n and graph[curr_pos][0]):
        ans = min(ans, cost + graph[curr_pos][0])
        return ans

    # Try going to all other cities
    for i in range(n):
        if (visited[i] == False and graph[curr_pos][i]):
            visited[i] = True
            ans = tsp(graph, visited, i, n, count + 1, cost + graph[curr_pos][i], ans)
            visited[i] = False # backtrack
            
    return ans

visited = [False] * V
visited[0] = True # start from city 0

ans = sys.maxsize
ans = tsp(graph, visited, 0, V, 1, 0, ans)

print("Minimum cost for Travelling Salesman is:", ans)
