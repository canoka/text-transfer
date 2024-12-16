# 📱 Text Transfer Uygulaması

**Text Transfer Uygulaması**, bir bilgisayar ve telefon arasında metin transferi yapmanıza olanak tanır. Bu uygulama, yerel sunucu üzerinden çalışır ve metin gönderme ve alma işlemleri basit ve hızlı bir şekilde gerçekleştirilir. 

---

## 💡 Uygulama Nedir?

Bu uygulama, telefonunuzdan bilgisayarınıza veya bilgisayarınızdan telefonunuza metin göndermenizi sağlar. Basit bir kullanıcı arayüzü ile çalışan bu uygulama, kullanıcıların metin paylaşımını hızlıca yapmalarına olanak tanır.

---

## 🛠️ Gereksinimler

Uygulamayı çalıştırabilmek için aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

### 1. Flask
Flask, bu uygulamanın temelini oluşturan hafif bir Python web framework'üdür. Flask kullanılarak API'ler oluşturulmakta ve veriler yerel olarak aktarılmaktadır.

```bash
pip install Flask
```

---

## ⚙️ Uygulamanın Çalıştırılması

### 1. Depoyu Klonlama
Uygulamayı kullanmak için, bu depoyu bilgisayarınıza klonlayın.

```bash
git clone https://github.com/canoka/text-transfer.git
cd text-transfer
```

### 2. Gerekli Kütüphaneleri Yükleme
Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Başlatma
Uygulamayı başlatmak için terminal veya komut satırında aşağıdaki komutu çalıştırın:

```bash
python app.py
```

Uygulama başarılı bir şekilde başlatıldığında, terminalde şu çıktıyı görmelisiniz:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Bu, uygulamanın yerel sunucunuzda çalıştığını ve erişilebildiğini gösterir.

---

## 📱 Mobilde Uygulama Nasıl Çalıştırılır?

Uygulama mobil cihazınızda da çalışabilir. Aşağıdaki adımları izleyerek telefondan da uygulamayı kullanabilirsiniz:

1. **Telefon ve Bilgisayar Aynı Ağda Olmalı:** Telefonunuzun ve bilgisayarınızın aynı Wi-Fi ağına bağlı olması gerekir.
   
2. **IP Adresi ile Erişim:** Flask sunucu başlatıldığında, terminalde gösterilen IP adresini (örneğin `http://127.0.0.1:5000/`) kullanarak, telefonunuzun tarayıcısına bu IP'yi girerek uygulamayı açabilirsiniz. Eğer telefonunuzdan bu IP'yi giremezseniz, bilgisayarınızın **yerel ağ IP adresini** (örneğin `192.168.x.x`) kullanarak erişebilirsiniz.

---

## 💻 Uygulama Arayüzü

Uygulamanın basit ve şık bir arayüzü vardır. İki ana bölümden oluşur:

1. **Metin Gönderme:**
    - Kullanıcılar burada metinlerini girer ve `Gönder` butonuna basarak metni bilgisayar veya telefona gönderir.
   
2. **Metin Alma:**
    - Kullanıcılar `Yenile` butonuna basarak, daha önce gönderilen metni görüntüleyebilirler.

---

## 🎨 Kullanıcı Arayüzü Özellikleri

- **Responsive Tasarım:** Hem masaüstü hem de mobil cihazlarda sorunsuz çalışacak şekilde tasarlanmıştır.
- **Animasyonlar:** Modern bir görünüm için animasyon efektleri kullanılmıştır.
- **Renkli ve Dikkat Çekici Butonlar:** Kullanıcı dostu ve şık butonlar ile uygulamanız modern bir görünüm sunar.

---

## 📚 Lisans

Bu proje, **MIT Lisansı** ile lisanslanmıştır. Detaylı bilgiye [LICENSE](LICENSE) dosyasından ulaşabilirsiniz.

---
