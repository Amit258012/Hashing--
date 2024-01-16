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
