


class Solution(object):
    def removeDuplicates(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        result  = []
        for i in nums:
            result.append(sorted(set(i)))
            len_of_list = len(nums)

        return result

s1 = Solution()
result = s1.removeDuplicates([[1,1,2]])
print(result)
        