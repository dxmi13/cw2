import hashlib

C_SIZE: int = 65536 # rozmiar 64KB

def calculate_file_hash(file_path: str, algorithm: str = 'sha256', chunk_size: int = C_SIZE) -> str:
    """
    Oblicza sumę kontrolną (hash) pliku o podanej ścieżce przy użyciu określonego algorytmu.

    :param file_path: Ścieżka do pliku, którego suma kontrolna ma być obliczona.
    :type file_path: str

    :param algorithm: Nazwa algorytmu skrótu. Domyślnie 'sha256'.
    :type algorithm: str

    :param chunk_size: Rozmiar kawałka (w bajtach) do czytania pliku..
    :type chunk_size: int

    :return: Suma kontrolna (hash) obliczona dla pliku.
    :rtype: str
    """

    hash_function = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while True:
            chunk: bytes = f.read(chunk_size)
            if not chunk:
                break
            hash_function.update(chunk)
    return hash_function.hexdigest()

sha256sums_file: str = "SHA256SUMS.txt"

# Odczytanie oczekiwanego hashu z pliku SHA256SUMS.txt
with open(sha256sums_file, 'r') as f:
    expected_hash: str = f.readline().split()[0]

file_path: str = "ubuntu.iso"

# Obliczenie hashu pliku ubuntu.iso
file_hash: str = calculate_file_hash(file_path)

# Porównanie z oczekiwanym hashem
if file_hash == expected_hash:
    print("Hash się zgadza.")
else:
    print("Hash się nie zgadza.")
