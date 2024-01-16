"""
Count the number of mountain subarrays(length.>=3) in the array 

1<=N<=100000

1<=A[i]<=100000000

[1 2 4 2 1] 

O/p-> [1 2 4 2] 
[2 4 2] 
[2 4 2 1] 
[1 2 4 2 1] 
"""

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

Pref[i] longest increasing subarray size ending at i
Suf[i] longest increasing subarray size in backward ending at i
For each peak value nums[i] the res = max(res, (pref[i]-1)*suf[i]-1) )
"""


class Solution:
    def count_mountain_subarray(self, arr):
        n = len(arr)
        suf = [0] * n
        suf[n - 1] = 1

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                suf[i] = suf[i + 1] + 1
            else:
                suf[i] = 1

        pref = 1
        res = 0

        for j in range(1, n):
            if arr[j] > arr[j - 1]:
                pref += 1
            else:
                pref = 1

            res += (pref - 1) * (suf[j] - 1)

        return res


def main():
    arr = list(map(int, input().split()))

    solution = Solution()
    res = solution.count_mountain_subarray(arr)
    print(res)


if __name__ == "__main__":
    main()
