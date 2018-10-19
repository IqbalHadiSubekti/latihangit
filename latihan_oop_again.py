class TugasKuliah():
    def __init__(self,tugas,nilai):
        self.nama_tugas = tugas
        self.nilai = nilai
    
class Mahasiswa():
    def __init__(self,nim,nama,jenis_kelamin):
        self.nim = nim
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.dataTugas = list()

    def addTugas(self,tugas):
        self.dataTugas.append(tugas)
    
    def printTugas(self):
        for t in self.dataTugas:
            print("Tugas %s nilai %s" % (t.nama_tugas, t.nilai))
            
    def nilaiRataRata(self):
        total = 0
        for t in self.dataTugas:
            total += t.nilai
        return total/len(self.dataTugas)
        
class Dosen():
    def __init__(self,nik,dosen):
        self.nik = nik
        self.dosen = dosen
        self.mahasiswaList = list()
        
    def addMahasiswa(self,m):
        self.mahasiswaList.append(m)
        
    def mahasiswaLakiLaki(self):
        result = list()
        for m in self.mahasiswaList:
            if m.jenis_kelamin == 'L':
                result.append(m)
        return result
    
    def nilaiRataRataSeluruhMahasiswa(self):
        total = 0
        n = 0
        for m in self.mahasiswaList:
            for t in m.dataTugas:
                total += t.nilai;
                n += 1
        return total/n
		
class Ujian():
	def __init__(self,uts,uas):
		self.uts = uts
		self.uas = uas
		
nama = str(input("Masukkan nama : "))
nim = str(input("Masukkan NIM : "))
uts = int(input("Masukkan nilai UTS : "))
uas = int(input("Masukkan nilai UAS : "))
tugas = int(input("Masukkan nilai Tugas : "))

Uts = uts*30/100;
Uas = uas*30/100;
Tugas = tugas*40/100;
nilai_akhir = Uts+Uas+Tugas;

print ("\nnama : %s"%nama)
print("nim : %s"%nim)
print("nilai uts : %i"%uts)
print("nilai uas : %i"%uas)
print("nilai tugas : %d"%tugas)
print("nilai akhir : ",float(nilai_akhir))

if 86<nilai_akhir<100:
	print("\nnilai huruf : A")
elif 71<nilai_akhir<85:
	print("\nnilaihuruf : B")
elif 51<nilai_akhir<70:
	print("\nnilai huruf : C")
elif 31<nilai_akhir<50:
	print("\nnilai huruf : D")
elif nilai_akhir < 30:
	print("\nnilai huruf : E")
	








