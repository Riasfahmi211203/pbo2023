class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_node(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert_node(root.left, key)
    elif key > root.key:
        root.right = insert_node(root.right, key)
    return root

def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = find_min_value(root.right)
        root.right = delete_node(root.right, root.key)
    return root

def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def search_node(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search_node(root.left, key)
    return search_node(root.right, key)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

# Fungsi menu
def print_menu():
    print("\nMenu:")
    print("1. Tambah Node")
    print("2. Hapus Node")
    print("3. Cari Node")
    print("4. Tampilkan Inorder")
    print("5. Keluar")

# Program utama
root = None

while True:
    print_menu()
    choice = input("Pilih menu (1-5): ")

    if choice == "1":
        value = int(input("Masukkan nilai untuk ditambahkan: "))
        root = insert_node(root, value)
        print("Node dengan nilai", value, "telah ditambahkan.")

    elif choice == "2":
        value = int(input("Masukkan nilai untuk dihapus: "))
        if search_node(root, value):
            root = delete_node(root, value)
            print("Node dengan nilai", value, "telah dihapus.")
        else:
            print("Node dengan nilai", value, "tidak ditemukan.")

    elif choice == "3":
        value = int(input("Masukkan nilai yang dicari: "))
        if search_node(root, value):
            print("Node dengan nilai", value, "ditemukan.")
        else:
            print("Node dengan nilai", value, "tidak ditemukan.")

    elif choice == "4":
        print("Tampilkan Inorder:")
        inorder_traversal(root)
        print()

    elif choice == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-5.")
