class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    
        height_peak = max(height)
        n = len(height)
        water_trapped = 0
        for j in range(height_peak):
            level_trapped = 0
            puddle = 0
            trap_left = False
            for i in range(n):
                if height[i] > 0:
                    if trap_left:
                        level_trapped += puddle
                        puddle = 0
                    trap_left = True
                    height[i] -= 1
                else:
                    if trap_left:
                        puddle += 1
            water_trapped += level_trapped
        return(water_trapped)




print('Test A')   
testa = Solution()
testa.trap([0,1,0,2,1,0,1,3,2,1,2,1])

print('\n\n')
print('Test B')   
testb = Solution()
testb.trap([4,2,0,3,2,5])


        

