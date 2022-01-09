class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for k in range(len(nums)):
                if(k != i and nums[k] + nums[i] == target):
                    return [i,k]


s1 = Solution()
result = s1.twoSum([2,7,11,15],9)
print(result)
                    
# You can see the question from this link
# https://leetcode.com/problems/two-sum/