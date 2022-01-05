class Solution:
    def addTwoNumbers(self, l1:list, l2:list):
        l1.reverse()
        l2.reverse()
        str1 = "".join(str(e) for e in l1)
        str2 = "".join(str(e) for e in l2)
        result_int = int(str2) + int(str1) 
        result_list = [int (e) for e in str(result_int)]
        result_list.reverse()
        print(result_list)

s1 = Solution()

s1.addTwoNumbers([2,4,3],[5,6,4]) 

