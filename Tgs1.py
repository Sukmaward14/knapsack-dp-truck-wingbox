#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0/1 KNAPSACK PROBLEM - DYNAMIC PROGRAMMING IMPLEMENTATION
Optimasi Muatan Truk Wingbox
"""

class KnapsackDP:
    """
    Implementasi 0/1 Knapsack Problem menggunakan Dynamic Programming
    """

    def __init__(self, items, capacity):
        """
        Parameters:
        -----------
        items : list of tuple
            List berisi (nama_item, berat) untuk setiap item
        capacity : int/float
            Kapasitas maksimal knapsack dalam kg
        """
        self.items = items
        self.capacity = int(capacity * 10)  # Konversi ke 0.1 kg untuk handle desimal
        self.n = len(items)
        self.dp = None
        self.selected_items = []

    def solve(self):
        """
        Menyelesaikan 0/1 Knapsack menggunakan Dynamic Programming

        Returns:
        --------
        dict : Dictionary berisi hasil optimasi
        """
        # Step 1: Inisialisasi tabel DP
        # dp[i][w] = maksimal berat dengan i item dan kapasitas w
        self.dp = [[0 for _ in range(self.capacity + 1)] 
                   for _ in range(self.n + 1)]

        # Step 2: Isi tabel DP secara bottom-up
        for i in range(1, self.n + 1):
            name, weight = self.items[i-1]
            weight_int = int(weight * 10)

            for w in range(self.capacity + 1):
                # Opsi 1: Tidak ambil item i
                exclude = self.dp[i-1][w]

                # Opsi 2: Ambil item i (jika muat)
                if weight_int <= w:
                    include = self.dp[i-1][w - weight_int] + weight_int
                    self.dp[i][w] = max(include, exclude)
                else:
                    self.dp[i][w] = exclude

        # Step 3: Backtracking untuk mencari item terpilih
        self.selected_items = []
        w = self.capacity

        for i in range(self.n, 0, -1):
            if self.dp[i][w] != self.dp[i-1][w]:
                self.selected_items.append(self.items[i-1])
                weight_int = int(self.items[i-1][1] * 10)  # ✅ FIX: Ambil [1] untuk weight
                w -= weight_int

        self.selected_items.reverse()
        return {
            'max_weight': self.dp[self.n][self.capacity] / 10,
            'selected_items': self.selected_items,
            'dp_table': self.dp,
            'total_items': len(self.selected_items)
        }

    def print_solution(self):
        """Menampilkan hasil solusi dengan format yang rapi"""
        result = self.solve()

        print("="*70)
        print("HASIL OPTIMASI 0/1 KNAPSACK PROBLEM")
        print("="*70)

        print(f"\nKapasitas Knapsack: {self.capacity/10:.1f} kg")
        print(f"Jumlah Item Tersedia: {self.n}")

        print(f"\n{'='*70}")
        print("SOLUSI OPTIMAL:")
        print(f"{'='*70}")
        print(f"Total Berat Maksimal: {result['max_weight']:.1f} kg")
        print(f"Jumlah Item Terpilih: {result['total_items']} dari {self.n} item")
        print(f"Utilisasi Kapasitas: {(result['max_weight']/(self.capacity/10))*100:.2f}%")
        print(f"Sisa Kapasitas: {(self.capacity/10) - result['max_weight']:.1f} kg")

        print(f"\n{'='*70}")
        print("ITEM YANG DIMUAT:")
        print(f"{'='*70}")
        print(f"{'No.':<5} {'Nama Item':<20} {'Berat (kg)':<15}")
        print("-"*70)

        total_check = 0
        for idx, (name, weight) in enumerate(result['selected_items'], 1):
            print(f"{idx:<5} {name:<20} {weight:<15}")
            total_check += weight

        print("-"*70)
        print(f"{'TOTAL':<25} {total_check:<15.1f} kg")
        print("="*70)


def main():
    """Fungsi utama program"""

    # Data item muatan truk
    items_data = [
        ("Beras", 4.0),
        ("Semen", 5.0),
        ("Baja Ringan", 3.5),
        ("Kayu Olahan", 6.0),
        ("Pupuk", 4.2),
        ("Gula", 3.8),
        ("Minyak Goreng", 2.5),
        ("Kertas", 3.0),
        ("Mesin Kecil", 5.5),
        ("Plastik Industri", 2.0)
    ]

    # Kapasitas truk
    capacity = 25  # kg

    print("="*70)
    print("0/1 KNAPSACK PROBLEM - OPTIMASI MUATAN TRUK WINGBOX")
    print("="*70)

    print(f"\nDATA INPUT:")
    print("-"*70)
    print(f"{'No.':<5} {'Nama Item':<20} {'Berat (kg)':<15}")
    print("-"*70)
    for idx, (name, weight) in enumerate(items_data, 1):
        print(f"{idx:<5} {name:<20} {weight:<15}")
    print("-"*70)
    print(f"Kapasitas: {capacity} kg")
    print("="*70)

    # Buat solver dan jalankan
    solver = KnapsackDP(items_data, capacity)
    solver.print_solution()


if __name__ == "__main__":
    main()