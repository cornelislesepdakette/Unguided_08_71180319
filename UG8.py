class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class ArrayQueue:
    DEFAULT_CAPACITY = "" #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
       pass
       self._namapelanggan = None
       self._size = 0
       
    def __len__(self): #mengembalikan ukuran Queue
        pass
        return self._namapelanggan

    def is_empty(self): #mengecek apakah Queue kosong ?
        pass
        if self._namapelanggan == 0:
            return True
        else:
            return False

    def dequeue(self): #menghapus data paling depan (front)
        pass
        if self.is_empty() == False:
            hapus = self._head
            if self._size == 1:
                self._head = None
            else:
               self._head = self._head._next
                self._head._namapelanggan = None
            del hapus
            self._size = self._size - 1

    def enqueue(self, namaPelanggan): #menambah data ke list
        pass
        if self._namapelanggan == True:
            return None
        else:
            return tuple([self._head._size, self._head._namapelanggan])


    def resize(self, cap): #mengubah ukuran queue pada list
        pass
        return self._size[0]
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        pass
        if self._namapelanggan == True:
            print("### Melakukan Resize ###")
        else:
            bantu = self._head
            while bantu != None:
                print('(', bantu._size, ',', bantu._namapelanggan, ')', end=' ')
                bantu = bantu._next
            print()

print("==== Kasir =====")
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

