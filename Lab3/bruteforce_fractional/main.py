def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def bruteforce_fractional_knapsack(p,w,m):
    assert len(p) == len(w), "p and w do not have the same length"

    n = len(p)
    bit_strings = get_strings(n)

    max_profit = 0

    for s in bit_strings:
        current_weight =0
        current_profit = 0
        subset = []

        for i in range(n):
            if s[i] == '1':
                current_weight += w[i]
                current_profit += p[i]
                subset.append(i)

        if current_weight <= m:
            max_profit = max(max_profit, current_profit)
        else:
            for i in subset:
                remaining_capacity = m - (current_weight - w[i])
                if remaining_capacity >0 and remaining_capacity<=w[i]:
                    fraction = remaining_capacity / w[i]
                    fractional_profit = current_profit-p[i] + (fraction * p[i])
                    max_profit = max(max_profit, fractional_profit)
    return max_profit

p = [60, 100, 120]  # Profits
w = [10, 20, 30]    # Weights
m = 50              # Maximum capacity

max_profit = bruteforce_fractional_knapsack(p, w, m)
print("Maximum Profit:", max_profit)