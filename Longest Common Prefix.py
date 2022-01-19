


from itertools import count


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        short_vocabulary = min(strs,key=len)
        strs.remove(short_vocabulary)
        count = 0
        if(len(short_vocabulary) == 0 ): 
            return short_vocabulary
        while(count < len(short_vocabulary)):
            char = short_vocabulary[count] 
            for i in strs:
                if(i[count] != char):
                    return short_vocabulary[:count]
            count +=1

        return short_vocabulary[:count]
        

s1 = Solution()
result = s1.longestCommonPrefix(["abab","aba",""])
print(result)