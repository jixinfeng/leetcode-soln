class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def put(self, x):
        if x == self.val:
            return
        elif x < self.val:
            if self.left:
                self.left.put(x)
            else:
                self.left = TreeNode(x)
        else:
            if self.right:
                self.right.put(x)
            else:
                self.right = TreeNode(x)

    def findMin(self, parent):
        if self.left:
            return self.left.findMin(self)
        else:
            return [parent, self]

    def delete(self, x):
        if x == self.val:
            if self.left and self.right:
                parent, succ = self.findMin(self)
                if parent.left == succ:
                    parent.left = succ.right
                else:
                    parent.right = succ.right
                succ.left = self.left
                succ.right = self.right
                return succ
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if x < self.val:
                if self.left:
                    self.left = self.left.delete(x)
            else:
                if self.right:
                    self.right = self.right.delete(x)
        return self


class BST(object):
    def __init__(self, data=None):
        self.root = None
        if data:
            for x in data:
                if self.root:
                    self.root.put(x)
                else:
                    self.root = TreeNode(x)

    def put(self, x):
        if self.root:
            self.root.put(x)
        else:
            self.root = TreeNode(x)

    def delete(self, x):
        if self.root:
            self.root.delete(x)

    def toList(self, order=0):
        """
        -1: preorder traversal
         0: inorder traversal
         1: postorder traversal
        """
        if order == -1:
            return self.preorder(self.root, [])
        elif order == 0:
            return self.inorder(self.root, [])
        else:
            return self.postorder(self.root, [])

    def toString(self, order=0, sep=' '):
        """
        -1: preorder traversal
         0: inorder traversal
         1: postorder traversal
        """
        strList = [str(x) for x in self.toList(order)]
        return str(sep).join(strList)

    def preorder(self, loc, ans):
        if loc is None:
            return []
        ans += [loc.val]
        ans += self.preorder(loc.left, [])
        ans += self.preorder(loc.right, [])
        return ans

    def inorder(self, loc, ans):
        if loc is None:
            return []
        ans += self.inorder(loc.left, [])
        ans += [loc.val]
        ans += self.inorder(loc.right, [])
        return ans

    def postorder(self, loc, ans):
        if loc is None:
            return []
        ans += self.postorder(loc.left, [])
        ans += self.postorder(loc.right, [])
        ans += [loc.val]
        return ans


if __name__ == "__main__":
    a = BST([2, 1, 3])
    print(a.toList())
