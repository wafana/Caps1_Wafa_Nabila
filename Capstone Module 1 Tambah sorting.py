from tabulate import tabulate
from colorama import init, Fore

header_stock = ['Kode', 'Nama Item', 'Stok Awal', 'Stok Masuk', 'Stok Keluar', 'Total Stok']
list_stock = [
    ['LET001', 'Lettuce', 23, 0, 0, 23], 
    ['TOM001', 'Tomato', 45, 0, 0, 45], 
    ['CAR001','Carrot', 50, 0, 0, 50],
    ['POT001', 'Potato', 30, 0, 0, 30],
    ['ONI001', 'Onion', 40, 0, 0, 40],
    ['GAR001', 'Garlic', 20, 0, 0, 20],
    ['CUC001', 'Cucumber', 35, 0, 0, 35],
    ['CAB001', 'Cabbage', 25, 0, 0, 25]
    ]

def display_list():
    print('\n' + 'Stock List:')
    print(tabulate(list_stock, headers = header_stock, tablefmt = "fancy_grid")) # Mengaplikasikan fungsi Tabulate terhadap List

def empty_stock(): # Regular function yang berfungsi untuk cek apakah list kosong
    if len(list_stock) == 0: 
        print('\n' + Fore.RED + '\t' + '      Data tidak ada' + Fore.RESET)
        return True # Kalau list kosong fungsi akan return True
    return False # Kalau list tidak kosong fungsi akan return False

def sub_menu_1():
    while True: # While loop submenu 1
        print('\n' + '\t' + '   Menu Menampilkan Data')
        print('\t' + '  ' + 23*'~')
        print('1. Tampilkan tabel seluruh data\n2. Tampilkan data berdasarkan kode item\n3. Tampilkan data berdasarkan nama item\n4. Tampilkan data berdasarkan urutan alfabet\n5. Tampilkan data berdasarkan total stok\n6. Kembali ke Main Menu')
        try: # Coba untuk input data sebagai integer
            no_submenu_1 = int(input('Masukkan angka sub-menu yang ingin dijalankan (1-6): ')) # User input opsi submenu
            if no_submenu_1 == 1: 
                if empty_stock():
                    continue # Lanjutkan fungsi submenu (ulang while loop submenu 1)
                else:
                    display_list()

            elif no_submenu_1 == 2:
                if empty_stock():
                    continue # Lanjutkan fungsi submenu (ulang while loop submenu 1)
                else:
                    item_code = input('Masukkan kode item yang ingin ditampilkan: ').strip().upper() # Input primary key item

                    found_item = None # Mencari item dari primary key yang diinput
                    for i in list_stock:
                        if i[0] == item_code:
                            found_item = i # Kalau ditemukan data akan masuk ke variabel found_item
                            break # Keluar dari for loop

                    if found_item: # Kondisi kalau item ditemukan
                        print(tabulate([found_item], headers=header_stock, tablefmt="fancy_grid"))
                    else: # Kondisi kalau item tidak ditemukan
                        print('\n' + Fore.RED + f'    Item dengan kode {item_code} tidak ditemukan' + Fore.RESET)
            elif no_submenu_1 == 3:
                if empty_stock(): # Kalau stok kosong
                    continue # Lanjutkan kembali ke while loop submenu 1
                else:
                    nama_item = input('Masukkan nama item yang ingin ditampilkan: ').strip().title() # Input nama item yang ingin di-display

                    found_item_name = None # Mencari item dari nama yang diinput
                    for i in list_stock:
                        if i[1] == nama_item:
                            found_item_name = i
                            break # Keluar dari for loop

                    if found_item_name: # Kalau item ditemukan eksekusi argumen di bawah
                        print(tabulate([found_item_name], headers=header_stock, tablefmt="fancy_grid"))
                    else: # Kalau item tidak ditemukan, eksekusi atgumen di bawah
                        print('\n' + Fore.RED + f'    Item dengan nama {nama_item} tidak ditemukan  ' +  Fore.RESET)
            elif no_submenu_1 == 4:
                    if empty_stock():
                        continue # Lanjutkan fungsi submenu (ulang while loop submenu 1)
                    else:
                        list_stock_by_name = list_stock.copy()
                        list_stock_by_name.sort(key=lambda x: x[1])
                        print(tabulate(list_stock_by_name, headers=header_stock, tablefmt='fancy_grid'))
            elif no_submenu_1 == 5:
                    if empty_stock():
                        continue # Lanjutkan fungsi submenu (ulang while loop submenu 1)
                    else:
                        list_stock_by_stock = list_stock.copy()
                        list_stock_by_stock.sort(key=lambda x:x[5], reverse=True)
                        print(tabulate(list_stock_by_stock, headers=header_stock, tablefmt='fancy_grid'))
            elif no_submenu_1 == 6:
                print('\n' + Fore.BLUE + '           Kembali ke Main Menu' + Fore.RESET + '\n')
                break # Keluar dari while loop submenu 1 kembali ke Main Menu

            else:
                print('\n' + Fore.RED + '     Nomor yang Anda input tidak valid' + Fore.RESET)
        except ValueError:  # Jika terjadi ValueError syntax di bawah akan dieksekusi
            print('\n' + Fore.RED + '         Input harus berupa angka' + Fore.RESET)

