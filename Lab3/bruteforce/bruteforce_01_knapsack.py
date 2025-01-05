def get_strings(n):
    #Generate all the binary strings of length n
    return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

def bruteforce_01knapsack(p,w,m):
    assert len(p) == len(w), "p and w do not have the same length"

    n = len(p)
    bit_strings = get_strings(n)

    max_profit = 0
    for s in bit_strings:
        current_weight = 0
        current_profit = 0

        for i in range(n):
            if s[i] == '1':
                current_weight += w[i]
                current_profit += p[i]

        if current_weight <= m and current_profit > max_profit:
            max_profit = current_profit

    return max_profit

