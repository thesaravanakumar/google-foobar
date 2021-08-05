def find_parent(node, root, size):
    """
    Recurse the current branch to find the parent node.

           7
         3   6
        1 2 4 5

    Assumptions:
    1. Root is the larget node in the tree
    2. Right branch is root - 1
    3. Left branch is right - size
    4. Next branch size is size / 2
    """

    # Check node is in range
    if node < 1 or node >= root:
        return -1

    # Get left and right branch
    right = root - 1
    left = right - size

    # Return root if node is left or right branch 
    if node in (left, right):
        return root

    # Determine which branch to traverse
    # - branch left if node < left
    # - branch right if node > left
    branch = left if node < left else right

    # Search branch for parent node
    return find_parent(node, branch, size >> 1)


def solution(h, q):
    """
    Return the list of parent nodes for each element in q.

    Assumptions:
    - h is the height of the tree, in the range 1..30
    - root of the tree is 2^h - 1
    - q is the list of nodes (1..10000 nodes)
    - p is the list of parent nodes (1..10000 nodes)
    """
    # Check h and q are within bounds
    if h < 1 or h > 30 or len(q) < 1 or len(q) > 10000:
        return

    # Root is 2^h - 1
    root = 2 ** h - 1

    # Size is root / 2
    size = root >> 1

    # Get the list of parent nodes for each element in q
    p = [find_parent(node, root, size) for node in q]
    
    return p
