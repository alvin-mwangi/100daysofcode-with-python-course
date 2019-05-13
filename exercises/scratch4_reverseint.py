# Given a 32-bit signed integer, reverse digits of an integer.
# example: 
#       input:   123
#       output:  321

# convert int to string, 
# reverse string
# convert string to int
# Input
#   1534236469
# Output
#   9646324351
# Expected
#   0

class Solution:
    def reverse(self, x: int) -> int:
        #print(x)
        revStr = str(abs(x))[::-1] 
        maxInt = 2**31 - 1
        revInt = int(revStr)

        if(revInt > maxInt):
            return 0

        if(x < 0): 
            print(-1 * revInt)            
            return -1 * revInt
        
        return revInt

if __name__ == "__main__":
    sol = Solution()
    testInput = 1534236469
    print(sol.reverse(testInput))
