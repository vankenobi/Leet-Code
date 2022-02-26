# 4009
# 4099
# 4999
# 99
# 9

class Solution(object):
    def plusOne(self, digits):
        if(digits[-1] != 9):
            digits[-1] = digits[-1] + 1
            return digits
        else:
            for i in range(len(digits)-1,-1,-1):
                if(digits[i] != 9):
                    digits[i] += 1
                    return digits  
                if(digits[i] == 9 and i == 0 ):
                    digits[i] = 0
                    digits.insert(0,1)
                    return digits                    
                if(digits[i] == 9):
                    digits[i] = 0
                
                     
s1 = Solution()

result = s1.plusOne([4,0,9,9])
print(result)

# You can see the question from this link 
# https://leetcode.com/problems/plus-one/