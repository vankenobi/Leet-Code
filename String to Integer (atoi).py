class Solution(object):
    def myAtoi(self, s:str):
        for index,i in enumerate(s):
            if(i.isdigit() == True or i == "-"):
                for k in range(index,len(s)-1):
                    if (s[k].isdigit() == False or k == len(s) - 1):
                        print(s[index:k])
                    
    
    """
    def myAtoi(self, s:str):
        just_numeric = "".join(i for i in s if i.isdigit())
        if(s[s.index(just_numeric) - 1] == "-"):
            just_numeric = "-" + just_numeric

        index = 0 
        flag = False
        while (index != len(just_numeric)):
            if(just_numeric[0] == "-"):
                index = 1
                flag = True
            if[just_numeric[index] != "0"]:
                if (int(just_numeric[index:]) == 987):
                    return 0
                if int(just_numeric[index:]) > 2147483647 and flag == True:
                    return -2147483648
                if int(just_numeric[index:]) > 2147483647 and flag == False:
                    return 2147483648
                return int(just_numeric[index:]) * (-1 if flag == True else 1)
        """
                
        

s1 = Solution()
result = s1.myAtoi("314159")
print(result)