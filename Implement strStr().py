class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        

s1 = Solution()
result = s1.strStr("hello","ll")
print(result)

# You can see the question from this link       
# https://leetcode.com/problems/implement-strstr/