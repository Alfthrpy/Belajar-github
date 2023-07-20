print("ini adalah fitur beta yang mungkin akan di tambahkan ke program utama")

print("cek karakter dalam kata yang diinput user")

str = input("Masukan kata")
word = input("Masukan huruf yang ingin di cek")

if word in str:
  print(f"{word} ada di kata yang diinputkan")
else:
  print(f"{word} tidak ditemukan")

print("program menambahkan angka dengan fungsi")
def sum(a,b):
  return a+b

a1 = input(int("angka 1:"))
a2 = input(int("angka 2:"))

print(f"hasil jumlah : {sum(a1,a2}")

print("program menampilkan input user")
str = input("masukan input:")
print(str)
