class kalkulator:
    def tambah(self, a, b=0, c=0,):
        return a + b + c
    
k = kalkulator()
print(k.tambah(5))
print(k.tambah(5, 10))
print(k.tambah(5, 10, 15))