#s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
#f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
recursive_a = []
iterative_a = []
def greedy_activity_selector(s, f):
    n = len(s)
    k = 0
    iterative_a.append(k)
    for m in range(1, n):
        if s[m] >= f[k]:
            iterative_a.append(m)
            k = m
    return iterative_a


def recursive_greedy_activity_selector(s, f, k, n):
    m = k + 1
    while m < n and s[m] < f[k] and k>=0:
        m = m + 1
    if m < n:
        recursive_a.append(m)
        recursive_greedy_activity_selector(s, f, m, n)
        return recursive_a

'''
r=greedy_activity_selector(s, f)
print(r)'''