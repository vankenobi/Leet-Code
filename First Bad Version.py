from pickle import TRUE


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a =  [TRUE,TRUE,TRUE,TRUE,TRUE,FALSE,FALSE,FALSE]
        list_of_len = len(a) - 1

        result = None
        while(result == None):
            if(a[list_of_len/2] == False):
                
           
            