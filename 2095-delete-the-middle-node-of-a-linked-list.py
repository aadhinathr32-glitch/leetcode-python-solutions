class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        previous = None

        while fast is not None and fast.next is not None:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = slow.next
        return head


def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    solution = Solution()

    assert linked_list_to_list(
        solution.deleteMiddle(build_linked_list([1, 3, 4, 7, 1, 2, 6]))
    ) == [1, 3, 4, 1, 2, 6]

    assert linked_list_to_list(
        solution.deleteMiddle(build_linked_list([1, 2, 3, 4]))
    ) == [1, 2, 4]

    assert linked_list_to_list(
        solution.deleteMiddle(build_linked_list([2, 1]))
    ) == [2]

    assert solution.deleteMiddle(build_linked_list([1])) is None

    print("All sample tests passed.")
