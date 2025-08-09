

class Solution(object):

    def __init__(self, hp= None):
        if hp is not None:
            self.result = self.lastRobotHP(hp)
            print(self.result)

    def maxHeap(self, A, n):

        for i in range(n):
            if A[i] > A[int((i - 1) / 2)]:
                j = i

                # Swap until parent is smaller than child
                while A[j] > A[int((j - 1) /2)]:
                    (A[j], A[int((j - 1)/2)]) = (A [int((j - 1) / 2)],A[j])
                    j = int( (j - 1) / 2)

    def heapifyUp(self, A, i):

            while i >0:
                parent = (i -1)//2
                if A[i] > A[parent]:
                    A[i], A[parent] = A[parent], A[i]
                    i = parent
                else:
                    break

    def heapify(self, A, n, i):

        large = i  # sets Largest to root
        l = 2*i + 1
        r = 2*i + 2

        if l < n and A[l] > A[large]:
            # Checks if left child is larger if so sets it
            large = l

        if r < n and A[r] > A[large]:
            # Deos the same for right so far
            large = r

        if large != i:
            A[i], A[large] = A[large], A[i]
            # recursively heapify
            self.heapify(A, n, large)

    def lastRobotHP(self, hp):

        n =len(hp)

        if n == 0:
            return 0

        # Creates a max Heap from the array
        self.maxHeap(hp, n)

        while len(hp) > 1:

            # Get the top 2 values
            hp[0], hp[-1] = hp[-1], hp[0]
            first = hp.pop()
            self.heapify(hp, len(hp), 0)

            if not hp:
                return first

            hp[0], hp[-1]= hp[-1], hp[0]
            second = hp.pop()
            self.heapify(hp, len(hp), 0)

            # If hp is different subtract and put remaining back
            if first !=second:
                hp.append(first - second)
                # Maintain the Heap
                self.heapifyUp(hp,len(hp) - 1)

        return hp[0] if hp else 0

hp = [54, 1, 23, 66, 178, 51, 60, 32, 15, 91]
hp2 = [5,5,5,5]
hp3 = [7]
hp4 = [1000,5]
hp5 = []
solution = Solution(hp)
solution2 = Solution(hp2)
solution3= Solution(hp3)
solution4 = Solution(hp4)
solution5 = Solution(hp5)