def sub_menu_2():
    while True: # While loop submenu 2
        print('\n\t'+'   '+'Menu Menambahkan Data')
        print('\t'+ '  '+ 23*'~')
        print('1. Menambah data\n2. Kembali ke Main Menu')
        try:
            no_submenu_2 = int(input('Masukkan angka sub-menu yang ingin dijalankan (1-2): ')) # Input submenu 2
            
            if no_submenu_2 == 1:
                back_to_submenu = False # Flag untuk kontrol kembali ke submenu
                
                while True: # While loop untuk input kode
                    new_code = input('Masukkan kode item baru (format: 3 huruf diikuti 3 angka): ').strip().upper()
                   
                    if len(new_code) != 6 or not new_code[:3].isalpha() or not new_code[3:].isdigit():  # Cek format kode user input
                        print(Fore.RED + 'Format yang Anda masukkan salah, silakan coba lagi' + Fore.RESET)
                        continue # Melanjutkan eksekusi ke awal while loop untuk input kode
                    
                    code_exists = False # Cek apakah kode yang user input sudah ada
                    for i in list_stock:
                        if i[0] == new_code:
                            code_exists = True
                            break
                    if code_exists: # Kalau kode yang sama ditemukan
                        print('\n' + Fore.RED + '\t' + '       Data sudah ada' + Fore.RESET)
                        back_to_submenu = True # Flag untuk kembali ke submenu 2
                        break # Keluar dari while loop input kode dan mengeksekusi syntax selanjutnya
                    else:
                        break # Data baru terverifikasi dan keluar dari while loop input kode untuk mengeksekusi syntax selanjutnya 

                if back_to_submenu:
                    continue # Keluar dari while loop untuk input kode dan kembali ke while loop submenu 2
                    
                while True: # While loop input nama
                    new_name = input('Masukkan nama item baru: ').strip().title() # Input nama baru
                    
                    name_exists = False # Cek apakah nama yang user input sudah ada
                    for i in list_stock:
                        if i[1] == new_name:
                            name_exists = True
                            break 
                    if name_exists: # Kondisi kalau nama telah ada
                        print('\n' + Fore.RED + f'     Data dengan nama {new_name} sudah ada' + Fore.RESET)
                        back_to_submenu = True # Flag untuk kembali ke submenu, dibutuhkan karena syntac berada di loop di dalam loop
                        break # Keluar while loop input nama untuk eksekusi syntax selanjutnya
                    else:
                        break # Nama benar eksekusi syntax selanjutnya

                if back_to_submenu: # Kalau statement Flag terpenuhi
                    continue # Keluar dari while loop untuk input kode dan kembali ke while loop submenu 2

                while True: # While loop konfirmasi
                    new_value = [new_code, new_name, 0, 0, 0, 0] # Variable data baru berisi list dari kode baru dan nama baru
                    print(tabulate([new_value], headers=header_stock, tablefmt='fancy_grid')) # Print tabel berisi value baru
                    conf_new_value = input(Fore.YELLOW + 'Apakah Anda yakin ingin menyimpan item di atas (y/n)? '+ Fore.RESET).strip().lower() # Konfirmasi menyimpan data
                    if conf_new_value == 'y': # Kalau user setuju menyimpan item
                        list_stock.append([new_code, new_name, 0, 0, 0, 0]) # Value baru akan ditambahkan ke list yang sudah ada
                        display_list() # Display list yang telah diubah
                        print('\n' + Fore.GREEN + f'      Item {new_name} berhasil ditambahkan' + Fore.RESET) # Notifikasi item baru telah ditambahkan
                        break # Keluar dari while loop konfirmasi kembali ke submenu 2
                    elif conf_new_value == 'n': # Kalau user tidak setuju menyimpan item
                        print('\n' + Fore.RED + '             Proses dibatalkan' + Fore.RESET) # Notifikasi item baru batal disimpan
                        break # Keluar dari while loop konfirmasi kembali ke submenu 2
                    else: # Kalau user menginput selain y dan n
                        print('\n' + Fore.RED + 'Input yang Anda masukkan salah' + Fore.RESET + '\n') #Notifikasi bahwa input salah
                        continue # Melanjutkan proses dan kembali ke while loop konfirmasi
                continue # Melanjutkan proses dan kembali ke submenu 2

            elif no_submenu_2 == 2: 
                print('\n' + Fore.BLUE + '           Kembali ke Main Menu' + Fore.RESET + '\n') 
                break # Keluar dari while loop submenu 2 dan kembali ke Main Menu
            else:
                print('\n' + Fore.RED + '     Nomor yang Anda input tidak valid' + Fore.RESET)

        except ValueError: # Kalau ValueError, syntax di bawah akan dieksekusi
            print('\n' + Fore.RED + '         Input harus berupa angka' + Fore.RESET)

