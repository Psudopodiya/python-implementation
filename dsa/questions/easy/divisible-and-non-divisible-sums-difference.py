
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1, sum2 = 0, 0
        for i in range(1, n + 1):
            if i % m == 0:
                sum2 += m
            else:
                sum1 += n
        print(sum1, sum2)
        return sum1 - sum2


obj = Solution()
obj.differenceOfSums(10, 3)
