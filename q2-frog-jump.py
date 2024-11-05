class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """    
        n = len(stones)
        reach_jumps = [[0]]
        for i in range(1,n):
            r2 = []
            for j in range(0,i):
                dist = stones[i] - stones[j]
                r = reach_jumps[j]
                for k in range(len(r)):
                    if abs(dist - r[k]) <= 1:
                        r2.append(dist)
                        break
            reach_jumps.append(r2)
        
        if len(reach_jumps[n-1]) > 0:
            return True
        else:
            return False

            
# Test Cases 
print('Test A')
testa = Solution()
resulta = testa.canCross([0,1,2,3,4,8,9,11])
print(resulta)

print('\n\n')

print('Test B')
testb = Solution()
resultb = testb.canCross([0,1,3,5,6,8,12,17])
print(resultb)