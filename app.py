import csv
import os

csv_filename = 'C:\Python\CRUD-INVENTORY-CSV-PYTHON\Data\Barang2.csv'
import time

# clearscreen ubntuk membersihkan layar dengan key cls = clearscreen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# Menampilkan menu program
def show_menu():
    clear_screen()
#   Baris kode untuk jumlah total data
    Barang = []
    with open('C:\Python\CRUD-INVENTORY-CSV-PYTHON\Data\Barang2.csv', mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file,delimiter = ",")
        for row in csv_reader:
            Barang.append(row)
    row_count = sum(1 for row in Barang)
    # print(Barang)
    print("=== APLIKASI Inventory TOKO SEDERHANA === \n")
    print("============ Menu =============")
    print("===============================")
    print("* INFO Total Barang : ",row_count)  
    print("[1] Lihat Daftar Barang")
    print("[2] Tambah Barang")
    print("[3] Edit Barang")
    print("[4] Hapus Barang")
    print("[5] Cari Barang")
    print("[6] Mengolah data csv dengan pandas")
    print("[0] Exit \n")
    print("===============================")
    selected_menu = input("Pilih menu> ")
    
    # Percabangan untuk menentukan pilihan menu
    if(selected_menu == "1"):
        show_barang()
    elif(selected_menu == "2"):
        tambah_barang()
    elif(selected_menu == "3"):
        edit_barang()
    elif(selected_menu == "4"):
        delete_barang()
    elif(selected_menu == "5"):
        search_barang()
    elif(selected_menu == "6"):
        pandas_import()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

# fungsi kembali ke menu isinya memanggil fungsi show menu
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


#  fungsi tambah barang 
def tambah_barang():
    clear_screen()
    with open(csv_filename, mode='a',newline='') as csv_file:
        fieldnames = ['kode', 'NAMA', 'harga','QTY', 'JumlahPesanan','HargaTotal']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("===============================")
        print("======== Tambah Barang ========")
        print("===============================\n")
        
        kode = input("kode: ")
        nama = input("Nama Barang: ")
        harga = float(input("Harga Barang: "))
        QTY = int(input("Jumlah Barang: "))
        JumlahPesanan = int(input("Jumlah Pesanan: "))
        HargaTotal = JumlahPesanan*harga
        print("===============================")
        print("Harga yang dibayar",HargaTotal)
        print("===============================")
        writer.writerow({'kode': kode, 'NAMA': nama, 'harga': harga, 'QTY': QTY, 'JumlahPesanan': JumlahPesanan, 'HargaTotal' : HargaTotal })    
    
    back_to_menu()

    # fungsi menampilkan barang 
    # hargaTotal = JumlahPesanan*harga
def show_barang():
        clear_screen()
        Barang = []
    # buka file CSV dengan mode R / Baca
        with open(csv_filename, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                Barang.append(row)

        row_count = sum(1 for row in Barang)

        print("-" * 80)
        print("\t\tDaftar Stok Barang Toko")
        print("-" * 80)

        print("kode \t NAMA \t\t harga \t\t QTY \t\t JumlahPesanan \t\t HargaTotal")
        print("-" * 80)
        
        # Looping untuk mengeluarkan datanyna
        for data in Barang:
            print(f"{data['Kode']} \t {data['NAMA']} \t Rp.{data['HARGA']} \t {data['QTY']} \t\t\t{data['JumlahPesanan']} \t\t{data['HargaTotal']}|")
        print("-" * 80)
        print("Total Data: ",row_count)
        print("-" * 80)
        
        back_to_menu()


def search_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    kode = input("Cari berdasrakan kode> ")

    data_found = []

    # mencari Barang
    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            data_found = Barang[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"NAMA: {data_found['NAMA']}")
        print(f"HARGA: Rp.{data_found['HARGA']}")
        print(f"QTY :{data_found['QTY']}")
        print(f"JumlahPesanan : {data_found['JumlahPesanan']}")
        print(f"Harga yang dibayar : Rp.{data_found['HargaTotal']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()
    


def edit_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r",newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)
    row_count = sum(1 for row in Barang)

    print("-" * 80)
    print("\t\tDaftar Stok Barang Toko")
    print("-" * 80)

    print("kode \t NAMA \t\t Harga \t\t QTY \t\t JumlahPesanan \t\t HargaTotal")
    print("-" * 80)

    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \tRp.{data['HARGA']} \t{data['QTY']} \t\t\t{data['JumlahPesanan']}\t\t\t{data['HargaTotal']}")

    print("-" * 80)
    print("Total Data :",row_count)
    print("-" * 80)
    kode = input("Pilih Kode Barang : ")
    nama = input("nama baru: ")
    harga = float(input("harga baru: "))
    QTY = input("JUMLAH baru: ")
    JumlahPesanan = int(input("Jumlah Pesanan: "))
    HargaTotal = JumlahPesanan*harga


    # mencari Barang dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            Barang[indeks]['NAMA'] = nama
            Barang[indeks]['HARGA'] = harga
            Barang[indeks]['QTY'] = QTY
            Barang[indeks]['JumlahPesanan'] = JumlahPesanan
            Barang[indeks]['HargaTotal'] = HargaTotal
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'HARGA','QTY','JumlahPesanan', 'HargaTotal']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA'], 'QTY': new_data['QTY'], 'JumlahPesanan': new_data['JumlahPesanan'], 'HargaTotal': new_data['HargaTotal']}) 

    back_to_menu()



def delete_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("kode \t NAMA \t\t harga \t QTY \t JumlahPesanan \t HargaTotal")
    print("-" * 80)

    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \t {data['HARGA']} \t {data['QTY']} \t {data['JumlahPesanan']} \t {data['HargaTotal']}")

    print("-----------------------")
    kode = input("Hapus Barang dengan KODE : ")

    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            Barang.remove(Barang[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'HARGA', 'QTY','JumlahPesanan', 'HargaTotal']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA'], 'QTY': new_data['QTY'], 'JumlahPesanan': new_data['JumlahPesanan'], 'HargaTotal': new_data['HargaTotal'] }) 

    print("Data sudah terhapus")
    back_to_menu()

def pandas_import() :
    import pandas as pd
    df = pd.read_csv('C:\Python\CRUD-INVENTORY-CSV-PYTHON\Data\Barang2.csv')
    print("data all")
    print(df)

    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()



# def editdata():
#     import os
#     os.system("CLS")
#     print("\t\t\t\tSILAHKAN EDIT DATA SESUAI KEINGINAN ANDA\n")
#     ml = input("Masukkan Nama Alat Musik Yang ingin Anda Ganti :")
#     ab = input("Nama Musik Pengiring Baru :")
#     bb = input("Cara memainkannya :")
#     f = open("Data/Musikpengiring.txt")
#     isi = f.readlines()
#     mb = 0
#     for x in isi:
#         ax = x.split(",")
#     if ax[0] == ml:
#         ax[0] = ab
#         ax[1] = bb+"\n"
#         ag = ",".join(ax)
#         isi[mb] = ag
#         mb +=1
#         f.close()
#         f = open("data/Musikpengiring.txt", "w")
#         isi = f.writelines(isi)
#         print("tekan enter untuk melanjutkan")
#         12
#         f.close()
#         input()
        # # daftar
        # daftar()