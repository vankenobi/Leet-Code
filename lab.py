import this
from typing import List

class Solution(object):
    def intToRoman(self, num):
        thisdict = {0:"",1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        result  = ""
        list_of_num = list(str(num))
        list_dict_keys = thisdict.keys()
        
        for i in range(0,len(list_of_num)):
            step_value = int(list_of_num[i])         
            if(step_value in list_dict_keys):
                result = result + thisdict.get(step_value)
            else:
                for index,i in enumerate(thisdict):
                    if(i > step_value):
                        remainder = i-step_value
                        
                        
        
        return result 


        """
        for i in range(len(num),1):
            int(list_of_num[len(num)-i]) * (10**(i-1))
        """
        """
        for i in range(3):
            if(num % dividing == remainder):
                return thisdict.get(dividing - remainder) + thisdict.get(dividing)
            else:
                remainder *= 10
                dividing *= 10
        """
        

s1 = Solution()
result = s1.intToRoman(58)
print(result)