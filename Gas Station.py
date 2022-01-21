class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        potantial_begins = [] 
        circle = False
        count = 0
        list_of_lenght = len(gas) # You can write if you want cost. It doesnt matter
        for i in range(len(gas)):
            if(gas[i] - cost[i] > 0):
                potantial_begins.append(i)

        for i in potantial_begins:
            current_gas = 0
            count = 0 
            while(circle == True and count == list_of_lenght):
                
                

        return potantial_begins


s1 = Solution()
result  = s1.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
print(result)


        