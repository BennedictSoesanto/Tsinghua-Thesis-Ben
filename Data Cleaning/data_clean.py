import pandas as pd
import unicodedata

"""
df = pd.read_csv('Thesis Results.csv')

mappings = {
    'BAC3': {
        'Kurang dari Rp2jt': 1,
        'Rp2-5jt': 2,
        'Rp5-10jt': 3,
        'Rp10-15jt': 4,
        'Lebih dari Rp15jt': 5
    },
    'BAC4': {
        'Tidak bersekolah': 1,
        'SD': 2,
        'SMP': 3,
        'SMA/SMK': 4,
        'Diploma/Sarjana': 5
    },
    'BAC5': {
        'Ya, keduanya': 1,
        'Ya, komputer': 1,
        'Ya, smartphone': 1,
        'Tidak memiliki keduanya': 0
    },
    'BAC6': {
        'Padi': 1, 'Cabai': 2, 'Tomat': 3, 'Kentang': 4, 'Terong': 5,
        'Kol': 6, 'Jagung': 7, 'Jeruk': 8, 'Wortel': 9, 'Bonsai': 10,
        'Pisang': 11, 'Singkong': 12, 'Ubi': 13, 'Sawit': 14,
        'Karet': 15, 'Bawang merah': 16
    },
    'BAC7': {
        'Ya': 1,
        'Tidak': 0
    },
    'BAC8': {
        'Jawa Tengah': 1,
        'Sumut': 2,
        'Jawa Barat': 3,
        'Lampung': 4
    },
    'SRI3': {
        'Ya': 1,
        'Tidak': 0
    },
    'IMP2' : {
        'Tidak yakin': 1,
        'Kurang dari 1 tahun' : 2,
        '1-3 tahun' : 3,
        'Lebih dari 3 tahun' : 4,
    }
}

df.replace(mappings, inplace=True)

df.to_csv('Cleaned Results.csv', index=False)

df = pd.read_csv('Cleaned Results.csv')

options = [
    "Kurangnya pengetahuan dan/atau pelatihan",
    "Biaya yang terlalu tinggi",
    "Kurangnya infrastruktur (contoh: internet, listrik)",
    "Hasil keuntungan yang belum pasti",
    "Penolakan dari pekerja di ladang"
]

for i, option in enumerate(options, start=1):
    column_name = f'INO2_{i}'
    df[column_name] = df['INO2'].apply(lambda x: 1 if option in str(x) else 0)

df.drop(columns=['INO2'], inplace=True)

df.to_csv('Cleaned Results2.csv', index=False)
"""

df = pd.read_csv('Cleaned Results2.csv')

com1_options = [
    "Layanan penyuluhan dari pemerintah",
    "Universitas atau lembaga pendidikan pertanian",
    "Perusahaan atau konsultan swasta",
    "Sumber online (internet, media sosial)",
    "Petani lain",
    "Asosiasi atau Kelompok tani",
    "Media (TV, radio, koran)"
]

out2_options = [
    "Lebih banyak subsidi dari pemerintah",
    "Infrastruktur internet atau listrik yang lebih baik",
    "Akses pelatihan dan pengetahuan yang lebih mudah",
    "Harga teknologi yang lebih terjangkau",
    "Dukungan dari petani lain atau koperasi pertanian"
]

def create_binary_columns(df, column_name, options):
    for i, option in enumerate(options, start=1):
        new_col = f"{column_name}_{i}"
        df[new_col] = df[column_name].apply(lambda x: 1 if option in str(x) else 0)
    df.drop(columns=[column_name], inplace=True)  # Drop the original column
    
create_binary_columns(df, 'COM1', com1_options)
create_binary_columns(df, 'OUT2', out2_options)

df.to_csv('final_cleaned.csv', index=False)