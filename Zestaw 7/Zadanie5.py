# Zadanie 4 - Tim sort

import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  # liczba elementów, można zmieniać
FPS = 60  # klatki na sekundę do parametru interval 

tablica = MonitorowanaTablica(0, 1000, N, "T") # zbadaj też opcje: "S", "A", "T"
algorytm = "Tim sort"

def min_run(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def insertion(tab, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and tab[j] < tab[j - 1]:
            tab[j], tab[j - 1] = tab[j - 1], tab[j]
            j -= 1


def merge(tab, left, middle, right):
    left_arr = []
    right_arr = []
    l1 = middle - left + 1
    l2 = right - middle

    for i in range(l1):
        left_arr.append(tab[left + i])
    for i in range(l2):
        right_arr.append(tab[middle + 1 + i])

    i = 0
    j = 0
    k = left

    while i < l1 and j < l2:
        if left_arr[i] <= right_arr[j]:
            tab[k] = left_arr[i]
            i+=1
        else:
            tab[k] = right_arr[j]
            j += 1
        k += 1

    while j < l2:
        tab[k] = right_arr[j]
        k += 1
        j += 1

    while i < l1:
        tab[k] = left_arr[i]
        k += 1
        i += 1


def tim_sort(tab):
    n = len(tab)
    minimum = min_run(n)

    for right in range(0,n,minimum):
        left = min(right+minimum-1, n-1)
        insertion(tab, right, left)
    
    size = minimum
    while(size < n):
        for left in range(0,n, 2*size):
            middle = min(n-1, left+size-1)
            right = min((left+2*size-1), (n-1))

            if(middle<right):
                merge(tab,left,middle,right)
        size=2*size


t0 = time.perf_counter()
tim_sort(tablica)
delta_t = time.perf_counter() - t0


###############################################
###############################################
print(f"Sortowanie: {algorytm}")
print(f"Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.")
###############################################

# konfiguracja wyświetlania histogramu
plt.rcParams["font.size"] = 16
fig, ax = plt.subplots(figsize=(16, 8))
container = ax.bar(np.arange(0, len(tablica), 1), tablica.pelne_kopie[0], align="edge", width=0.8)
fig.suptitle(f"Sortowanie: {algorytm}")
ax.set(xlabel="Indeks", ylabel="Wartość")
ax.set_xlim([0, N])
txt = ax.text(0.01, 0.99, "", ha="left", va="top", transform=ax.transAxes)

# funkcja aktualizująca stan poszczególnych klatek do wyświetlenia
def update(frame):
    txt.set_text(f"Liczba operacji = {frame}")
    for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
        rectangle.set_height(height)
        rectangle.set_color("darkblue")

    idx, op = tablica.aktywnosc(frame)
    if op == "get":
        container.patches[idx].set_color("green")
    elif op == "set":
        container.patches[idx].set_color("red")

    return (txt, *container)

# tu akumulowana jest animacja, wyświetlna komendą show
ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./FPS, repeat=False)
plt.show()