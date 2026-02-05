class Hewan:
    def suara (self):
        pass

class ayam (Hewan):
    def suara (self):
        return "aaaaaaaaaaaaaaaaaaaaaaaaaaa!"
    
class ayam2 (Hewan):
    def suara (self):
        return "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!" 

def cetak_suara (objek_hewan):
    print(f"Suara hewan: {objek_hewan.suara()}")
jenis = input("Masukkan jenis hewan (ayam/ayam2): ").lower()
if jenis == "ayam":
    hewan = ayam()
    cetak_suara (hewan)
elif jenis == "ayam2":
    hewan = ayam2()
    cetak_suara (hewan)
else:
    print("Hewan tidak dikenal")