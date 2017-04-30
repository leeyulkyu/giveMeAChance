def kthElementFromlast(self,k):
    p1 = self.head
    p2 = self.head
    if k != 0:
        for i in range(k):
            p2 = p2.next
            # over flow k is greater than linkedList length
            if p2 is None:
                return None
        # run until p2 reach the end
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next
        # since p2 = p1 is tbe k, now p1 position is the kth from last node
        return p1.val