#Program Penentuan Kategori Umur
umur=float(input("Masukkan Umur: "))
if (umur >=0 and umur <=5):
    print ("Kategori Balita")
elif (umur >5 and umur <= 11):
    print ("Kategori Anak anak")
elif (umur >11 and umur <=25):
    print ("Kategori Remaja")
elif (umur >25 and umur <=45):
    print ("Kategori Dewasa")
elif (umur >45 and umur <=65):
    print ("Kategori Lansia")
elif (umur >65 and umur <= 120):
    print ("Kategori Manula")
else :
    print ("Data tidak valid")