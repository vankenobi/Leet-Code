from operator import indexOf


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return indexOf(nums,target)
        else:
            if (nums[-1] < target):
                return len(nums)
            for i in range(len(nums)):
                if(nums[i] > target):
                    return i
        
        

s1 = Solution()
result = s1.searchInsert([1,3,5,6], 4)
print(result)

# If you want you can see to this question from this link:
# https://leetcode.com/problems/search-insert-position/