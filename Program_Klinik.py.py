class Klinik:
    def __init__(core):
        # Database admin
        core.admin_data = {"admin": "admin123"}
        # Database pasien
        core.pasien_data = {} 
        # Menyimpan status login
        core.admin = False 
        # Menyimpan username pengguna yang sedang login
        core.user = None 

    def admin_login(core):
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")

        if username in core.admin_data and core.admin_data[username] == password:
            print("========= Login admin berhasil =========\n")
            core.admin = True
            core.user = username
        else:
            print("========== Login admin gagal ==========\n")
    
    def pendaftaran(core):
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = ["Kode", "Nama Dokter", "Spesialis", "Jadwal Praktek"]
        table.add_row([1, "dr. Yanti E.A. Gultom, Sp. P", "Spesialis Paru", "Senin-Jum'at (17.00-Selesai)"])
        table.add_row([2, "dr. Resliany, Sp. P D", "Spesialis Penyakit Dalam", "Senin-Jum'at (19.00-Selesai)"])
        table.add_row([3, "dr. A. Wisnu Wardhana, Sp. A", "Spesialis Anak", "Senin-Jum'at (19.30-Selesai)"])
        table.add_row([4, "dr. Selvianti, Sp. THT-KL", "Spesialis THT", "Sen, Sel, Kam, Jum (18.30-Selesai)"])
        print(table)
        nama = input("Masukkan nama pasien: ")
        alamat = input("Masukkan alamat pasien: ")
        nomor_hp = input("Masukkan nomor HP pasien: ")
        spesialis = input("Masukkan dokter spesialis: ")

        core.pasien_data[nama] = {
            "Alamat": alamat,
            "Nomor HP": nomor_hp,
            "Spesialis": spesialis,
        }
        print(f"========= Pendaftaran pasien {nama} berhasil =========\n")

    def admin_edit(core):
        nama = input("Masukkan nama pasien yang ingin diedit: ")
        if nama in core.pasien_data:
            alamat = input("Masukkan alamat baru: ")
            nomor_hp = input("Masukkan nomor HP baru: ")
            spesialis = input("Masukkan dokter spesialis (kosongkan jika tidak ingin mengubah): ")

            core.pasien_data[nama]["Alamat"] = alamat
            core.pasien_data[nama]["Nomor HP"] = nomor_hp
            if spesialis:
                core.pasien_data[nama]["Spesialis"] = spesialis
            print(f"========= Data pasien {nama} telah diperbarui =========\n")
        else:
            print(f"========= Data pasien {nama} tidak ditemukan =========\n")

    def admin_hapus(core):
        nama = input("Masukkan nama pasien yang ingin dihapus: ")
        if nama in core.pasien_data:
            del core.pasien_data[nama]
            print(f"========= Data pasien {nama} telah dihapus =========\n")
        else:
            print(f"======== Data pasien {nama} tidak ditemukan ========\n")

    def tampil_tabel_pasien(core):
        print("\nTabel Data Pasien:")
        print("{}\t\t\t|{}\t\t\t\t\t|{}\t\t\t\t\t|{}".format("Nama", "Alamat", "Nomor HP", "Spesialis"))
        for nama, data in core.pasien_data.items():
            alamat = data["Alamat"]
            nomor_hp = data["Nomor HP"]
            spesialis = data["Spesialis"]
            print("{}\t\t\t|{}\t\t\t\t|{}\t\t\t\t\t|{}".format(nama, alamat, nomor_hp, spesialis))

    def run(core):
        while True:
            print("=====================================================================================================")
            print("\t\t\t\tSELAMAT DATANG DI KLINIK ANTASARI")
            print("\t\t\t\tJl. P. Antasari No. 29 Samarinda")
            print("=====================================================================================================")
            if not core.admin:
                print("\nMenu Utama:")
                print("1. Log in sebagai Admin")
                print("2. Pendaftaran Pasien (Umum)")
                print("3. Keluar")
            else:
                print("\nMenu Admin:")
                print("1. Edit Data Pasien")
                print("2. Hapus Data Pasien")
                print("3. Tampil Tabel Pasien")

            pilih = input("Pilih tindakan : ")
            
            if not core.admin:
                if pilih == "1":
                    core.admin_login()
                elif pilih == "2":
                    core.pendaftaran()
                elif pilih == "3":
                    break
                else:
                    print("======= Pilihan tidak valid =======\n")
                    break
            else:
                if pilih == "1":
                    core.admin_edit()
                elif pilih == "2":
                    core.admin_hapus()
                elif pilih == "3":
                    core.tampil_tabel_pasien()
                else:
                    print("======= Pilihan tidak valid =======\n")
                    break

# Untuk menampilkan seluruh program di atas
if __name__ == "__main__":
    klinik = Klinik()
    klinik.run()