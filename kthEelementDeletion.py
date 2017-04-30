def remove(self, item):
    if self.head.val == item:
        self.head = self.head.next
    else:
        cur = self.head
        while cur.next is not None:
            if cur.val == item:
                self.removeItem(item)
                return
        cur = cur.next
    print("item does not exist in linked list")



def removeItem(self,item):
    cur = self.head
    while cur.next is not None:
        if cur.next.val == item:
            nextnode = cur.next.next
            cur.next.next = None
            cur.next = nextnode
            break