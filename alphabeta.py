def minimax_alpha_beta(depth, nodelndex, maximizingPlayer, values, alpha, beta):
if depth ==3:
return values[nodelndex]
best = float('-inf') if maximizingPlayer else float('inf')
for i in range(2):
val = minimax_alpha_beta(depth + 1, nodelndex * 2 + i, not maximizingPlayer, values,
alpha,beta)
best = max(best, val) if maximizingPlayer else min(best, val)
alpha = max(alpha, best) if maximizingPlayer else min(alpha, best)
if beta <= alpha:
break
return best
if name ==" main ":
values=[3,5,6,9,1,2,0,-1]
print("The optimal value is:", minimax_alpha_beta(0, 0, True, values, float('-inf'),
float('inf')))
