print("ini adalah fitur beta yang mungkin akan di tambahkan ke program utama")

print("cek karakter dalam kata yang diinput user")

str = input("Masukan kata")
word = input("Masukan huruf yang ingin di cek")

if word in str:
  print(f"{word} ada di kata yang diinputkan")
else:
  print(f"{word} tidak ditemukan")
