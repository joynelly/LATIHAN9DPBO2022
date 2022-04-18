from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, luas):
        super().__init__("Indekos", luas)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni

    def get_dokumen(self):
        return "\nDokumen\n" + "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_luas(self):
        return self.luas

    def get_summary(self):
        return super().get_summary()

    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nPenghuni : " + self.nama_penghuni + "\nLuas Kamar : " + str(self.luas) + " m2\n"