import time

def cetak_dramatis(teks):
    """Fungsi untuk menampilkan teks dengan jeda 0.2 detik untuk efek dramatis"""
    for karakter in teks:
        print(karakter, end='', flush=True)
        time.sleep(0.2)
    print()  # Baris baru di akhir

def tampilkan_intro():
    """Menampilkan intro cerita dan penjelasan sistem"""
    print("=" * 60)
    print("    ⚡ DUNIA ISEKAI: PENGADILAN KEHIDUPAN ⚡")
    print("=" * 60)
    print("")
    print("📖 CERITA:")
    print("Kamu adalah manusia biasa yang baru saja meninggal.")
    print("Roh mu dibawa ke sebuah ruang gelap yang penuh misteri...")
    print("Di sini, dua kekuatan besar menunggu: MALAIKAT dan IBLIS")
    print("")
    print("Mereka akan menimbang SETIAP PERBUATAN BAIK dan BURUK mu")
    print("dalam hidup untuk menentukan tempat mu di dunia isekai!")
    print("")
    print("=" * 60)
    print("    📊 PENJELASAN SISTEM PERMAINAN 📊")
    print("=" * 60)
    print("")
    print("❤️ NYAWA (Health/Spiritual Strength):")
    print("   - Dimulai dengan: 100 poin")
    print("   - Setiap pilihan buruk mengurangi nyawa (-50)")
    print("   - Jika nyawa mencapai 0, kamu tergoyahkan dari keyakinan")
    print("   - Nyawa rendah = Jiwa lemah = Masuk ke tempat gelap")
    print("")
    print("💎 PAHALA (Karma Score/Reward Points):")
    print("   - Dimulai dengan: 1000 poin")
    print("   - Perbuatan baik menambah pahala (+500)")
    print("   - Perbuatan buruk mengurangi pahala (-200)")
    print("   - Pahala tinggi = Kebaikan mu terbukti = Surga menanti")
    print("")
    print("=" * 60)
    print("    🎯 TUJUAN AKHIR 🎯")
    print("=" * 60)
    print("")
    print("✨ SURGA (Best Ending):")
    print("   Pahala ≥ 1500 & Nyawa ≥ 75")
    print("   → Dijemput oleh para Malaikat!")
    print("")
    print("🌙 PURGATORI (Good Ending):")
    print("   Pahala 1000-1499 atau Nyawa 50-74")
    print("   → Berada di dunia tengah, menunggu takdir")
    print("")
    print("🔥 NERAKA (Bad Ending):")
    print("   Pahala < 1000 atau Nyawa < 50")
    print("   → Jatuh ke kegelapan karena perbuatan buruk!")
    print("")
    print("=" * 60)
    time.sleep(1)

