import hashlib

C_SIZE: int = 65536 # rozmiar 64KB

def calculate_file_hash(file_path: str, algorithm: str = 'sha256', chunk_size: int = C_SIZE) -> str:
    """
    Oblicza skrót (hash) podanego pliku używając określonego algorytmu.

    Parametry:
    file_path (str): Ścieżka do pliku, dla którego ma być obliczony skrót.
    algorithm (str): Nazwa algorytmu skrótu. Domyślnie 'sha256'.
    chunk_size (int): Rozmiar fragmentu danych odczytywanych z pliku na raz.

    Zwraca:
    str: Skrót (hash) obliczony dla podanego pliku.
    """
    hash_function = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while True:
            chunk: bytes = f.read(chunk_size)
            if not chunk:
                break
            hash_function.update(chunk)
    return hash_function.hexdigest()

binary_file_path: str = "ubuntu.iso"

file_hash: str = calculate_file_hash(binary_file_path)

print(f"Hash pliku {binary_file_path}: {file_hash}")