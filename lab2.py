class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_curl = 0
        left_rect = 0
        left_curv = 0
        count = len(s) - 1
        s = list(s.replace(" ",""))
        while(count != 0):
            if (s.pop() == "}"):
                left_curl +=1
            if (s.pop() == "]"):
                left_curl +=1
            if (s.pop() == "]"):
                left_curl +=1    

s1 = Solution()
result = s1.isValid('{ { } [ ] [ [ [ ] ] ] }')



