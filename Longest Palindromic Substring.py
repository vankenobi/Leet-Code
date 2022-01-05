""" class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[0]:
                state = False
                break
            else:
                state = True
        if state == True:
            return s

        for i in range(len(s)):
            for k in range(i+1,len(s)):
                if (s[i] == s[k]):
                    result = s[i:k+1] 
                    return result
        return s[0]         


s1 = Solution()
result = s1.longestPalindrome("aaa")
print(result)         """


from typing import List

class Solution(object):

    def longestPalindrome(self, s):

        potentialPalindrome = []
        palindrome = []

        for i in range(len(s)):
            for k in range(i+1,len(s)):
                if(s[i] == s[k]):
                    potentialPalindrome.append(s[i:k+1])     

        if len(s) == 1:
            return s
        if len(s) == 2 and s[0] == s[1]:
            return s
        if len(s) == 2 and s[0] != s[1]:
            return s[0]

        for i in range(len(potentialPalindrome)):
            count = 0
            value = potentialPalindrome[i]
            loop = round(len(value)/2)
            
            while(loop != count):
                if(value[0] == value[len(value)-1]):
                    value = value[1:len(value)-1]
                    count += 1

                else:
                    palindrome.append(potentialPalindrome[i])
                    break

        result = list(set(potentialPalindrome) - set(palindrome))
        result = max(result,key=len)
        return result

                                     
            

s1 = Solution()
result = s1.longestPalindrome("abcda")
print(result)