def sub_menu_3():
    while True:
        print('\n' + '\t'+'  '+'Menu Memperbarui Data')
        print('\t'+ ' '+ 23*'~')
        print('1. Update item\n2. Kembali ke Main Menu')

        try:
            no_submenu_3 = int(input('Masukkan angka sub-menu yang ingin dijalankan (1-2): '))

            if no_submenu_3 == 1:
                    display_list()
                    code_updated = input('Masukkan kode dari item yang ingin Anda ubah: ').strip().upper() # User input kode dari item yang ingin diupdate
                    if empty_stock():
                        continue # Lanjutkan proses dan kembali ke while loop submenu 3
                    else:
                        data_changed = None # Find the data based on code updated
                        for i in list_stock:
                            if i[0] == code_updated:
                                data_changed = i
                                break # Break dari for loop

                        if data_changed: # Kondisi kalau data yang ingin diubah ditemukan
                            print(tabulate([data_changed], headers=header_stock, tablefmt='fancy_grid'))
                            
                            while True: # While loop konfirmasi
                                conf_data_change = input(Fore.YELLOW + 'Apakah Anda yakin ingin mengubah data di atas ini (y/n)? ' + Fore.RESET).strip().lower() # User input konfirmasi mengupdate data
                                if conf_data_change == 'y': # Kalau user setuju untuk mengubah data tersebut syntax di bawah akan dieksekusi
                                    print('1. Ubah nama\n2. Tambahkan stok masuk\n3. Tambahkan stok keluar\n4. Kembali ke Menu Update')
                                    
                                    while True: # While loop input kolom
                                        try:
                                            input_column = int(input('Silakan pilih kolom yang ingin Anda ubah (1-3): ')) # User input menu yang ingin dijalankan
                                            
                                            if input_column == 1: # Ubah nama
                                                while True: # While loop input nama baru
                                                    changed_name = input(f'Masukkan nama baru: ').strip().title()
                                                    changed_name_exists = False # Variable apakah untuk test nama yang baru sudah ada

                                                    for i in list_stock: # For loop untuk mencari apakah nama baru sudah ada
                                                        if i[1] == changed_name.strip().title():
                                                            changed_name_exists = True # Flag kalau nama baru sudah ada di list
                                                            break # Keluar dari for loop mencari nama baru
                                                    if changed_name_exists: # Kalau nama baru sudah ada, syntax di bawah akan dieksekusi
                                                        print(Fore.RED + f'Data dengan nama {changed_name} sudah ada. Silakan masukkan nama lain.' + Fore.RESET)
                                                        continue # Lanjut ke while loop input nama baru
                                                    else:
                                                        while True: # While loop konfirmasi 
                                                            conf_name_change = input(Fore.YELLOW + 'Apakah Anda yakin ingin mengubah data (y/n)? ' + Fore.RESET).strip().lower() # User input konfirmasi
                                                            if conf_name_change == 'y': # Kalau user setuju untuk mengubah nama
                                                                data_changed[1] = changed_name # Indeks ke-1 dari data yang diubah akan diubah dengan data baru berdasarkan input
                                                                display_list() 
                                                                print('\n' + Fore.GREEN + f'      Nama item {code_updated} berhasil diubah' + Fore.RESET)
                                                                break # Keluar dari while loop konfirmasi 
                                                            elif conf_name_change == 'n': # Kalau user tidak setuju mengubah data
                                                                print('\n' + Fore.RED + '             Proses dibatalkan' + Fore.RESET)
                                                                break # Keluar dari while loop konfirmasi
                                                            else:
                                                                print(Fore.RED + 'Input yang Anda masukkan salah' + Fore.RESET)
                                                        break # Keluar dari while loop input nama baru

                                            elif input_column == 2:
                                                while True: # While loop input stok masuk 
                                                    try:
                                                        stockin = int(input('Masukkan jumlah stok masuk: '))

                                                        while True: # While loop konfirmasi
                                                            conf_stockin_change = input(Fore.YELLOW + 'Apakah Anda yakin ingin mengubah data (y/n)? ' + Fore.RESET).strip().lower() # Konfirmasi data yang ingin diubah
                                                            if conf_stockin_change == 'y': # Kalau user setuju
                                                                data_changed[3] = stockin # indeks ke-3 dari data yang diubah berubah jadi stockin
                                                                data_changed[5] += data_changed[3] # indeks ke-5 dari data yang diubah ditambahkan dengan stockin
                                                                print(tabulate([data_changed], headers=header_stock,tablefmt='fancy_grid')) # Tampilkan data yang telah diubah
                                                                print('\n' + Fore.GREEN + f'Stok masuk item {code_updated} berhasil ditambahkan' + Fore.RESET) # Notifikasi
                                                                break # Keluar dari while loop konfirmasi
                                                            elif conf_stockin_change == 'n':
                                                                print('\n' + Fore.RED + '             Proses dibatalkan' + Fore.RESET)
                                                                break
                                                            else:
                                                                print(Fore.RED + 'Input yang Anda masukkan salah' + Fore.RESET)
                                                        break # Keluar dari while loop input stok

                                                    except ValueError: # Kalau ValueError, eksekusi syntax di bawah
                                                        print('\n' + Fore.RED + '         Input harus berupa angka' + Fore.RESET)
                                            
                                            elif input_column == 3:
                                                while True: # While loop input stok keluar
                                                    try:
                                                        stockout = int(input('Masukkan jumlah stok keluar: ')) # Input stok keluar 
                                                        if stockout > data_changed[5]: # Kondisi kalau stok keluar yang diinput lebih besar dari total stok
                                                            print('\n' + Fore.RED + '             Stok tidak cukup' + Fore.RESET)
                                                        else: # Kondisi kalau stok keluar tidak lebih besar dari total stok
                                                            while True: # While loop input konfirmasi
                                                                conf_stockout_change = input(Fore.YELLOW + 'Apakah Anda yakin ingin mengubah data (y/n)? '+ Fore.RESET) # Input konfirmasi
                                                                if conf_stockout_change == 'y': # Kalau user setuju 
                                                                    data_changed[4] = stockout # indeks ke-4 dari data yang diubah akan diganti jadi input stockout
                                                                    data_changed[5] -= data_changed[4] # indeks ke-5 dari data yang diubah akan dikurangi stok keluar yang baru
                                                                    print(tabulate([data_changed], headers=header_stock,tablefmt='fancy_grid')) # tabel akan diprint
                                                                    print('\n' + Fore.GREEN + f'Stok keluar item {code_updated} berhasil ditambahkan' + Fore.RESET) # Notifikasi
                                                                    break # Keluar dari while loop input konfirmasi
                                                                elif conf_stockout_change == 'n': # Kalau user tidak setuju
                                                                    print('\n' + Fore.RED + '             Proses dibatalkan' + Fore.RESET)
                                                                    break # Keluar dari while loop input konfirmasi
                                                                else: # Kalau input selain y dan n
                                                                    print(Fore.RED + 'Input yang Anda masukkan salah' + Fore.RESET)
                                                        break # Keluar dari while loop input stok keluar
                                                    except ValueError: # Kalau ValueError
                                                        print('\n' + Fore.RED + '         Input harus berupa angka' + Fore.RESET) 
                                            elif input_column == 4:
                                                print('\n' + Fore.BLUE + '    Kembali ke Menu Mengupdate Data' + Fore.RESET)
                                                break # Keluar dari while loop input kolom
                                            else:
                                                print('\n' + Fore.RED + '     Nomor yang Anda input tidak valid' + Fore.RESET)
                                        except ValueError: # Kalau input kolom ValueError
                                            print('\n' + Fore.RED + '     Nomor yang Anda input tidak valid' + Fore.RESET)
                                        break # Keluar dari while loop input kolom
                                elif conf_data_change == 'n':# Kalau user tidak setuju dengan item yang ingin diubah, syntax di bawah akan dieksekusi
                                    print('\n' + Fore.RED + '             Proses dibatalkan' + Fore.RESET)
                                    break # Keluar dari while loop konfirmasi
                                else: # Kalau input selain y dan n
                                    print(Fore.RED + 'Input yang Anda masukkan salah' + Fore.RESET)
                                    continue # Lanjut dan kembali ke while loop konfirmasi
                                break # Keluar dari while loop konfirmasi
                        else: # Kondisi kalau kode yang ingin diubah tidaj ditemukan
                            print('\n' + Fore.RED + f'    Item dengan kode {code_updated} tidak ditemukan' + Fore.RESET)
                            continue # Lanjutkan proses kembali ke while loop submenu 3
            elif no_submenu_3 == 2: 
                print('\n' + Fore.BLUE + '           Kembali ke Main Menu' + Fore.RESET + '\n')
                break # Keluar dari while loop submenu 3
            else: # Kalau nomor yang diinput tidak sesuai dengan menu
                print('\n' + Fore.RED + '     Nomor yang Anda input tidak valid' + Fore.RESET) 
        except ValueError: # Kalau input ValueError
            print('\n' + Fore.RED + '         Input harus berupa angka' + Fore.RESET)

