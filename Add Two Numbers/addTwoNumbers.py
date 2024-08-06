# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        carry = 0
        tail = temp
        while l1 is not None or l2 is not None or carry != 0:
            d1 = l1.val if l1 is not None else 0
            d2 = l2.val if l2 is not None else 0
            summ = d1+d2+carry
            d3 = summ % 10
            carry = summ // 10

            newNode = ListNode(d3)
            tail.next = newNode; tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result =  temp.next
        temp.next = None
        return result

def list_to_linkedlist(lst):
    head = ListNode(lst[0])
    current = head
    for number in lst[1:]:
        current.next = ListNode(number)
        current = current.next
    return head

def linkedlist_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

def test_add_two_numbers():
    solution = Solution()
    
    # Test case 1: Simple case
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [7, 0, 8], "Error: Test case 1 failed"
    
    # Test case 2: Different lengths
    l1 = list_to_linkedlist([9, 9])
    l2 = list_to_linkedlist([1])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0, 0, 1], "Error: Test case 2 failed"
    
    # Test case 3: With carry
    l1 = list_to_linkedlist([1])
    l2 = list_to_linkedlist([9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0, 0, 0, 1], "Error: Test case 3 failed"
    
    # Test case 4: Both lists are empty
    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0], "Error: Test case 4 failed"
    
    # Test case 5: Both lists contain single digits
    l1 = list_to_linkedlist([5])
    l2 = list_to_linkedlist([5])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0, 1], "Error: Test case 5 failed"

    print("All test cases passed")

# Call the test function
test_add_two_numbers()