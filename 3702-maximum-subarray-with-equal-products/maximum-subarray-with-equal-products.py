class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def maxLength(self, nums):
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                prod *= nums[j]

                if g == 0:
                    g = nums[j]
                else:
                    g = self.gcd(g, nums[j])

                l = self.lcm(l, nums[j])

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans