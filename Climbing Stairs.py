class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fibonacci(n + 1)

    def fibonacci(self,n):
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)        
    
    
s1 = Solution()
result = s1.climbStairs(4)
print(result)