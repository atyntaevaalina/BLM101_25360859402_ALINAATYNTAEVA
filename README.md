# BLM101 - Bilgisayar Mühendisliğine Giriş Dönem Projesi

Bu proje, **Bursa Teknik Üniversitesi** Bilgisayar Mühendisliği Bölümü, BLM101 dersi kapsamında hazırlanmıştır. Python programlama dili kullanılarak "Sanal Mantık Devresi Simülatörü" geliştirilmiştir.

## 👤 Öğrenci Bilgileri
* **Ad Soyad:** Alina ATYNTAEVA
* **Öğrenci No:** 25360859402
* **Bölüm:** Bilgisayar Mühendisliği

## 📚 Proje Konusu
**3. Grup: Veri Manipülasyonu ve Mantık Kapıları**
* **İlgili Kitap Bölümü:** Chapter 2 (2.1 Computer Architecture, 2.2 Machine Language)
* **Proje Başlığı:** Sanal Mantık Devresi Simülatörü

## 🎥 Proje Sunum Videosu
Projenin çalışmasını ve kodların anlatımını içeren YouTube videosuna aşağıdaki bağlantıdan ulaşabilirsiniz:

👉 **[YOUTUBE LİNK]** 👈

---

## 💻 Proje Açıklaması ve Kullanım

Bu proje, kullanıcının temel mantık kapılarını (AND, OR, NOT, XOR) kullanarak işlem yapmasını ve karmaşık mantıksal ifadelerin doğruluk tablolarını oluşturmasını sağlayan bir simülasyon aracıdır.

### Özellikler
1.  **Temel Kapı Hesaplama:** Kullanıcıdan alınan iki giriş değeri (0 veya 1) ve seçilen kapı türüne göre (AND, OR, vb.) sonuç üretir.
2.  **Doğruluk Tablosu Oluşturucu:** "A AND (B OR C)" gibi 3 değişkenli ifadeler için tüm olasılıkları hesaplayarak ekrana tablo şeklinde basar.

### 🚀 Kurulum ve Çalıştırma

Proje herhangi bir ek kütüphane kurulumu gerektirmez (Standart Python kütüphaneleri kullanılmıştır). Çalıştırmak için aşağıdaki adımları izleyin:

1.  Repoyu bilgisayarınıza klonlayın veya indirin.
2.  `src` (veya kodlar) klasörüne gidin.
3.  Terminal veya komut satırında şu komutu çalıştırın:
    ```bash
    python src/main.py
    ```
    *(Not: Dosya adınız farklıysa `main.py` yerine kendi dosya adınızı yazınız.)*

---

## 🔧 Algoritma ve Kod Mantığı

Kodlama sürecinde aşağıdaki mantıksal yaklaşım izlenmiştir:

1.  **Giriş Alma:** Kullanıcıdan input fonksiyonları ile mantık kapısı türü ve giriş değerleri (0/1) alınır.
2.  **Mantıksal Operatörler:** Python'un yerleşik `and`, `or`, `not`, `^` (XOR) operatörleri kullanılarak hesaplama fonksiyonları tanımlanmıştır.
3.  **Döngüler (Loops):** Doğruluk tablosu oluşturulurken, A, B ve C değişkenlerinin tüm olası durumları (000, 001, ... 111) iç içe döngüler veya iterasyon yöntemleri ile taranır.
4.  **Koşullu İfadeler (If/Else):** Kullanıcının seçtiği işleme göre doğru fonksiyonun çağrılması `if-elif-else` blokları ile kontrol edilmiştir.

---
