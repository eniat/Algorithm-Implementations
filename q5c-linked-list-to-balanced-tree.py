

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def getTail(self,head):
        while head and head.next:
            head = head.next
        return head

    def LomutosPartition(self, head, tail):
        pivot, prev, curr = tail, None, head
        while curr != pivot:
            if curr.val < pivot.val:
                if prev is None:
                    prev = head
                else:
                    prev = prev.next
                curr.val, prev.val = prev.val, curr.val
            curr = curr.next
        if prev is None:
            prev = head
        else:
            prev = prev.next
        pivot.val, prev.val = prev.val, pivot.val
        return prev

    def quickSort(self, head):
        if head is None:
            return None
        tail = self.getTail(head)
        self.quicksortHelper(head, tail)
        return head

    def quicksortHelper(self, head, tail):
        if head is None or head == tail:
            return
        pivot = self.LomutosPartition(head, tail)
        if head != pivot:
            temp = head
            while temp.next != pivot:
                temp = temp.next
            temp.next = None
            self.quicksortHelper(head, temp)
            temp.next = pivot
        self.quicksortHelper(pivot.next, tail)

    def findMiddle(self, head):

        prev, slow, fast = None, head, head

        # Move slow 1 step and fast 2 steps
        while fast and fast.next:
            # store the node before slow for splitting the list
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Disconnect the first half from list
        if prev:
            prev.next = None
        # Return the middle node
        return slow

    def sortedListTOBST(self, head):

        # If list is empty return none
        if not head:
            return None

        # Find middle then make that the root of tree
        mid = self.findMiddle(head)
        root = TreeNode(mid.val)

        # If one in list return
        if head == mid:
            return root

        # recursively build the left subtree using left half of list
        root.left = self.sortedListTOBST(head)
        # recursively build the right subtree using right half of list
        root.right = self.sortedListTOBST(mid.next)

        return root


    def listToBST(self, head):

        # Sorts the list
        curr = self.quickSort(head)

        # Turns sorted list ino BST
        return self.sortedListTOBST(curr)



    def preorderTraversal(self, bst):

        # If not bst return empty array
        if not bst:
            return []
        # else traverse the left first then the right
        return [bst.val] + self.preorderTraversal(bst.left) + self.preorderTraversal(bst.right)


head = ListNode(123)
head.next = ListNode(78)
head.next.next = ListNode(43)
head.next.next.next = ListNode(123)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(123)
head.next.next.next.next.next.next = ListNode(34)
head.next.next.next.next.next.next.next = ListNode(123)
head.next.next.next.next.next.next.next.next = ListNode(123)

solution = Solution()
bst = solution.listToBST(head)
print(solution.preorderTraversal(bst))