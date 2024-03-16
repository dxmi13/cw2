import timeit
import hashlib
import matplotlib.pyplot as plt
from typing import List

def measure_hash_speed(message: str) -> float:
    """
    Funkcja mierzy czas potrzebny na wygenerowanie hasha dla danej wiadomości.

    Parameters:
        message (str): Wiadomość, dla której będzie generowany hash.

    Returns:
        float: Czas w sekundach potrzebny na wygenerowanie hasha.
    """
    start_time = timeit.default_timer()
    hashlib.sha256(message.encode()).hexdigest()
    end_time = timeit.default_timer()
    return end_time - start_time

# Wybrane rozmiary wiadomości do testowania
message_sizes: List[int] = [10000, 100000, 1000000]
message_labels: List[str] = ['10KB', '100KB', '1MB']   # Podpisy dla rozmiarów wiadomości

# Pomiar czasu dla każdego rozmiaru wiadomości
times: List[float] = []
for size in message_sizes:
    message: str = 'a' * size
    time_taken: float = measure_hash_speed(message)
    times.append(time_taken)

# Tworzenie wykresu za pomocą Matplotlib
plt.plot(message_sizes, times, marker='o')
plt.title('Szybkość generowania hashy dla różnych rozmiarów wiadomości')
plt.xlabel('Rozmiar wiadomości')
plt.ylabel('Czas (s)')
plt.grid(True)

# Dodanie podpisów dla punktów na osi x
for i, txt in enumerate(message_labels):
    plt.text(message_sizes[i], times[i], txt, ha='right')

plt.show()
