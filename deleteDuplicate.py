def deleteDuplicate(self):
    cur = self.head
    dict = {}
    prev = None

    while cur is not None:
        if cur.val in dict:
            prev.next = cur.next
        else:
            dict[cur.val] = True
            prev = cur
        cur = cur.next