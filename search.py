class Tree:
    def __int__(self, parent = None, left = None, right = None, key = None):
        self.root = parent
        self.left = left
        self.right = right
        self.key = key



def search(t, value):
    if t == None:
        return None
    if t.key == value:
        return 1
    if t.key != value and t.left == None and t.right == None:
        return 0
    if value < t.key:
        search(t.left, value)
    if value > t.key:
        search(t.right, value)

def search_min(t):
    index_min = Tree()
    if t == None:
        return None
    index_min = t
    while index_min.left != None:
        index_min = index_min.left
    return index_min

