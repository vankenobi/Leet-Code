a = "100"
b = "110010"

class Solution(object):
    def addBinary(self, a, b):
        len_a = len(a)
        len_b = len(b)
        carry = 0
        result = ""

        if(int(a) == 0 and int(b) == 0):
            return "0"
        if(len_a - len_b < 0):
            a = abs(len_a - len_b) * "0" + a
        if(len_b - len_a < 0):
            b = abs(len_b - len_a) * "0" + b

        for i in range(-1,-1*len(b)-1,-1):
            summary = carry + int(a[i]) + int(b[i])
            if(summary == 1):
                result = str(1) + result 
                carry = 0
            elif(summary == 0):
                result = str(0) + result 
                carry = 0
            elif(summary == 2):
                result = str(0) + result 
                carry = 1
            elif(summary == 3):
                result = str(1) + result 
                carry = 1
            if(carry == 1 and i == -1 * len(a)):
                result = str(1) + result

        return result       
            
s1 = Solution()
result = s1.addBinary(a,b)

print(result)

# You can see the question from this link 
# https://leetcode.com/problems/add-binary/submissions/