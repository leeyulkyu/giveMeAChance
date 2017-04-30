def solution (ll, key):
    cur = ll.getHead()
    pre = None
    post = None
    while cur is not None:
        if cur.val != key:
            if cur.val > key:
                if post is None:
                    post = LindedList(cur.val)
                else:
                    post.add(cur.val)
            elif cur.val < key:
                if pre is None:
                    pre = LinkedList(cur.val)
                else:
                    pre.add(cur.val)
        cur = cur.next

    cur = pre.getHead()
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(key)
    cur.next.next = post.getHead()
    return pre.printlist()