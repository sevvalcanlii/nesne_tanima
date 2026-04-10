Gözlük Tipi Tespit Sistemi (Eyewear Detection)Bu proje, görüntü ve video karelerindeki Güneş Gözlüğü ve Optik Gözlük nesnelerini birbirinden ayırmak için geliştirilmiş bir derin öğrenme modelidir. 
Projenin Amacı Görüntü işleme tekniklerini kullanarak kullanıcıların yüzündeki gözlük tipini otomatik olarak belirlemek. Bu sistem, optik mağazaları veya sanal deneme uygulamaları için bir ön hazırlık aşaması olarak kullanılabilir. 
Öne Çıkan Özellikler Güneş Gözlüğü Tespiti: Koyu camlı ve güneş korumalı modellerin tanınması.
Optik Gözlük Tespiti: Şeffaf camlı, numaralı çerçevelerin ayırt edilmesi. Hızlı Çıkarım: YOLOv8 mimarisi sayesinde düşük gecikmeli (low-latency) çalışma. Veri Seti: Yaklaşık 1900 görüntüden oluşan, titizlikle etiketlenmiş veri seti. Teknik YığınModel: YOLOv8 (Ultralytics) Platform: Roboflow (Etiketleme) Ortam: Anaconda & Python 
Kütüphaneler: OpenCV, PyTorch, Matplotlib  Model Başarısı Modelin eğitim sürecinde elde edilen başarı oranları şu şekildedir:SınıfHassasiyet (Precision)Duyarlılık (Recall)mAP50Güneş Gözlüğü 0920.900.94Optik Gözlük 0.890.870.91Not: Eğitim süreci boyunca loss (kayıp) değerleri düzenli olarak takip edilmiş ve aşırı öğrenmeyi (overfitting) önlemek için erken durdurma uygulanmıştır. 
Kurulum ve ÇalıştırmaDepoyu bilgisayarınıza indirin:Bashgit clone https://github.com/kullaniciadi/gozluk-tespit-sistemi.git
Gerekli paketleri yükleyin:Bashpip install ultralytics opencv-python
Tahmin işlemini başlatın:Pythonfrom ultralytics import YOLO

model = YOLO('best.pt') # Eğitilmiş model ağırlığı
model.predict(source='deneme_fotografi.jpg', show=True)
 Klasör Yapısıdata/: Eğitim ve test için kullanılan görsel setleri. 
 weights/: En iyi sonucu veren best.pt dosyası. 
 results/: Eğitim grafikleriniz ve doğruluk matrisleriniz. 
