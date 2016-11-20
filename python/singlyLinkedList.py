class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class singlyLinkedList(object):
    def __init__(self, data = None):
        """
        data: list()
        """
        self.head = None
        if data:
            for x in data:
                self.addTail(x)

    def isEmpty(self):
        return self.head is None

    def addHead(self, x):
        newHead = ListNode(x)
        newHead.next = self.head
        self.head = newHead

    def addTail(self, x):
        if self.head:
            p = self.head
            while p.next:
                p = p.next
            p.next = ListNode(x)
        else:
            self.head = ListNode(x)

    def insertAfter(self, loc, x):
        newNode = ListNode(x)
        newNode.next = loc.next
        loc.next = newNode

    def size(self):
        p = self.head
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def search(self, x):
        """
        return pointer to the first node with val x or None
        """
        p = self.head
        while p:
            if x == p.val:
                return p
            else:
                p = p.next
        return None

    def delete(self, x):
        q = ListNode(None)
        q.next = self.head
        p = q
        while p.next:
            if p.next.val == x:
                p.next = p.next.next
                break
            else:
                p = p.next

    def isEqualTo(self, y):
        p = ListNode(None)
        p.next = self.head
        q = p.next

        r = ListNode(None)
        r.next = y.head
        s = r.next
        
        while q and s:
            if q.val == s.val:
                q = q.next
                s = s.next
            else:
                return False
        return q is None and s is None

    def toList(self):
        ans = []
        p = self.head
        while p:
            ans.append(p.val)
            p = p.next
        return ans
    
    def toString(self, sep=' '):
        return str(sep).join(list(map(str, self.toList())))

    def printNodes(self, sep=''):
        print(self.toString(sep))

if __name__ == "__main__":
    print("----------")
    print("singly linked list [1,2,3,3,4,5]")
    a = singlyLinkedList([1,2,3,3,4,5])
    a.printNodes()
    print("delete a element")
    a.delete(3)
    a.printNodes()
    print("----------")
    print("singly linked list [2,4]")
    b = singlyLinkedList([2,4])
    b.printNodes()
    print("add element at head")
    b.addHead(1)
    b.printNodes()
    print("add element at tail")
    b.addTail(5)
    b.printNodes()
    print("insert element at middle")
    c = b.search(2)
    b.insertAfter(c, 3)
    b.printNodes()
    print("compare two slls")
    print(a.isEqualTo(b))
