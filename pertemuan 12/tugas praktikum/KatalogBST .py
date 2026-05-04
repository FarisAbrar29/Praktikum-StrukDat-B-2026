class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul   = judul
        self.left    = None
        self.right   = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, id_buku, judul, node=None, mulai=True):
        if mulai:
            node = self.root
        if self.root is None:
            self.root = Node(id_buku, judul)
        elif id_buku < node.id_buku:
            if node.left is None:
                node.left = Node(id_buku, judul)
            else:
                self.insert(id_buku, judul, node.left, False)
        elif id_buku > node.id_buku:
            if node.right is None:
                node.right = Node(id_buku, judul)
            else:
                self.insert(id_buku, judul, node.right, False)
        if mulai:
            print(f" INSERT -> Berhasil memasukkan: ID {id_buku} - {judul}")

    # SEARCH
    def search(self, id_buku):
        print(f" SEARCH -> Mencari ID {id_buku}...", end=" ")
        hasil = self._cari(id_buku, self.root)
        print(f"Ditemukan Judul: {hasil.judul}" if hasil else "Data tidak ditemukan.")

    def _cari(self, id_buku, node):
        if node is None: return None
        if id_buku == node.id_buku: return node
        return self._cari(id_buku, node.left if id_buku < node.id_buku else node.right)

    # IN-ORDER TRAVERSAL
    def traversal_inorder(self, node=None, hasil=None, mulai=True):
        if mulai:
            node, hasil = self.root, []
            print("\n INFO -> Koleksi Buku (InOrder Traversal):")
        if node:
            self.traversal_inorder(node.left, hasil, False)
            hasil.append(node)
            self.traversal_inorder(node.right, hasil, False)
        if mulai:
            for i, n in enumerate(hasil, 1):
                print(f"  {i}. {n.id_buku} - {n.judul}")

    # GET MIN
    def get_min(self):
        node = self.root
        while node.left: node = node.left
        return node

    # GET MAX
    def get_max(self):
        node = self.root
        while node.right: node = node.right
        return node

    # HEIGHT
    def height(self, node=None, mulai=True):
        if mulai: node = self.root
        if node is None: return -1
        return 1 + max(self.height(node.left, False), self.height(node.right, False))


# MAIN
print(' ---SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"--- ')


katalog = BST()
katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")

katalog.traversal_inorder()

print()
katalog.search(60)
katalog.search(100)


mn, mx = katalog.get_min(), katalog.get_max()
print(f"\n STATISTIK -> ID Terkecil : {mn.id_buku} - {mn.judul}")
print(f" STATISTIK -> ID Terbesar : {mx.id_buku} - {mx.judul}")
print(f"\n INFO ->Tinggi (Height) Tree: {katalog.height()}")

print("Simulasi Selesai")