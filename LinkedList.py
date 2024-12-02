class LinkedList:
    def __init__(self, nilai1, nilai2, nilai3, nilai4):
        # Membuat simpul pertama
        self.kepala = {'nilai': nilai1, 'berikutnya': None}
        
        # Membuat simpul kedua dan menghubungkannya
        simpul2 = {'nilai': nilai2, 'berikutnya': None}
        self.kepala['berikutnya'] = simpul2
        
        # Membuat simpul ketiga dan menghubungkannya
        simpul3 = {'nilai': nilai3, 'berikutnya': None}
        simpul2['berikutnya'] = simpul3
        
        # Membuat simpul keempat dan menghubungkannya
        simpul4 = {'nilai': nilai4, 'berikutnya': None}
        simpul3['berikutnya'] = simpul4
        
        # Menampilkan nilai-nilai
        print("Nilai pertama:", self.kepala['nilai'])
        print("Nilai kedua:", simpul2['nilai'])
        print("Nilai ketiga:", simpul3['nilai'])
        print("Nilai keempat:", simpul4['nilai'])


# Membuat objek LinkedList
daftar = LinkedList(10, 20, 30, 40)
