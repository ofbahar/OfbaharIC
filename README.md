![Logo](https://i.hizliresim.com/9iFCQT.png)
### Açıklama
- **Fotoğraf yığınınızı yüz tanıma ile kişilere göre klasörlere ayırmak ve dağınıklıktan kurtulmanızı sağlamak için yazılmış bir program.

### Uyarılar

- Windows ve MacOS ile uyumlu değildir!
- Python3+ ile uyumludur!

### Kullanılan Kütüphaneler

- face_recognition
- os
- cv2
- numpy
- time
- urllib

### Kurulum (Debian)
```
1) git clone https://github.com/ofbahar/OfbaharIC.git
2) cd OfbaharIC/
3) sudo -H pip3 install -r requirements.txt
4) python3 OfbaharIC.py
```
### Kullanım

- python3 Ofbahar.py komutuyla program çalıştırıldıktan sonra tanınması gereken kişilerin bulunduğu klasörün yolu isteniyor.
- Kişiler klasörü girildikten sonra ayrıştırılacak fotoğrafların bulunduğu klasör yolu isteniyor.
- Daha sonra program "Katalog" isimli bir klasör açıp içerisine kişiler klasöründeki isimler için klasör açıyor. Tanınmayan kişiler için "Unknown", manzara fotoğrafları için "Manzara", birden fazla kişinin aynı fotğrafta bulunmasına karşın "Ortak" klasörü açılıyor.
- Son olarak ayırma işlemi yapılıp raporlar gösteriliyor. 

### Ekran Fotoğrafları
![Kayıt_1](https://i.hizliresim.com/Lft0mG.png)
![Kayıt_2](https://i.hizliresim.com/kursOl.png)
