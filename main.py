import time

def cetak_dramatis(teks):
    """Fungsi untuk menampilkan teks dengan jeda 0.2 detik untuk efek dramatis"""
    for karakter in teks:
        print(karakter, end='', flush=True)
        time.sleep(0.2)
    print()  # Baris baru di akhir

def tampilkan_intro():
    """Menampilkan intro cerita dan penjelasan sistem"""
    cetak_dramatis("=" * 60)
    cetak_dramatis("    ⚡ DUNIA ISEKAI: PENGADILAN KEHIDUPAN ⚡")
    cetak_dramatis("=" * 60)
    cetak_dramatis("")
    cetak_dramatis("📖 CERITA:")
    cetak_dramatis("Kamu adalah manusia biasa yang baru saja meninggal.")
    cetak_dramatis("Roh mu dibawa ke sebuah ruang gelap yang penuh misteri...")
    cetak_dramatis("Di sini, dua kekuatan besar menunggu: MALAIKAT dan IBLIS")
    cetak_dramatis("")
    cetak_dramatis("Mereka akan menimbang SETIAP PERBUATAN BAIK dan BURUK mu")
    cetak_dramatis("dalam hidup untuk menentukan tempat mu di dunia isekai!")
    cetak_dramatis("")
    cetak_dramatis("=" * 60)
    cetak_dramatis("    📊 PENJELASAN SISTEM PERMAINAN 📊")
    cetak_dramatis("=" * 60)
    cetak_dramatis("")
    cetak_dramatis("❤️ NYAWA (Health/Spiritual Strength):")
    cetak_dramatis("   - Dimulai dengan: 100 poin")
    cetak_dramatis("   - Setiap pilihan buruk mengurangi nyawa (-50)")
    cetak_dramatis("   - Jika nyawa mencapai 0, kamu tergoyahkan dari keyakinan")
    cetak_dramatis("   - Nyawa rendah = Jiwa lemah = Masuk ke tempat gelap")
    cetak_dramatis("")
    cetak_dramatis("💎 PAHALA (Karma Score/Reward Points):")
    cetak_dramatis("   - Dimulai dengan: 1000 poin")
    cetak_dramatis("   - Perbuatan baik menambah pahala (+500)")
    cetak_dramatis("   - Perbuatan buruk mengurangi pahala (-200)")
    cetak_dramatis("   - Pahala tinggi = Kebaikan mu terbukti = Surga menanti")
    cetak_dramatis("")
    cetak_dramatis("=" * 60)
    cetak_dramatis("    🎯 TUJUAN AKHIR 🎯")
    cetak_dramatis("=" * 60)
    cetak_dramatis("")
    cetak_dramatis("✨ SURGA (Best Ending):")
    cetak_dramatis("   Pahala ≥ 1500 & Nyawa ≥ 75")
    cetak_dramatis("   → Dijemput oleh para Malaikat!")
    cetak_dramatis("")
    cetak_dramatis("🌙 PURGATORI (Good Ending):")
    cetak_dramatis("   Pahala 1000-1499 atau Nyawa 50-74")
    cetak_dramatis("   → Berada di dunia tengah, menunggu takdir")
    cetak_dramatis("")
    cetak_dramatis("🔥 NERAKA (Bad Ending):")
    cetak_dramatis("   Pahala < 1000 atau Nyawa < 50")
    cetak_dramatis("   → Jatuh ke kegelapan karena perbuatan buruk!")
    cetak_dramatis("")
    cetak_dramatis("=" * 60)
    time.sleep(1)

