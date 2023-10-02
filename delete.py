from search import Tree

def delete_list(T,value):
    if T == None:
        return
    if T.key == value:
        T.parent.left = None
        T.parent.right = None
    if value > T.key:
        delete_list(T.right, value)
    else:
        delete_list(T.left, value)

def delete_with_one_child(T, value):
    if T == None:
        return
    #а что если удалим корень с одним ребенком?
    if T.key == value and T.left == None and T.right != None and T.parent.right == T:
        tmp = T.parent
        if T.parent.right == T:
            tmp.right.right = T.right
        else:
            tmp.left.right = T.right

    if T.key == value and T.left != None and T.right == None and T.parent.right == T:
        tmp = T.parent
        if  T.parent.right == T:
            tmp.right.left = T.left
        else:
            tmp.left.left = T.left
    T = None
