class PekerjaanRumah:
    def kerjakan(self):
        return "Mengurus pekerjaan rumah."

class Vicko(PekerjaanRumah):
    def kerjakan(self):
        return "Vicko menyapu lantai."

class Cantika(PekerjaanRumah):
    def kerjakan(self):
        return "Cantika mencuci piring dan memasak."

class Rafca(PekerjaanRumah):
    def kerjakan(self):
        return "Rafca menyiram tanaman."

def distribusi_tugas(pekerja):
    print(pekerja.kerjakan())

pekerja_rumah = [Vicko(), Cantika(), Rafca()]

for p in pekerja_rumah:
    distribusi_tugas(p)