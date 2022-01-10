class Solution(object):
    def maxArea(self, height):
        maxArea = 0 
        l = 0
        r = len(height) - 1
        while(l<r):
            maxArea = max(maxArea,min(height[l],height[r]) * (r-l))
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return maxArea
        
                
s1 = Solution()
result = s1.maxArea([1,8,6,2,5,4,8,3,7])
print(result)

# You can access the link from this
# https://leetcode.com/problems/container-with-most-water/submissions/