from PIL import Image

def gambar_ke_ascii_detail(path_gambar, lebar_baru=100):
    """Mengubah gambar menjadi ASCII art yang lebih detail.

    Args:
        path_gambar (str): Path ke file gambar.
        lebar_baru (int): Lebar maksimum dari hasil ASCII art.

    Returns:
        str: Representasi ASCII art yang lebih detail dari gambar.
    """
    try:
        gambar = Image.open(path_gambar).convert('L')  # Buka gambar dan konversi ke grayscale
    except FileNotFoundError:
        return "Error: File gambar tidak ditemukan."

    lebar, tinggi = gambar.size
    rasio_aspek = tinggi / lebar
    tinggi_baru = int(lebar_baru * rasio_aspek * 0.55) # Kompresi vertikal untuk tampilan yang lebih baik
    gambar_resized = gambar.resize((lebar_baru, tinggi_baru))
    piksel = gambar_resized.getdata()

    karakter = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/;:,\"^`'. "
    panjang_karakter = len(karakter)

    ascii_art = ""
    for pixel_value in piksel:
        index = pixel_value * panjang_karakter // 255
        ascii_art += karakter[panjang_karakter - 1 - index] # Urutan terbalik untuk gelap ke terang
    return [ascii_art[i:i+lebar_baru] for i in range(0, len(ascii_art), lebar_baru)]

if __name__ == "__main__":
    path_gambar = input("Path lengkap gambar: ")
    lebar_hasil = int(input("Ukuran Ascii: "))

    hasil_ascii = gambar_ke_ascii_detail(path_gambar, lebar_hasil)

    if isinstance(hasil_ascii, str) and hasil_ascii.startswith("Error"):
        print(hasil_ascii)
    else:
        for baris in hasil_ascii:
            print(baris)