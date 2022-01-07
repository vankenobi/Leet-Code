
class Solution(object):
    def reverse(self, x):
        x = list(str(x)) 
        flag = False

        if(x[0] == "-"):
            flag = True
            x.pop(0)
        if (len(x) == 1):
            return int("".join(x))

        x.reverse()
        count = 0
            
        while(count != len(x)-1):
            if(x[count] != 0):
                if (flag == True):
                    x = int("".join(x[count:])) * -1
                else:
                    x = int("".join(x[count:]))

            if(abs(x) > 2**31-1):
                return 0    
            return x
                
            count += 1 
    
           
s1 = Solution()
result = s1.reverse(1534236469)
print(result)

# You can see the question from this link 
# https://leetcode.com/problems/reverse-integer/
