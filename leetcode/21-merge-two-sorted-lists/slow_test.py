import unittest
from slow import Solution, ListNode

class TestMergeTwoLists(unittest.TestCase):
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
        list1 = self.list_to_linkedlist([1, 2, 4])
        list2 = self.list_to_linkedlist([1, 3, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_empty_lists(self):
        list1 = self.list_to_linkedlist([])
        list2 = self.list_to_linkedlist([])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linkedlist_to_list(result), [])

    def test_one_empty_list(self):
        list1 = self.list_to_linkedlist([1, 2, 3])
        list2 = self.list_to_linkedlist([])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 3])

    def test_no_overlap(self):
        list1 = self.list_to_linkedlist([1, 2, 3])
        list2 = self.list_to_linkedlist([4, 5, 6])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 3, 4, 5, 6])

    def test_all_overlap(self):
        list1 = self.list_to_linkedlist([1, 1, 1])
        list2 = self.list_to_linkedlist([1, 1, 1])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 1, 1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()
