class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def delete_node(root, key):
    if root is None:
        return root

    # Temukan node yang akan dihapus
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # Node dengan satu anak atau tanpa anak
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node dengan dua anak, temukan penerus inorder (node terkecil pada subpohon kanan)
        root.key = find_min_value(root.right)

        # Hapus node penerus inorder
        root.right = delete_node(root.right, root.key)

    return root

def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

# Contoh penggunaan
# Buat pohon contoh
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

# Cetak pohon sebelum penghapusan
print("Pohon sebelum penghapusan:")
# Implementasi fungsi cetak pohon inorder
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root)
print()

# Hapus node dengan nilai 30
root = delete_node(root, 30)

# Cetak pohon setelah penghapusan
print("Pohon setelah penghapusan:")
inorder_traversal(root)
