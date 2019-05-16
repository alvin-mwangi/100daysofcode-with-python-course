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
<<<<<<< HEAD
# issues: doesn't work if larger island/substring can be found starting from middle of one of the islands
# example: dvdf: islands: 'dv' and 'df'
# however, larger island/substring possible starting from 'v' 
# (within first island): 'd' and 'vdf'
# how to check this? 
# solutions: 
#     find substrings of max length and work backward? 
#        --- doesn't work if substring is at start of string 
#         -- e.g., 'anviaj' => 'anvi' 
#     sliding window approach?
#         - check susbtrings from start of string
#         - if string length > currentMax
#           examples:
#             input: 'anviaj'
#              1: anviaj' => 'anvi' 'aj', currentMax: 4
#              2: stringLength(5) > currentMax (4) 
#                 'nviaj' => 'nviaj', currentMax: 5
#              3: stringLength(5) == currentMax --> stop here and output the currentMax
#         
# 
#             input: 'dvdf'
#              1: dvdf => 'dv', 'df', currentMax: 2
#              2: stringLength(4) > currentMax(2)
#                'vdf' => 'vdf', currentMax(3)
#             3: stringLength(3) == currentMax --> stop here and output the currentMax
#         
=======
>>>>>>> parent of d160611... tempdict approach -- not working


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
    
        

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        highestMax = 0
        currentString = s
        while True:
            
            currentMax = self.findCurrentMax(currentString)
            if(currentMax > highestMax):
                highestMax = currentMax
            
            print(f"currentMax: {currentMax}")
            print(f"highestMax: {highestMax}")

            currentString = currentString[1:]
            if(len(currentString) <= highestMax):
                break

        return highestMax

            
        
    def findCurrentMax(self, s: str) -> int:

        letterDict = dict()
        substringList = list()
        substringLength = 0
        
        if(len(s) > 0):
            for i in s:
                if letterDict.get(i) == None:
                    letterDict[i] = 1
                    substringLength += 1
<<<<<<< HEAD
                    substringList.append([s[i], substringLength])
=======
                    substringList.append([i, substringLength])
>>>>>>> parent of d160611... tempdict approach -- not working

                # else case here
                else:
                    letterDict[i] += 1
                    substringLength = 1
<<<<<<< HEAD
                    substringList.append([s[i], substringLength])
            
                       
            # print(letterDict)
            # print(substringList)

            maxLen = max(j for i,j in substringList)
            return maxLen
                        
        else:
            return 0

if __name__ == "__main__":    
    #testString = "dvdj"
    # testString = "abcabcbb"
    testString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(testString))
=======
                    substringList.append([i, substringLength])
            
                       
            print(letterDict)
            print(substringList)

            # print results
            maxLen = max(j for i,j in substringList)
            print(maxLen)
            #return max(j for i,j in substringList) 
        else:
            return 0

if __name__ == "__main__":        
    sol = Solution()
    sol.lengthOfLongestSubstring("dvdf")


    

>>>>>>> parent of d160611... tempdict approach -- not working
