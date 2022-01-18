from audioop import reverse


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        number_list = list(str(x))
        number_list.reverse()
        number_list = int("".join(number_list))
        if(x == number_list):
            return True
        else:
            return False
        

s1 = Solution()

result = s1.isPalindrome(-151)
print(result)