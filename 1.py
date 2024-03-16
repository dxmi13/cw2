import hashlib
import time
from typing import List, Tuple, Callable

def main() -> None:
    """
    Obliczenie hashu wiadomości podanej przez użytkownika przy użyciu różnych algorytmów skrótu
    i zmierzenie czasu potrzebnego na każde obliczenie.
    """
    message: str = input("Enter the message to hash: ")
    
    # Definicja listy funkcji skrótu wraz z przykładowym polem długości, jeśli istnieje potrzeba
    hash_algorithms: List[Tuple[str, Callable[[str], str]]] = [
        ("SHAKE-256", lambda msg: hashlib.shake_256(msg.encode('utf-8')).hexdigest(64)),
        ("BLAKE2b", lambda msg: hashlib.blake2b(msg.encode('utf-8')).hexdigest()),
        ("RIPEMD160", lambda msg: hashlib.new('ripemd160', msg.encode('utf-8')).hexdigest()),
        ("SHA3-384", lambda msg: hashlib.sha3_384(msg.encode('utf-8')).hexdigest()),
        ("BLAKE2s", lambda msg: hashlib.blake2s(msg.encode('utf-8')).hexdigest()),
        ("SHA-512", lambda msg: hashlib.sha512(msg.encode('utf-8')).hexdigest()),
        ("SHA3-256", lambda msg: hashlib.sha3_256(msg.encode('utf-8')).hexdigest()),
        ("SHA3-512", lambda msg: hashlib.sha3_512(msg.encode('utf-8')).hexdigest()),
        ("MD5-SHA1", lambda msg: hashlib.new('md5-sha1', msg.encode('utf-8')).hexdigest()),
        ("SHA3-224", lambda msg: hashlib.sha3_224(msg.encode('utf-8')).hexdigest()),
        ("MD4", lambda msg: hashlib.new('md4', msg.encode('utf-8')).hexdigest()),
        ("MD5", lambda msg: hashlib.md5(msg.encode('utf-8')).hexdigest()),
        ("SHA-1", lambda msg: hashlib.sha1(msg.encode('utf-8')).hexdigest()),
        ("SHA512/224", lambda msg: hashlib.sha512(msg.encode('utf-8')).hexdigest()[:28]),
        ("Whirlpool", lambda msg: hashlib.new('whirlpool', msg.encode('utf-8')).hexdigest()),
        ("SM3", lambda msg: hashlib.new('sm3', msg.encode('utf-8')).hexdigest()),
        ("SHA-256", lambda msg: hashlib.sha256(msg.encode('utf-8')).hexdigest()),
        ("SHAKE-128", lambda msg: hashlib.shake_128(msg.encode('utf-8')).hexdigest(32)),
        ("SHA-224", lambda msg: hashlib.sha224(msg.encode('utf-8')).hexdigest()),
        ("SHA512/256", lambda msg: hashlib.sha512(msg.encode('utf-8')).hexdigest()[:32]),
        ("SHA-384", lambda msg: hashlib.sha384(msg.encode('utf-8')).hexdigest()),
        ("MDC2", lambda msg: hashlib.new('mdc2', msg.encode('utf-8')).hexdigest())
    ]
    # Iteracja przez funkcje i obliczanie czasu oraz skrótu wiadomości
    for algorithm, func in hash_algorithms:
        start_time: float = time.time()
        hash_result: str = func(message)
        end_time: float = time.time()
        print(f"{algorithm}: {hash_result} - Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()