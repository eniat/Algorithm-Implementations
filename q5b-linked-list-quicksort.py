

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getTail(head):
    while head and head.next:
        head = head.next
    return head


def LomutosPartition (head, tail):

    pivot = tail
    prev = None
    curr = head

    # Partition the list around the pivot
    while curr != pivot:
        if curr.val < pivot.val:
            if prev is None:
                prev = head
            else:
                prev = prev.next
            # swap the values
            curr.val, prev.val = prev.val, curr.val

        curr = curr.next

    # final swap
    if prev is None:
        prev = head
    else:
        prev = prev.next
    pivot.val, prev.val = prev.val, pivot.val

    return prev

def quickSort(head):

    if head is None:
        return None

    tail = getTail(head)

    quicksortHelper( head, tail)
    return head

def quicksortHelper(head, tail):

    if head is None or head == tail:
        return

    pivot = LomutosPartition(head, tail)

    # Recursively sort the left partition
    if head != pivot:
        temp = head
        while temp.next != pivot:
            temp = temp.next
        temp.next = None
        quicksortHelper(head, temp)
        temp.next = pivot
    # recursively sort the right partition
    quicksortHelper(pivot.next, tail)



head = ListNode(123)
head.next = ListNode(78)
head.next.next = ListNode(43)
head.next.next.next = ListNode(123)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(123)
head.next.next.next.next.next.next = ListNode(23)
head.next.next.next.next.next.next.next = ListNode(43)


curr = quickSort(head)

while curr:
    print(curr.val, end=" ")
    curr = curr.next
print("\n")


