from search import Tree

def insert(T, value):
    if T == None:
        T.key = value
        return
    if value < T.parent.key:
        insert(T.parent.left, value)
    else:
        insert(T.parent.right, value)

