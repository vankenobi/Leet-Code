class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        list_of_lenght = len(nums)
        for i in range(0,list_of_lenght-1):
            if(nums[i] == val):
                nums.pop(i)
                nums.append(0)
                count += 1
        return int(list_of_lenght-count),list(nums)

s1 = Solution()
result = s1.removeElement([3,2,2,3],3)
print(result)
