'''
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

             
Input: "pwkwew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''



# approach 1: using dictionary
# iterate through each letter in the string
# add letter to dictionary with entry {letter, index}
# 



# approach 2: gaps and islands solution
# similar to sql -- find biggest island
# use dictionary to keep track of letters we've seen
# if letter exists, reset counter (create a new island)
# otherwise, increment the counter 


'''
input: 'abcabcbb' 
output: 12311111

letterDict = dict()
substringDict = dict()
substringLength = 1

for i in input:
    if letterDict.get(i) == None:
        letterDict[i] = 1
        substringDict[i] = substringLength
        substringLength += 1
    else:
        l
        


dvdf

d = 1, 0
v = 2, 1
d = 1, 2
f = 2, 3


--for each substring of max length:
    -- if there are any where the endIndex > maxLength:
        populate dictionary with letters in substring
         for each letter in original string starting from index(endIndex - maxLength) and working down to 0:
             if letter not in dictionary, increment maxLength by 1
    


-----------------------------------------------------------------
--- Alt approach
...reverse the string and repeat the above
...if longest substring from reversed > forward, 

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        forwardMax = self.checkLongestSubstring(s)
        reverseMax = self.checkLongestSubstring(s[::-1])

        return max(forwardMax, reverseMax)
    
    def checkLongestSubstring(self, s: str) -> int:
        letterDict = dict()
        substringList = list()
        substringLength = 0
        
        if(len(s) > 0):
            for i in s:
                if letterDict.get(i) == None:
                    letterDict[i] = 1
                    substringLength += 1
                    substringList.append([i, substringLength])

                # else case here
                else:
                    letterDict[i] += 1
                    substringLength = 1
                    substringList.append([i, substringLength])
            
                       
            print(letterDict)
            print(substringList)

            # print results
            maxLen = max(j for i,j in substringList)
            #print(maxLen)
            #return max(j for i,j in substringList) 
            return maxLen

        else:
            return 0
        
        
if __name__ == "__main__":        
    sol = Solution()
    testStr = "asjrgapa"

    maxSubstrLen = sol.lengthOfLongestSubstring(testStr)
    
    print(maxSubstrLen)
