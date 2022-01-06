class Solution(object):
    def carPooling(self, trips, capacity):
        _to = []
        _from = []
        for i in range(len(trips)):
            _to.append(trips[i][2])
            _from.append(trips[i][1])
        _to = list(set(_to))
        _from = list(set(_from))

        max_to = max(_to)
        max_from = max(_from)

        min_to = min(_to)
        min_from = min(_from)

        live_capacity = 0

        for i in range(min_from,max_to):
            for j in range(len(trips)):
                if (trips[j][2] == i):
                    live_capacity -= trips[j][0]
            for k in range(len(trips)):
                if (trips[k][1] == i) :
                    live_capacity += trips[k][0]
                if (capacity < live_capacity):
                    return False
                
                
        return True

s1 =  Solution()
result = s1.carPooling([[4,5,6],[6,4,7],[4,3,5],[2,3,5]],13)
print(result)

# You can see the question from this link 
# https://leetcode.com/problems/car-pooling/