# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        
        minSize = min(l1Size, l2Size)
        
        elementCounter = 0
        maxCount = minSize
        
        currL1 = l1
        currL2 = l2
        carryOne = False
        
        outputList = ListNode()
        
        while(elementCounter < maxCount):
            
            currTotal = currL1.val + currL2.val
            
            if carryOne:
                currTotal += 1
                
            if currTotal >= 10:
                carryOne = True
                outputDigit = currTotal % 10
            else:
                outputDigit = currTotal
            
            insertPoint = outputList
            while(insertPoint.next != None):
                insertPoint = insertPoint.next
            
            insertPoint.next = ListNode(outputDigit)
            
            elementCounter += 1
        
        