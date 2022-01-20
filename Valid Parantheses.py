from pickletools import StackObject


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        count = 0
        s = s.replace(" ","")

        if (len(s) % 2 != 0):
            return False
        
        for i in s:
            if (i == '(' or i == '[' or i == '{'):
                 stack.append(i)
            elif(i == ')' and len(stack) != 0 and stack[-1] == '('):
                stack.pop()
                count +=1
            elif(i == ']' and len(stack) != 0 and stack[-1] == '['):
                stack.pop()
                count +=1
            elif(i == '}' and len(stack) != 0 and stack[-1] == '{'):
                stack.pop()
                count +=1

        return True if len(s) / 2  == count else False

s1 = Solution()
result = s1.isValid('([}}])') # instance case
print(result)

# You can see the question from this link 
# https://leetcode.com/problems/valid-parentheses/submissions/

