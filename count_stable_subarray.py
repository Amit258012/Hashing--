# https://www.desiqna.in/15839/zscaler-oa-2023-sep-set-10
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

Use hashmap for checking for occurence
calc prefix sum
if num in hashmap and sum between 2 same elements are same , count++
"""


class Solution:
    def count_stable_subarray(self, nums):
        n = len(nums)
        hmap = {}
        pref = [0] * n
        count = 0

        for i in range(n):
            if nums[i] in hmap and (pref[i - 1] - pref[hmap[nums[i]]]) == nums[i]:
                count += 1

            if i >= 1:
                pref[i] = pref[i - 1] + nums[i]
            else:
                pref[i] = nums[i]

            hmap[nums[i]] = i
        return count


def main():
    arr = list(map(int, input().split()))

    solution = Solution()
    res = solution.count_stable_subarray(arr)
    print(res)


if __name__ == "__main__":
    main()
