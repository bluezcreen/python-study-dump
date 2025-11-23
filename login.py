#bikin akun

print("Buat akun")

namabenar = input("Masukkan namamu")
passbenar = input("Masukkan passwordmu")

input("Akun berhasil dibuat. Klik tombol manapun untuk melanjutkan login")

#login ke akun

print("Login")
nama = input("Masukkan nama penggunamu")
passw = input("Masukkan passwordmu")

if nama == namabenar and  passw == passbenar:
	print("Selamat datang", namabenar)
else:
	print("Nama atau password salah")