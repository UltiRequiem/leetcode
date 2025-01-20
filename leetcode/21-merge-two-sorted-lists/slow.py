from typing import Optional

# runtime: O(nlogn), space: O(n), where n is the total number of nodes in the two lists
class ListNode:
          def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals = []

        while list1:
            vals.append(list1.val)
            list1 = list1.nexts

        while list2:
            vals.append(list2.val)
            list2 = list2.next

        vals.sort()

        answer = ListNode()
        current = answer

        for num in vals:
            current.next = ListNode(num)
            current = current.next


        return answer.next
      