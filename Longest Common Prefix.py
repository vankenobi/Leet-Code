


from itertools import count


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        short_vocabulary = min(strs,key=len)
        count = 0
        if(len(short_vocabulary) == 0 ):
            return strs[0]
        while(count < len(short_vocabulary)):
            char = short_vocabulary[count] 
            for i in strs:
                if(i[count] != char):
                    return short_vocabulary[:count]
            count +=1
        

s1 = Solution()
result = s1.longestCommonPrefix(["a"])
print(result)