MIN, MAX = -1000, 1000

def alpha_beta(depth, nodeIndex, isMaximizing, values, alpha, beta):
    if depth == 3: # leaf nodes
        return values[nodeIndex]
 
    if isMaximizing:
        best = MIN
        for i in range(0, 2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            if beta <= alpha: # Alpha Beta Pruning condition
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            if beta <= alpha: # Alpha Beta Pruning condition
                break
        return best
      
values = [3, 5, 6, 9, 1, 2, 0, -1]
ans = alpha_beta(0, 0, True, values, MIN, MAX)
print("The optimal value after pruning is:", ans)
