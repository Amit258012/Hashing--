"""
Given an array of size “N” ; find the maximum sum subarray which has the same elements in the start and end. 

Example :- 

[1 8 10 8 -5 8] 

Output :-> 29.

"""

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

create hashmap to check the occurence ot the same element 
hashmap {value: pref[i-1]}
sub array sum = pref[j] - pref[i-1]
pref[j] is constant, to get max result we need to minimize the value of pref[i-1]
"""


class Solution:
    def google(self, arr):
        n = len(arr)
        hmap = {}
        pref = 0
        res = 0

        for i in range(n):
            res = max(res, arr[i])

            if arr[i] not in hmap:
                hmap[arr[i]] = pref

            else:
                cur_sum = pref + arr[i] - hmap[arr[i]]
                res = max(res, cur_sum)
                hmap[arr[i]] = min(arr[i], pref)

            pref += arr[i]

        return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    res = sol.google(arr)
    print(res)
