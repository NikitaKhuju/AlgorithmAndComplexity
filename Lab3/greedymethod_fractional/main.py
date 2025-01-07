def greedy_fractional_knapsack(p,w,n):
    items = [(p[i], w[i], p[i] / w[i] , i) for i in range(len(p))]
    items.sort(key=lambda x: x[2], reverse = True)

    max_profit = 0
    remaining_capacity = m
    
    for profit, weight, ratio, index in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            max_profit += profit
            remaining_capacity -= weight
        else:
            max_profit += profit *(remaining_capacity/weight)
            remaining_capacity = 0
    return max_profit

p = [1,4,5,7] 
w = [1,3,4,5]
m = 10
print(greedy_fractional_knapsack(p,w,m ))


