class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stairs_n = [0,0]
        for i in range(1,n+1): 
            if (i == 1):
                result = 1
            elif (i == 2):
                result = 2
            else:
                result = stairs_n[0] + stairs_n[1]
            stairs_n[0] = stairs_n[1]
            stairs_n[1] = result

        print(stairs_n)
        return(stairs_n[1])

# Test Cases

test = Solution()
test.climbStairs(10)