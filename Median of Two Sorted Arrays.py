from typing import List
class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        new_list = []
        new_list= nums1 + nums2
        new_list = sorted(new_list)
        remainder = len(new_list)%2

        if remainder == 0:
            result = new_list[int(len(new_list)/2)-1] + new_list[int(len(new_list)/2)]
            result /= 2
        else:
            result = int(len(new_list)/2) + 1 
        return result    

s1 = Solution()
result = s1.findMedianSortedArrays([1,2],[3,4]) 
print(result)
