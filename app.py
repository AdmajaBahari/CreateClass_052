#menghitung luas persegi panjang
class persegiPanjang :

    def __init__(self, p, l):
        self.p = p
        self.l = l
    
    def luasPersegiPanjang(self) :
        return self.p * self.l
    
    def kelilingPersegiPanjang(self) :
        return 2 * (self.p + self.l)
    
    def __str__(self) :
        return f"Persegi panjang dibuat dengan panjang {self.p} dan lebar {self.l}"
    
try :
    panjang = int(input("Isikan Panjang : "))
    lebar = int(input("Isikan Lebar : "))

    pp = persegiPanjang(panjang, lebar)
        
    luas = pp.luasPersegiPanjang()
    print(f"Luas Persegi Panjang : {luas}")

    keliling = pp.kelilingPersegiPanjang()
    print(f"Keliling Persegi Panjang : {keliling}")

except ValueError :
    print(" Inputan harus berupa angka saja!")
    exit()

finally :
    print("\tProgram selesai.\n\tTerima Kasih telah mengunakan program ini.")