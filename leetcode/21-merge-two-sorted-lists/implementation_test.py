import unittest
from implementation import Solution, ListNode

class TestDeleteDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_linkedlist(self, elements):
        head = ListNode(elements[0])
        current = head
        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next
        return head

    def linkedlist_to_list(self, head):
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        return elements

    def test_example_case(self):
        head = self.list_to_linkedlist([1, 1, 2])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2])

    def test_no_duplicates(self):
        head = self.list_to_linkedlist([1, 2, 3])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 3])

    def test_all_duplicates(self):
        head = self.list_to_linkedlist([1, 1, 1])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), [1])

    def test_mixed_duplicates(self):
        head = self.list_to_linkedlist([1, 1, 2, 3, 3])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
