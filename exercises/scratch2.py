# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLength(self, inputList: ListNode):
        # find size of each list 
        current = inputList
        sizeCounter = 0
        
        while(current != None):
            sizeCounter += 1
            current = current.next
        
        return sizeCounter
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find size of each list 
        l1Size = self.getLength(l1)
        l2Size = self.getLength(l2)
        
        print(f"l1 length: {l1Size}")
        print(f"l2 length: {l2Size}")
        
        maxSize = max(l1Size, l2Size)
        minSize = min(l1Size, l2Size)
        
        elementCounter = 0
        maxCount = maxSize
        print(f"maxCount: {maxCount}")
        
        currL1 = l1
        currL2 = l2
        carryOne = False
                
        while(elementCounter < maxCount):

            #curr1Val = currL1.val if currL1 != None else 0
            #curr2Val = currL2.val if currL2 != None else 0
            currTotal = currL1.val + currL2.val
            
            if carryOne:
                currTotal += 1
                
            if currTotal >= 10:
                carryOne = True
                outputDigit = currTotal % 10
            else:
                carryOne = False
                outputDigit = currTotal
            
            if(elementCounter == 0):
                outputList = ListNode(outputDigit)
            else:
                insertPoint = outputList

                while(insertPoint.next != None):
                    insertPoint = insertPoint.next
                
                insertPoint.next = ListNode(outputDigit)
                
            if(elementCounter + 1 == maxCount and carryOne):
                insertPoint = outputList

                while(insertPoint.next != None):
                    insertPoint = insertPoint.next

                insertPoint.next = ListNode(1)
                
            
            if(currL1.next == None):
                currL1.next = ListNode(0)
            
            if(currL2.next == None):
                currL2.next = ListNode(0)
                
            currL1 = currL1.next
            currL2 = currL2.next
            
            elementCounter += 1
         
        return outputList