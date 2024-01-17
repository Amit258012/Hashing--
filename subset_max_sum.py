"""
 Given an array of size “N”; find a subset from an array with a particular property and the sum of that subset should be maximum possible. 

-> all adjacent elements should follow this.-> 

(s[1],s[2],...........s[m]) -> s[2] - s[1] = position[2] - position[1] 
S[3]-s[2] = position[3] - position[2].
.
.
.
.
"""

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

Analyze the equation s[i]-s[j] = i - j => s[i]-i = s[j]-j
Pref[i] = arr[i]-i
Use hashmap to add same diffence value and return maxValue
"""


class Solution:
    def fn(self, arr):
        n = len(arr)
        pref = [0] * n
        hmap = {}
        res = 0

        for i, num in enumerate(arr):
            pref[i] = num - i

        for i, val in enumerate(pref):
            hmap[val] = hmap.get(val, 0) + arr[i]
            res = max(res, hmap[val])
        return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    res = sol.fn(arr)
    print(res)
