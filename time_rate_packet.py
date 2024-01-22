"""
https://www.desiqna.in/14058/cisco-ideathon-oa-july-2023-sde-1
"""

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:
if current > max_capacity then add the drop into answer
Calculate the difference in current and next time then subtract the rate*difference 
if the current < 0 current = 0
"""


def ciscoOA(n, requests, rate, max_cap):
    cur = res = 0

    for i in range(n):
        cur_time = requests[i][0]
        cur += requests[i][1]

        if cur > max_cap:
            drop = cur - max_cap
            res += drop
            cur = max_cap

        if i <= n - 2:
            next_time = requests[i + 1][0]
            cur = cur - (next_time - cur_time) * rate

        if cur < 0:
            cur = 0

    return res


if __name__ == "__main__":
    n = int(input())
    requests = []
    for i in range(n):
        time, pack = list(map(int, input().split()))
        requests.append([time, pack])

    rate = int(input())
    max_cap = int(input())

    print(ciscoOA(n, requests, rate, max_cap))


"""
test case:-

i/p-
3
1 8
4 9
6 7
2
10

o/p - 4
"""
