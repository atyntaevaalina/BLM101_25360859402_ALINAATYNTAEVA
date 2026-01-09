# ====== BOLUM 1: MANTIK LAPILARI ======

# BIR SAYI GIR: (0 veya 1)
A = int(input("Birinci girisi giriniz (0 veya 1): "))

# IKINCI SAYI GIR (0 veya 1)
B = int(input("Ikinci girisi giriniz (0 veya 1): "))

# MANTIK DEGERI SECIM MENUSU
print("\nKapi turunu seciniz:")
print("1 - AND")
print("2 - OR")
print("3 - XOR")
print("4 - NOT (sadece A icin)")

# KULANICI SECIMI 
choice = int(input("Seciminiz: "))

# KULANICI SECIMI
if choice == 1:
    print("Sonuc (AND):", A and B)
elif choice == 2:
    print("Sonuc (OR):", A or B)
elif choice == 3:
    print("Sonuc (XOR):", A ^ B)
elif choice == 4:
    print("Sonuc (NOT A):", not A)
else:
    print("Gecersiz secim!")


# ====== part 2: DOĞRULUK TABLOSU ======

print("\nA AND (B OR C) icin Dogruluk Tablosu")
print("A B C | Sonuc")
print("----------------")

#  A, B, C NIN TUM OLASI DEGERLERININ DENEMESI 
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            result = A and (B or C)
            print(A, B, C, "| ", result)