def game_utama():
    tampilkan_intro()
    
    cetak_dramatis("Sekarang... beri tahu kami siapa nama mu!")
    nama = input("\n👤 Nama mu: ")
    
    # Inisialisasi variabel game
    nyawa = 100
    pahala = 1000
    
    cetak_dramatis("")
    cetak_dramatis(f"🕯️ Selamat datang di pengadilan, {nama}...")
    cetak_dramatis("")
    cetak_dramatis("📜 CATATAN MALAIKAT:")
    cetak_dramatis(f"   Nama: {nama}")
    cetak_dramatis(f"   ❤️ Kekuatan Spiritual (Nyawa): {nyawa}")
    cetak_dramatis(f"   💎 Skor Kebaikan (Pahala): {pahala}")
    cetak_dramatis("")
    cetak_dramatis("Langit terbuka, dan kamu melihat dua jalan yang terbentang:")
    cetak_dramatis("")
    
    # Pilihan pertama: Neraka atau Surga
    cetak_dramatis("🔱 Jalan Kiri (NERAKA - Hitam & Berapi-api):")
    cetak_dramatis("   Berkilau dengan kemewahan haram. Iblis tersenyum menggodamu.")
    cetak_dramatis("")
    cetak_dramatis("✨ Jalan Kanan (SURGA - Terang & Cahaya Emas):")
    cetak_dramatis("   Bersinar dengan ketenangan abadi. Malaikat menunggu dengan penuh harap.")
    cetak_dramatis("")
    
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
    cetak_dramatis("")
    cetak_dramatis("=" * 60)
    cetak_dramatis("    ⚖️ PENGHITUNGAN AKHIR NASIB ⚖️")
    cetak_dramatis("=" * 60)
    cetak_dramatis(f"")
    cetak_dramatis(f"📋 RINGKASAN PERJALANAN {nama.upper()}:")
    cetak_dramatis(f"   ❤️ Kekuatan Spiritual Akhir: {nyawa}")
    cetak_dramatis(f"   💎 Skor Kebaikan Akhir: {pahala}")
    cetak_dramatis("")
    cetak_dramatis("🔮 PENGGABUNGAN DUA KEKUATAN...")
    cetak_dramatis("")
    time.sleep(1)
    
    # Penentuan ending
    if pahala >= 1500 and nyawa >= 75:
        cetak_dramatis("✨✨✨ KESIMPULAN: JALAN MENUJU SURGA SEJATI ✨✨✨")
        cetak_dramatis("")
        cetak_dramatis("🏆 ENDING: SURGA - THE BLESSED PARADISE")
        cetak_dramatis("")
        cetak_dramatis("Langit terbuka lebar. Ribuan malaikat turun menyambutmu!")
        cetak_dramatis("Kebaikan hatimu yang murni dan jiwa yang kuat membawamu")
        cetak_dramatis("ke istana cahaya abadi. Selamat datang di SURGA, {nama}!")
        cetak_dramatis("")
        cetak_dramatis("🎉 Kamu telah menyelesaikan permainan dengan ENDING TERBAIK!")
        
    elif pahala >= 1000 or nyawa >= 50:
        cetak_dramatis("🌙🌙🌙 KESIMPULAN: BERJAGA DI DUNIA TENGAH 🌙🌙🌙")
        cetak_dramatis("")
        cetak_dramatis("🌍 ENDING: PURGATORI - THE MIDDLE REALM")
        cetak_dramatis("")
        cetak_dramatis("Kamu berada di wilayah dimana cahaya dan kegelapan berpadu.")
        cetak_dramatis("Jiwa mu cukup kuat namun hati mu belum cukup murni, {nama}.")
        cetak_dramatis("Di sini kamu harus belajar dan tumbuh sebelum")
        cetak_dramatis("mencapai surga atau jatuh ke neraka. Takdir mu belum ditentukan...")
        cetak_dramatis("")
        cetak_dramatis("🎭 Kamu telah menyelesaikan permainan dengan ENDING NORMAL.")
        
    else:  # pahala < 1000 atau nyawa < 50
        cetak_dramatis("🔥🔥🔥 KESIMPULAN: KEJATUHAN KE KEGELAPAN 🔥🔥🔥")
        cetak_dramatis("")
        cetak_dramatis("🔥 ENDING: NERAKA - THE CONDEMNED ABYSS")
        cetak_dramatis("")
        cetak_dramatis("Kegelapan menelan dirimu sepenuhnya, {nama}...")
        cetak_dramatis("Perhitungan malaikat menunjukkan: Kebaikan mu terlalu sedikit,")
        cetak_dramatis("dan jiwa mu sudah terlalu tergoyahkan. Kamu jatuh ke neraka")
        cetak_dramatis("untuk menjalani hukuman sesuai dengan perbuatan burukmu.")
        cetak_dramatis("")
        cetak_dramatis("☠️ Kamu telah menyelesaikan permainan dengan ENDING TERBURUK.")
    
    cetak_dramatis("")
    cetak_dramatis("=" * 60)
    cetak_dramatis("        PERMAINAN SELESAI - TERIMA KASIH BERMAIN")
    cetak_dramatis("=" * 60)
    
if __name__ == "__main__":
    game_utama()