def sub_menu_4():
    while True: # While loop submenu 4
        print('\n\t'+'   '+'Menu Menghapus Data')
        print('\t'+ ' '+ 23*'~')
        print('1. Hapus data berdasarkan kode item\n2. Hapus semua data\n3. Kembali ke Main Menu')
        try:
            no_submenu_4 = int(input('Masukkan angka sub-menu yang ingin dijalankan (1-3): '))
            if no_submenu_4 == 1:
                    display_list()
                    code_deleted = input('Masukkan kode barang yang ingin Anda hapus: ').strip().upper()
                    if empty_stock(): # Cek kalau stok kosong
                        continue # Lanjut dan kembali ke while loop submenu
                    item_deleted = None # Set kondisi
                    for i in list_stock: # For loop untuk menemukan kode item yang ingin dihapus
                        if i[0] == code_deleted.strip().upper():
                            item_deleted = i # Kondisi kalau data ditemukan
                            break # Keluar dari for loop
                    if item_deleted: # Kalau item ditemukan
                        print(tabulate([item_deleted], headers=header_stock, tablefmt="fancy_grid"))
                        while True: # While loop konfirmasi
                            conf_delete = input(Fore.YELLOW + 'Apakah Anda yakin ingin menghapus barang di atas (y/n): ' + Fore.RESET).strip().lower()
                            if conf_delete == 'y':
                                list_stock.remove(item_deleted) # Values di-remove dari list
                                display_list() # Display list yang sudah diubah
                                print('\n' + Fore.GREEN + f'Item dengan kode {code_deleted} telah dihapus' + Fore.RESET)
                                break # Keluar dari while loop konfirmasi
                            elif conf_delete == 'n':
                                print('\n' + Fore.RED + '             Proses dibatalkan' + Fore.RESET)
                                break # Keluar dari while loop konfirmasi
                            else:
                                print(Fore.RED + 'Input yang Anda masukkan salah' + Fore.RESET)
                    else:
                        print('\n' + Fore.RED + f'Item dengan kode {code_deleted} tidak ditemukan' + Fore.RESET)

            elif no_submenu_4 == 2:
                if empty_stock(): # Cek kalau stok kosong
                        continue # Lanjut dan kembali ke while loop submenu
                while True: # Konfirmasi hapus semua data
                    con_del_all = input(Fore.YELLOW + 'Apakah Anda yakin ingin menghapus SEMUA data? (y/n): ' + Fore.RESET).strip().lower()
                    if con_del_all == 'y':
                        list_stock.clear()  # Hapus semua data
                        print(Fore.GREEN + 'Semua data telah berhasil dihapus.' + Fore.RESET)
                        break # Break dari while loop konfirmasi
                    elif con_del_all == 'n':
                        print('\n' + Fore.RED + '             Proses dibatalkan' + Fore.RESET)
                        break # Break dari while loop konfirmasi
                    else:
                        print(Fore.RED + 'Input yang Anda masukkan salah' + Fore.RESET)

            elif no_submenu_4 == 3:
                print('\n' + Fore.BLUE + '           Kembali ke Main Menu' + Fore.RESET + '\n')
                break # Keluar dari submenu 4
            else:
                print('\n' + Fore.RED + '    Nomor yang Anda input tidak valid' + Fore.RESET)
        except ValueError:
            print('\n' + Fore.RED + '         Input harus berupa angka' + Fore.RESET)

def main_menu():
    while True:
        print(42*'~')
        print('\t\t'+'Main Menu')
        print(42*'~')
        print('1. Menampilkan list stok\n2. Menambahkan item\n3. Memperbarui data pada item\n4. Menghapus item\n5. Keluar dari program')
        try:
            nomor_menu = int(input('Masukkan angka menu yang ingin dijalankan (1-5): '))
            if nomor_menu == 1:
                sub_menu_1()
            elif nomor_menu == 2:
                sub_menu_2()
            elif nomor_menu == 3:
                sub_menu_3()
            elif nomor_menu == 4:
                sub_menu_4()
            elif nomor_menu == 5:
                print(42*'-')
                print(Fore.RED + '      '+'Anda telah keluar dari program' + Fore.RESET)
                print(42*'-')
                break
            else:
                print('\n' + Fore.RED + '     Nomor yang Anda input tidak valid' + Fore.RESET + '\n')
        except ValueError:
            print('\n' + Fore.RED + '         Input harus berupa angka' + Fore.RESET + '\n')

print('\n' + Fore.YELLOW + '~ Selamat Datang di Program Manajemen Stok ~' + Fore.RESET)
print(Fore.YELLOW + 44*'=' + Fore.RESET)
main_menu()