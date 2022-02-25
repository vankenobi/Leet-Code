class Solution(object):
    def lengthOfLastWord(self, s):
        list_of_s = s.split()
        for i in list_of_s[::-1]:
            if(i.isalpha() == True):
                return len(i)
            
s1 = Solution()  
result = s1.lengthOfLastWord("   fly me   to   the moon  ")
print(result)

# You can see the question from this link
# https://leetcode.com/problems/length-of-last-word/submissions/