def game_utama():
    tampilkan_intro()
    
    cetak_dramatis("Sekarang... beri tahu kami siapa nama mu!")
    nama = input("\n👤 Nama mu: ")
    
    # Inisialisasi variabel game
    nyawa = 100
    pahala = 1000
    
    print("")
    print(f"🕯️ Selamat datang di pengadilan, {nama}...")
    print("")
    print("📜 CATATAN MALAIKAT:")
    print(f"   Nama: {nama}")
    print(f"   ❤️ Kekuatan Spiritual (Nyawa): {nyawa}")
    print(f"   💎 Skor Kebaikan (Pahala): {pahala}")
    print("")
    print("Langit terbuka, dan kamu melihat dua jalan yang terbentang:")
    print("")
    
    # Pilihan pertama: Neraka atau Surga
    print("🔱 Jalan Kiri (NERAKA - Hitam & Berapi-api):")
    print("   Berkilau dengan kemewahan haram. Iblis tersenyum menggodamu.")
    print("")
    print("✨ Jalan Kanan (SURGA - Terang & Cahaya Emas):")
    print("   Bersinar dengan ketenangan abadi. Malaikat menunggu dengan penuh harap.")
    print("")
    
    # Validasi input pilihan
    pilihan = None
    while pilihan not in ["1", "2"]:
        try:
            pilihan = input("\nPilih jalan mana? (1=Neraka / 2=Surga): ").strip()
            if pilihan not in ["1", "2"]:
                cetak_dramatis("⚠️ Hanya masukkan 1 atau 2!")
                pilihan = None
        except Exception as e:
            cetak_dramatis(f"⚠️ Input tidak valid! Silakan coba lagi.")
            pilihan = None
    
    cetak_dramatis("")
    
    if pilihan == "1":
        cetak_dramatis("🔥 PILGRIM {nama} MEMILIH JALAN NERAKA! 🔥")
        cetak_dramatis("")
        cetak_dramatis("⚡ Ledakan api menyambutmu! Ribuan iblis berteriak kemenangan!")
        cetak_dramatis("Kamu memilih petualangan yang penuh dengan godaan dan kegelapan...")
        cetak_dramatis("Setiap langkah membawa kesakitan... Keyakinanmu goyah!")
        nyawa -= 50
        pahala -= 200
        cetak_dramatis(f"")
        cetak_dramatis(f"⚠️ PERUBAHAN STATUS:")
        cetak_dramatis(f"   ❤️ Nyawa: 100 → {nyawa} (BERKURANG 50!)")
        cetak_dramatis(f"   💎 Pahala: 1000 → {pahala} (BERKURANG 200!)")
        cetak_dramatis("")
        cetak_dramatis("😈 Iblis berbisik: 'Pilihan mu adalah permulaan menuju kehancuran...'")
        
    else:  # pilihan == "2"
        cetak_dramatis("✨ PILGRIM {nama} MEMILIH JALAN SURGA! ✨")
        cetak_dramatis("")
        cetak_dramatis("🌟 Cahaya hangat menampar wajahmu! Malaikat-malaikat menyanyikan nyanyian")
        cetak_dramatis("kidungan selamat datang. Kamu memilih jalan kebijaksanaan dan kebaikan!")
        cetak_dramatis("Setiap langkah membawa kedamaian... Jiwa mu diperkuat!")
        pahala += 500
        cetak_dramatis(f"")
        cetak_dramatis(f"✅ PERUBAHAN STATUS:")
        cetak_dramatis(f"   ❤️ Nyawa: Tetap {nyawa} (TERJAGA DENGAN BAIK)")
        cetak_dramatis(f"   💎 Pahala: 1000 → {pahala} (BERTAMBAH 500!)")
        cetak_dramatis("")
        cetak_dramatis("👼 Malaikat berbisik: 'Keputusan mu adalah cahaya yang memandu...'")
    
    # Status akhir dan penentuan akhir cerita
    print("")
    print("=" * 60)
    print("    ⚖️ PENGHITUNGAN AKHIR NASIB ⚖️")
    print("=" * 60)
    print(f"")
    print(f"📋 RINGKASAN PERJALANAN {nama.upper()}:")
    print(f"   ❤️ Kekuatan Spiritual Akhir: {nyawa}")
    print(f"   💎 Skor Kebaikan Akhir: {pahala}")
    print("")
    cetak_dramatis("🔮 PENGGABUNGAN DUA KEKUATAN...")
    print("")
    time.sleep(1)
    
    # Penentuan ending
    if pahala >= 1500 and nyawa >= 75:
        print("✨✨✨ KESIMPULAN: JALAN MENUJU SURGA SEJATI ✨✨✨")
        print("")
        print("🏆 ENDING: SURGA - THE BLESSED PARADISE")
        print("")
        print("Langit terbuka lebar. Ribuan malaikat turun menyambutmu!")
        print("Kebaikan hatimu yang murni dan jiwa yang kuat membawamu")
        print(f"ke istana cahaya abadi. Selamat datang di SURGA, {nama}!")
        print("")
        print("🎉 Kamu telah menyelesaikan permainan dengan ENDING TERBAIK!")
        
    elif pahala >= 1000 or nyawa >= 50:
        print("🌙🌙🌙 KESIMPULAN: BERJAGA DI DUNIA TENGAH 🌙🌙🌙")
        print("")
        print("🌍 ENDING: PURGATORI - THE MIDDLE REALM")
        print("")
        print("Kamu berada di wilayah dimana cahaya dan kegelapan berpadu.")
        print(f"Jiwa mu cukup kuat namun hati mu belum cukup murni, {nama}.")
        print("Di sini kamu harus belajar dan tumbuh sebelum")
        print("mencapai surga atau jatuh ke neraka. Takdir mu belum ditentukan...")
        print("")
        print("🎭 Kamu telah menyelesaikan permainan dengan ENDING NORMAL.")
        
    else:  # pahala < 1000 atau nyawa < 50
        print("🔥🔥🔥 KESIMPULAN: KEJATUHAN KE KEGELAPAN 🔥🔥🔥")
        print("")
        print("🔥 ENDING: NERAKA - THE CONDEMNED ABYSS")
        print("")
        print(f"Kegelapan menelan dirimu sepenuhnya, {nama}...")
        print("Perhitungan malaikat menunjukkan: Kebaikan mu terlalu sedikit,")
        print("dan jiwa mu sudah terlalu tergoyahkan. Kamu jatuh ke neraka")
        print("untuk menjalani hukuman sesuai dengan perbuatan burukmu.")
        print("")
        print("☠️ Kamu telah menyelesaikan permainan dengan ENDING TERBURUK.")
    
    print("")
    print("=" * 60)
    print("        PERMAINAN SELESAI - TERIMA KASIH BERMAIN")
    print("=" * 60)
    
if __name__ == "__main__":
    game_utama()