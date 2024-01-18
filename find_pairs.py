# https://www.desiqna.in/15111/intuit-oa-sde1-2023-may
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

for a pair to be counted as an answer , both the elements ( x and x+k ) , need to be in the array.
So we simply create a map and store the frequency of each element in the map.
Now we traverse the map and for each element 'x' , we check if 'x+k' exists in the map . If it does , then it means a unique pair can be formed and hence, we increment the answer.

EDGE CASE :
The only edge case is the situation where k=0. If k=0 , instead of finding 'x+k' , we check if the frequency of 'x'>1. If it is , then we increment the answer .
Else , we don't increment the answer , as the frequency of x=1 and hence it can't form a pair with itself.
(only incrementing by one because in this case two the repeated pair say (4,4) needs to be counted only once it only needs to be counted once only)
"""


class Solution:
    def findPairs(self, nums, k):
        freq_map = {}
        for i in nums:
            freq_map[i] = freq_map.get(i, 0) + 1

        ans = 0
        for x, val in freq_map.items():
            # edge case where we are searching for the same element twice
            # for example, if we have 8 and we got 4 two times in our array
            if k == 0:
                if val > 1:
                    ans += 1
            # normal case
            elif x + k in freq_map:
                ans += 1

        return ans


if __name__ == "__main__":
    k = int(input())
    arr = list(map(int, input().split()))
    sol = Solution()
    res = sol.findPairs(arr, k)
    print(res)
