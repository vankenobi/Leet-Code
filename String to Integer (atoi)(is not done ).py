class Solution(object):
    def myAtoi(self, s):
        just_number = 0

        for i in range(len(s)):
            if(s[i].isalpha() == True or s[i] == "."):
                return 0
            if (len(s) == 1 and s.isdigit() == False):
                return 0
            if(s[i].isdigit() == True):
                start_index = i
                break
            if (s[i] == "-" and s[i+1].isdigit() == True):  
                if(s[i-1] == "+"):
                    return 0
                if (s[i+1].isdigit() == True):
                    start_index = i
                    break
            if ((s[i] == "+" and s[i+1].isdigit() == True) or ((s[i] == "+" and s[i+1] == "-") )):     
                if(s[i-1] == "-"):
                    return 0
                if(s[i+1] == "+"):
                    return 0
                if (s[i+1].isdigit() == True):
                    start_index = i+1
                    break
                break
        
        if(s == ""):
            return 0

        for i in range(start_index,len(s)):
            if (s[i] != "-" and s[i].isdigit() == False):
                just_number = int(s[start_index:i])
                break
            elif i+1 == len(s):
                just_number = int(s[start_index:])
                break
        
        if(just_number > 2147483647):
            return 2147483648
        if(just_number < -2147483648):
            return -2147483648

        return just_number
            
            
        

            
                    
    
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
                
# + - . -541+   **        

s1 = Solution()
result = s1.myAtoi("+-")
print(result)