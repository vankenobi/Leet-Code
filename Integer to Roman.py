from typing import List


class Solution(object):
    def intToRoman(self, num):
        thisdict = {0:"",1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        dividing = 5
        remainder = 4
        result  = ""
        list_of_num = list(str(num))
        list_dict_keys = thisdict.keys()
        for i in range(len(list_of_num),0,-1):
            step_value = int(list_of_num[len(list_of_num) - i])         
            value = step_value * (10**(i-1))
            value2 = value%(5*(10**(i-1)))
            if (value2 == 4*(10**(i-1))) or value2 == 9*(10**(i-1)):
                result = thisdict.get((5*(10**(i-1)))-value2) + thisdict.get(5*(10**(i-1)))
            else:
                if (step_value * 10**(i-1) in list_dict_keys):
                    result = result + str(thisdict.get(step_value * 10**(i-1)))
                else:
                    for k in range(0,len(list_dict_keys)-1):
                        if(list_dict_keys[k] > (10**(i-1) * step_value)):
                            pass
                            #result = result + 
                            
                    # buraya güncelleme gelecek 
                    result = result + thisdict.get((10**(i-1))) * step_value 
        
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